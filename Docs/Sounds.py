import sys
from pygame import *
import Soundscape as ss


SFShort=[
    # Short names for all the sound files available.
    'BLACK',
    'CANCEL',
    'CLICK',
    'CONTINUE',
    'CREDITS',
    'DOORCLOSE',
    'DOOROPEN',
    'FIRST',
    'JINGLE',
    'INVENT',
    'MENU',
    'MILKY',
    'NO',
    'OPENANDCLOSE',
    'OPENJAR',
    'PLANET',
    'REMOVE',
    'ROCKET',
    'SHOOTINGSTAR',
    'SPACESHIP',
    'START',
    'YES']
    

SFNames = ['blackwholelandscape1.mp3',
            'Cancelvoiceover.mp3',
            'clickingmenuoption.mp3',
            'continuegamevoiceover.mp3',
            'creditsvoiceover.mp3',
            'doorclose.mp3',
            'dooropen.mp3',
            'firstscene.mp3',
            'gamejingle.mp3',
            'inventorysoundscape.mp3',
            'menusoundscape.mp3',
            'milkywaysoundscape1.mp3',
            'novoiceover.mp3',
            'openandcloseinventory.wav',
            'openjar.mp3',           
            'planetsoundscape1.mp3',
            'removejar.mp3',
            'rocketsoundscape1.wav',           
            'shootingstarsoundscape1.wav',          
            'spaceshipsoundscape1.wav',          
            'startgamevoiceover.mp3',            
            'yesvoiceover.mp3']
# Create a dictionary from all the short names to
# the full filenames of the sounds we want to use



# Initialisation code
mixer.init(channels=2)
bg_music=mixer.Channel(1)
smap={}
mmap={}
prog=sys.argv[0]
for i in range(len(SFShort)):
    smap[SFShort[i]]=prog+"/Sounds/"+SFNames[i]
    mmap[SFShort[i]]=mixer.Sound(prog+"/Sounds/"+SFNames[i])


"""       Set up Soundscapes      """
spacescape=ss.SoundMap("Space",
                       entry_sound=mmap['DOOROPEN'],
                       exit_sound=None,
                       background_sound=mmap['MILKY'],
                       sounds=[ss.Sound("Mars",mmap['PLANET'],90,90),
                               ss.Sound("Apollo",mmap['ROCKET'],-60,-70)
                               ],
                       size=200,
                       entry=(0,0),
                       nextscape=None)

cabinscape=ss.SoundMap("Cabin")

outsidescape=ss.SoundMap("Outside")

riverscape=ss.SoundMap("River")

harbourscape=ss.SoundMap("Harbour")

boat1=ss.SoundMap("Boat1")
boat2=ss.SoundMap("Boat2")
boat3=ss.SoundMap("Boat3")


spacescape.nextscape=cabinscape
cabinscape.nextscape=outsidescape
outsidescape.nextscape=riverscape
riverscape.nextscape=harbourscape
    
startscape=spacescape
nextscape=startscape
currentscape=startscape
#print(smap)
 
