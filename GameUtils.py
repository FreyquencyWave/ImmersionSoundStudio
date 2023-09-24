# 
# These are either packages we need or will need later

import sys
import os
import re
import pickle       # for serialising and saving objects
import pygame
from pygame import *
from pygame.locals import *
from enum import Enum
from Soundscape import SoundMap, Source, stereo_vol, distance
from SoundsX import *
from os.path import expanduser

play_cut_scene=True
current_level=None
savefile=".SavedGame"        # Name for file conaying saved game
bag=[]                      # Collected sounds
played_scenes=[]            # List of played cutscenes, prevents repetition
channel_id=[]
step=1.5                      # size of mves for each arrow press
SIZE=100                    # Default size of sondscapes
near=SIZE                   # Distance to nearest sound
restored=False              # Has game ben previously saved
nearestsound=None           
mixer.set_num_channels(128) # Maximum number of simultaneous sounds


class Option(Enum):

    # Options for the main game menu
    START = 1
    RESTORE = 2
    EXIT = 3

# Create opening menu

options={"Start game":Option.START,
              "Restore game":Option.RESTORE,
              "Quit":Option.EXIT}

class SavedGame:
#  This is a structure we put all the necessary information to save the game into.
# Saving will entail constructing it, serialising it and writing it to a file.
# Reloading will entail reading from the file, deserialising and restting all the values from the structure.
    def __init__(self, bag, escape, position, played):
        self.bag=bag
        self.i=escape
        self.position=position
        self.played=played
        
