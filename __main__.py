""" Emmersion Sound Studio main program

A R Jackson - February 2022

"""

# Imports come here
import sys
import argparse
import os
import re


from GameUtils import *  # Most of the code for the game is in here


    
def loop(args):     # Function representing main program
   
    game = Emgame() # Create a game object (defined in GameUtils)
        
    opt=game.show_menu(options) # Play basic game menu
                                # New game, continue game or quit
                               
    #x=game.get_command()        # Get keyboard char or sequence
    while x != pygame.K_q :     # Loop until a 'q' is entered
       # game.do_command(x)      # Interpret command
       #STARTS HERE - NEEDS TO BE CALLED OVER AND OVER WHEN THE GAME IS RUNNING
       #x=game.get_command()    # Get next command
        #STARTS HERE - NEEDS TO BE CALLED OVER AND OVER WHEN THE GAME IS RUNNING
        print("hello from start of main")
        pth= os.path.dirname(os.getcwd())

        f=open(pth+'/LatestVersion/Game/location.txt','r')
        contents=f.readlines()
        print("hello from main")
        print(contents)
        print(contents[0])
        print(contents[1])
        #THE LINE BELOW NEEDS TO GO BACK IN WHEN ITS BEEN CALLED OVER AND OVER
        game.player=(float(contents[0]),float(contents[1]))
        print("done")
        f.close()
        time.sleep(.1)
        #ENDS HERE


    game.tidy_up()
    sys.exit(0)

                 
try:
    loop(sys.argv[1:])          # Run main program and catch any serious errors.
except EOFError:
    print("something badly wrong")
    

