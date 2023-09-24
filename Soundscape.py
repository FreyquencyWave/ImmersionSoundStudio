# Package describing a general system for representingSounds and maps of collections of sounds
# F Shaw and A R Jackson 
from pygame import *
import math as m
soundcoeff=1000   # Factor for inverese square sound calculation
class BoundaryError(Exception):
    """ Error condition to be used if a position is outside the voundary of a soundscape
    pass """

def distance(pos0,pos1):

    # Calculates distance between two points using pythagoras theorem
    # Both parameters are co-ordinate pairs (x,y)
    
    x0,y0=pos0  # Split coorid
    x1,y1=pos1
    x=x1-x0
    y=y1-y0
    return m.sqrt(x*x+y*y)

def pan(pos0, pos1):

    # Calculates the position of an object in the sound sound field relative
    # to the player
    # pos0 - the players position
    # pos1 - the position of the sound object
    # returns a value in the range 0 to 1
    # where 0 is extreme left and 1 is extreme right.
    
    x0,y0=pos0
    x1,y1=pos1
    dist=distance(pos0,pos1)
    if dist==0 :
        return 0.5
    return ((x1-x0)/dist+1)/2

def stereo_vol(player_pos, sound_pos, mapsize=200):
    dist=distance(player_pos,sound_pos)         # Distance from position to object
    pdist= dist/(m.sqrt(4*mapsize*mapsize))     # Distance normalised to 0-1
    vol = 1-pdist                               # Invert distance so volume is lower
                                                # for greater distances
    fact = soundcoeff/((dist+1)*(dist+1))       # ad hoc factor for appropriate
                                                # volume levels
    vol= fact*vol
    if vol >1: vol = 1                          # Limit volume
    # distance as 0..1 where 1 is max distance on map (diagonal)
    pos=pan(player_pos,sound_pos)               # Find position of sound left tp right
    return((1-pos)*vol,pos*vol)                 # Return adjusted volume
    
class SoundMap:
    """
        Class representing a number of objects located in a soundscape

        Attributes
        ----------
        name : String
                A string representing the name of the Sounscape
        tlist : Source []
                List of sound objects in the soundscape              
        cutscene : Sound
                Initial explanation of th esoundscape to be played the first time it is entered
        first_time : Bool
                True if this soundscape has notr been visited previously
        enter: Sound
                Door opening sound
        enter_save : Sound
                Copy of door opening sound
        entervo : Sound
                Voice over to play on entry after door opening
        bg : Sound
                Background sound to play continuously when in soundscape (loop)
        foot : Sound
                Footstreop sound to represent motion in the soundscape
        xmin,ymin,xmax,ymax : real
                The boudaries of the soundscape
        start : (int,int)
                Coordinate representing the point of entry to this soundscape
                Usually (0,0) the centre
        pos : (int,int)
                Coordibnate representing the current position of the player
        next : SoundMap
                Soundmap to move to on a normal exit (leave command)
                of the soundscape
        prev : SoundMap
                The soundscape the player was previously in 
        no_of_trips: int

        Methods
        -------

        in_range(a,b,c) : bool
        
        Checks if a lies between b and c inclusive
        Returns True if it does, otherwise False

        on_map(pos) : bool
        pos : (int, int)
        returns True if pos is within the bounds (inclusive) of the current Soundscape
        False otherwise.

        
    """
    def in_range(self,a,b,c):
        """ Function to check if a number lies between two other values inclusive
            :param a: value to be checked
            :param b: lower bound
            :param c: upper bound
            
            """
        if a>=b and a<=c:
            return True
        else:
            return False
        
    def on_map(self,pos):
        """ Function to check if a specific position is actually on the map.
            :param pos: position to be checked against the current map
            """       
        (x,y)=pos
        if self.in_range(x,self.xmin,self.xmax) and self.in_range(y,self.ymin,self.ymax):
            return True
        else:
            return False
        

    
    
        
    def __init__(self,name, cutscene_sound=None,  entry_sound=None, exit_sound=None, background_sound=None, foot=None, entryvo=None,
                 sounds=[], size=200, entry=(0,0),out_door=None,nextscape=None,prevscape=None):
        """
            :param name: the name of the map
            :param cutscene_sound: pygame.pymixer.Sound object to be played before entry to the map
            :param entry_sound: pygame.pymixer.Sound object to be played on entry to the map
            :param exit_sound: pygame.pymixer.Sound object to be played on leaving the map
            :param background_sound: pygame.pymixer.Sound object to be played continuously
            :param entryvo_sound: pygame.pymixer.Sound object to be played on entry to the map
            :param sounds: list of sound object tobe on the map initially
            :param size: the length of the sides of a square map
                         the coordinates of the sides run from -size/2 to +size/2
            :param entry: the point at which a player enters the map, defaukts to the middle(origin)
            :param out_door: the location of the exit door,
                            deafaults to the middle of the top of the map
            :param nextscape: the next soundscape to go to.
                     ***   This will need generalising ***
                     ***   to allow for multiple exits ***
                     ***   perhaps a list of           ***
                     ***   possible exits              ***
 
            """
        self.name=name
        self.tlist=sounds
        self.cutscene=cutscene_sound
        self.first_time=True
        self.enter=entry_sound
        self.enter_save=entry_sound
        self.entervo=entryvo
        self.bg=background_sound
        self.foot=foot
        self.xmin=self.ymin=-size/2
        self.xmax=self.ymax=size/2
        self.start=entry
        self.pos=entry
        self.next=nextscape
        self.prev=prevscape
        if out_door is None:
            self.od=(0,size/2)
        else:
            self.od=out_door
        (xi,yi)=self.start
        (xo,yo)=self.od
        if not self.on_map(self.start):
            raise BoundaryError(self.start)
        if not self.on_map(self.od):
            raise BoundaryError(self.od)
        self.max_distance=m.sqrt(2*size*size)
        self_no_of_trips=0


class Source:
    """
        Represents a sound object within a Soundscape

        Attributes
        ----------
        name : String
            a descriptive name for the sound (currently unused)
        sound : String
            name used to identify the siund in GaeUtils.poy
        ch: pygame.mixer.Channel
            if the sound is playing, the pygame.mixer channel on which it
            is playing
        x,y : int
            The coordinate position of the sound in the soundscape
        exitscape : SoundMap
            If the exit (e) command can be used to move to another
            soundscpe through this sound it contains a reference to
            that soundscape, otherwise it has the valure None
        loop : int
            0 is the sound is to play oncew when the soudscape starts
            and 1 if is to play continuously
        namesound : String
            a short name for the sound, no longer used
        atmos : String
            the id of a sound which plays along with the main sound
            but is not saved when the sound is collected
            
    """
    def __init__(self, n, sound=None,xpos=0,ypos=0,ex=None,namesound=None, loop=-1, atm=None):
        self.name=n
        self.sound=sound
        self.ch=None
        self.x=xpos
        self.y=ypos
        self.exitscape=ex
        self.loop=loop
        self.namesound=namesound
        self.atmos=atm
        