class Emgame:
# This will contain most of the functionality of your game
# Mostly sets up a window for the game
# and loads an image into it
    def __init__(self):
        global prog
        img=pygame.image.load(bundle_dir+"/"+'/start_image.jpg')
        width= img.get_width()
        height=img.get_height()
        screen=pygame.display.set_mode((width,height))
        pygame.display.flip()
        pygame.display.set_caption("Immersion SoundStudio")      
        img.convert()
        rect=img.get_rect()
        screen.blit(img,rect)
        pygame.draw.rect(screen,(0,0,150), rect, 1)
        pygame.display.update()

    def tidy_up(self):
        pass       

        
    def get_command(self):
        # Uses the keyboard event system to get the last key press
        pygame.event.clear()
        while True:
            events =  pygame.event.get()
            while  events == None:
               events =  pygame.event.get()
            for ev in events:
                if ev.type==QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    key = ev.key
                    pygame.event.clear()
                    return ev.key

 
    def do_command(self,com):
        global near,nearestsound,nextscape,bag,currentscape, played_scenes, play_cut_scene
        match com:
            case pygame.K_q:    # Quit game
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
            case pygame.K_UP:   # Up arrow
                x,y=self.player
                self.walk()
                if y <SIZE :  y+=step
                self.player=(x,y)
                self.adjust_volumes()

            case pygame.K_DOWN:     # Down arrow
                x,y=self.player
                self.walk()
                if y > -SIZE :  y-=step
                self.player=(x,y)
                self.adjust_volumes()

            case pygame.K_RIGHT:    # Right arrow
                x,y=self.player
                self.walk()
                if x <SIZE :  x+=step
                self.player=(x,y)
                self.adjust_volumes()

            case pygame.K_LEFT:     # Left arrow
                x,y=self.player
                self.walk()
                if x > -SIZE :  x-=step
                self.player=(x,y)
                self.adjust_volumes()

            case pygame.K_l:        # L - leave soundscape
                self.start_soundscape()

            case pygame.K_x:        # Exit to previous soundscape (if allowed)
                if currentscape.prev != None:
                    nextscape= currentscape.prev
                    nextscape.enter=currentscape.enter
                    self.start_soundscape()

            case pygame.K_RETURN | pygame.K_e: # Take door through a sound object
                distance = 25
                if near <= distance:
                    if nearestsound.exitscape != None:
                        nextscape=nearestsound.exitscape
                        near=nextscape.xmax*2
                        self.start_soundscape()
                        
            case pygame.K_SPACE:    # Collect sound
                distance = 25
                if nearestsound !=  None:
                    if near <= distance:
                        if nearestsound not in bag:
                            if nearestsound.namesound == None:
                                pass
                            else:
                                self.play_sound('OPENJAR',0)
                                self.play_sound(nearestsound.namesound,0)
                                bag.append(nearestsound)
                        else:
                            self.play_sound('ALREADYCOLLECTED',0)
                    else:
                        self.play_sound('NOTNEAR',0)
                        pass
                    
            case pygame.K_b:        # List collected sounds
                if bag != []:
                    self.play_sound('OPENANDCLOSE',1)
                    for j in bag:
                        self.play_sound(j.namesound,1)
                    self.play_sound('OPENANDCLOSE',1)
                pass

            case pygame.K_c:        # Toggle playing cutstrnes
                play_cut_scene = not play_cut_scene
                self.play_sound('SKIP',0)
                        
            case pygame.K_s:        # Save game
                prog=sys.argv[0]
                sv=SavedGame(bag,currentscape,self.player,played_scenes)
                with open(expanduser("~")+"/"+savefile+".dat","wb") as outfile:
                    pickle.dump(sv,outfile)
                    outfile.close()  
                    self.play_sound('REMOVE',0)
                
    

    def show_menu(self,menu):
        global currentscape, nextscape, newgame, restored,bag, played_scenes

        # Set up Menu
        # Create some variables containing the sounds for each menu item
        
        startvo='START'
        continuevo='CONTINUE'
        cancelvo='CANCEL'

        # And also the sound to be played when an item is chosen
        click='CLICK'

        # A list containing the sounds for the menu items
        startmenu= [startvo,continuevo,cancelvo]
        # A sound for the game starting jingle
        # Create the sound play it and wait for it to finish
        # self.jingle='JINGLE'

        self.play_on_chan(bg_music,'JINGLE')
        self.wait_on_channel(bg_music)
        #self.menubg=mmap['MENU']
        #bg_music.play(self.menubg)
        #self.wait_on_channel(bg_music)
        self.play_on_chan(bg_music,'MENU',loops=-1)

        # Now get the player to choose a menu item
        # Start with the firstone
        current_menuitem=0
        
        # Keep going round in a loop until a selection is made
        while True :
            # Play the sound for the current item and wait for it to finish
            #speech.play(mmap[startmenu[current_menuitem]])
            #self.wait_on_channel(speech)

            # Get a player command from the keyboard
            # tHe only commands which work here are UP, DOWN and SPACE

            cm=self.get_command()
            self.play_sound('CLICK2',wait=0)
            if cm == pygame.K_DOWN:

                # Move to the next item in the menu
                current_menuitem=(current_menuitem+1)%len(startmenu)
                
            elif cm == pygame.K_UP:
                # Move to the previous item in the menu
                current_menuitem=(current_menuitem-1)%len(startmenu)

            elif cm == pygame.K_RETURN:
                pass
                
            elif cm == pygame.K_SPACE:
                # Choose the current item
                 # Play the click sound amd wait for it to finish
                pygame.key.set_repeat(200,200)
                bg_music.stop()
                #bg_music.play(mmap[click])
                if current_menuitem == 0 :
                    self.play_on_chan(bg_music,click)
                    self.wait_on_channel(bg_music)
                    self.start_soundscape()
                    return
                elif current_menuitem == 1 :
                    # Continue -  restart a previous game
                    try:
                        infile = open(expanduser("~")+"/"+savefile+".dat","rb") 
                        newgame=pickle.load(infile)
                        infile.close()
                        bag=newgame.bag
                        currentscape=newgame.i
                        pl=newgame.position
                        restored=True
                        played_scenes=newgame.played
                        nextscape=newgame.i
                        self.play_on_chan(bg_music,click)
                        self.wait_on_channel(bg_music)
                        self.start_soundscape(pl) 
                        return
                    except:
                        self.play_sound('NOGAME',wait=1)
                        self.tidy_up()
                        sys.exit(0)
                    #return
                elif current_menuitem ==2 :
                    # Cancel - tidy up and exit
                    self.tidy_up()
                    sys.exit(0)
                #return


            self.play_on_chan(speech,startmenu[current_menuitem])
            self.wait_on_channel(speech) 
            # Otherwise carry on round again
       

    def continue_game(self) :

        # Doesn't do anything yet
        self.tidy_up()
        sys.exit(0)

    def wait_on_channel(self,ch):
        # Just loop until the chosen channel is not playing anything._
        while ch.get_busy() :
            pass

    def adjust_volumes(self):
        global near,nearestsound
        near=SIZE
        for s in currentscape.tlist:
            dist=distance(self.player,(s.x,s.y))
            if dist < near :
                nearestsound=s
                near=dist
            lv,rv=stereo_vol(self.player,(s.x,s.y))
            channel_id[s.ch].set_volume(lv,rv)
        pass
    
    def start_soundscape(self,p=(0,0)):
        global currentscape, nextscape, restored, played_scenes
        # Start first soundscape
        if nextscape  == None:
            self.end_game()
        currentscape=nextscape   # Move on one soundscape
        nextscape=currentscape.next
        mixer.stop()             # Stop all currently opaying sounds
        channel_id.clear()
        # Play cutscene if present and not previously played
        if currentscape.cutscene != None:
            if currentscape.cutscene not in played_scenes:
                if play_cut_scene:
                    self.play_sound(currentscape.cutscene, wait=1)
                    played_scenes.append(currentscape.cutscene)
        restored= False
        self.play_sound(currentscape.enter, wait=0)
        self.play_on_chan(bg_music,currentscape.bg,loops=-1)
        bg_music.set_volume(0.25)
        # Play entry voice over
        if currentscape.entervo != None:
           self.play_sound(currentscape.entervo,wait=0)
        currentscape.enter=currentscape.enter_save


        # Set player to centre of soundscape
        self.player = p
        for s in currentscape.tlist:   # Play all sounds
            new_ch=mixer.find_channel()
            if new_ch not in channel_id:
                channel_id.append(new_ch)             
                s.ch=channel_id.index(new_ch)
            self.play_on_chan(channel_id[s.ch],s.sound,loops=s.loop)
            x=s.x
            y=s.y
            dst=distance(self.player,(x,y))
            lv,rv=stereo_vol(self.player,(x,y))
            channel_id[s.ch].set_volume(lv,rv)
        self.adjust_volumes()
            
    def play_sound(self,snd,wait=1):
        ## Find a free channel and play a sound on it
        if snd not in mmap:
            mmap[snd]=mixer.Sound(smap[snd])
        ch=mixer.find_channel()
        ch.play(mmap[snd])
        if wait != 0:
            self.wait_on_channel(ch)
            ch.stop()
            
    def play_on_chan(self,chan,snd, loops=0):
    ##  Play a sound on a specific named channel
        if snd not in mmap:
            mmap[snd]=mixer.Sound(smap[snd])
        chan.play(mmap[snd],loops)


    def walk(self):
        global currentscape
        if currentscape.foot != None:
            ch=mixer.find_channel()
            if ch != None:
                self.play_sound(currentscape.foot,0)

    def end_game(self):
        mixer.stop()
        self.play_sound('FORTH',1)
        self.play_sound('INVENT',0)
        atmosses=[]
        if bag != []:
            for j in bag:
                if j.atmos != None:
                    if j.atmos not in atmosses:
                        atmosses.append(j.atmos)
                        self.play_sound(j.atmos,0)
                else:
                    self.play_sound(j.sound,0)
        while mixer.get_busy():
            pass
        self.play_sound('FITH',1)    
        self.tidy_up()
        sys.exit(0)

    def testx(self):
        # Thus just reads keystrokes and prints out the associated command until the QUIT command is given.
        # It is just here for us to test that the above stuff works.
        a=Emgame()
        cm = Command.UNKNOWN
        while cm != Command.QUIT :
            cm=self.get_command()
            # print ('Next','\r')
            # print(cm.name,'\r')
          
