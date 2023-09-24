import sys
import os
PYGAME_HIDE_SUPPORT_PROMPT=1
from pygame import *
import Soundscape as ss
from os import path


# List of sound files and short names for use within the program
SF=[

    ('1.56',	'1.56.mp3'),
    ('40',	'40.mp3'),
    ('44',	'44.mp3'),
    ('AHOY',	'ahoy.mp3'),
    ('AIR','air.mp3'),
    ('AIRCON','aircon.mp3'),
    ('ALREADYCOLLECTED','alreadycollected.mp3'),
    ('ATMCABINPIANO','atmcabinpiano.mp3'),
    ('ATMPIANO','atmpiano.mp3'),
    ('BAYWALK',	'baywalk.mp3'),
    ('BIRDS',	'birds.mp3'),
    ('BIRDS2',	'birds2.mp3'),
    ('BIRDS3',	'birds3.mp3'),
    ('BLACK',	'blackwholelandscape1.mp3'),
    ('BLACK2',	'blackwholelandscape2.mp3'),
    ('BOATSTEP','boatstep.mp3'),
    ('BUBBLES',	'bubbles.mp3'),
    ('BUSK','busk.mp3'),
    ('CABIN',	'cabin.mp3'),
    ('CABINDOOR',	'cabindoor.mp3'),
    ('CABINWALK',	'cabinwalk.mp3'),
    ('CAFEATMOS','cafeatmos.mp3'),
    ('CAFFE',	'caffe.mp3'),
    ('CAFFEDOOR',	'caffedoor.mp3'),
    ('CAFFEINSIDE',	'caffeinside.mp3'),
    ('CAFFEPIANO',	'caffepiano.mp3'),
    ('CAFFEWALK','caffewalk.mp3'),
    ('CANCEL',	'Cancelvoiceover.mp3'),
    ('CAR','car.mp3'),
    ('CAR2','car2.mp3'),
    ('CAROUSEL','carousel.mp3'),
    ('CAVE',	'cave.mp3'),
    ('CHIME','chime.mp3'),
    ('CINIMA','cinima.mp3'),
    ('CINIMAATMOS','cinimaatmos.mp3'),
    ('CINIMADOOR','cinimadoor.mp3'),
    ('CINVOICE','cinvoice.mp3'),
    ('CLICK2','click2.mp3'),
    ('CLICK',	'clickingmenuoption.mp3'),
    ('CLOCKTOWER',	'clocktower.mp3'),
    ('CLOSIT',	'closit.mp3'),
    ('CONTINUE',	'continuegamevoiceover.mp3'),
    ('CRAB',	'crab.mp3'),
    ('CREDITS',	'creditsvoiceover.mp3'),
    ('DOORCLOSE',	'doorclose.mp3'),
    ('DOOROPEN',	'dooropen.mp3'),
    ('DOOROPENCABIN','dooropencabin.mp3'),
    ('DOOROPENHARBOUR','dooropenharbour.mp3'),
    ('DOOROPENSPACE','dooropenspace.mp3'),
    ('DRINK',	'drink.mp3'),
    ('DROP',	'drop.mp3'),
    ('ELECTROBOAT',	'electroboat.mp3'),
    ('ELECTROBOAT2',	'electroboat2.mp3'),
    ('FAIR','fair.mp3'),
    ('FAIRATMOS','fairatmos.mp3'),
    ('FILM','film.mp3'),
    ('FAIRWALK','fairwalk.mp3'),
    ('FIRE',	'fire.mp3'),
    ('FIREATMOS','fireatmos.mp3'),
    ('FIRST',	'firstscene.mp3'),
    ('FISH',	'fish.mp3'),
    ('FITH','fith.mp3'),
    ('FOREST',	'forest.mp3'),
    ('FOREST2',	'forest2.mp3'),
    ('FOREST3',	'forest3.mp3'),
    ('FOREST4',	'forest4.mp3'),
    ('FOREST5',	'forest5.mp3'),
    ('FOREST6',	'forest6.mp3'),
    ('FOREST7',	'forest7.mp3'),
    ('FOREST8',	'forest8.mp3'),
    ('FORESTATMOS','forestatmos.mp3'),
    ('FORTH','forth.mp3'),
    ('JINGLE',	'gamejingle.mp3'),
    ('GAMES','games.mp3'),
    ('GAMES2','games2.mp3'),
    ('GARDENWALK',	'gardenwalk.mp3'),
    ('GOLD',	'gold.mp3'),
    ('GUITAR',	'guitar.mp3'),
    ('GUITAR2',	'guitar2.mp3'),
    ('GUITARATMOS','guitaratmos.mp3'),
    ('HELLO',	'hello.mp3'),
    ('INVENT',	'inventory.mp3'),
    ('KITCHEN',	'kitchen.mp3'),
    ('LEAVETRAIN','leavetrain.mp3'),
    ('LEAVETRAIN2','leavetrain2.mp3'),
    ('LIGHTATMOS','lightatmos.mp3'),
    ('LIGHTHOUSE',	'lighthouse.mp3'),
    ('LIGHTHOUSEATMOS','lighthouseatmos.mp3'),
    ('LIGHTHOUSEDOOR',	'lighthousedoor.mp3'),
    ('LIGHTHOUSEINSIDE',	'lighthouseinside.mp3'),
    ('LIGHTHOUSEWALK','lighthousewalk.mp3'),
    ('LIGHTS',	'lights.mp3'),
    ('MENU',	'menusoundscape.mp3'),
    ('MERMAID',	'mermaid.mp3'),
    ('MILKY',	'milkywaysoundscape1.mp3'),
    ('NBIRDS','nbirds.mp3'),
    ('NBLACKWHOLE','nblackwhole.mp3'),
    ('NBUBBLES','nbubbles.mp3'),
    ('NCABINRAIN','ncabinrain.mp3'),
    ('NCAFE','ncafe.mp3'),
    ('NCAFFE','ncaffe.mp3'),
    ('NCAFEPIANO','ncafepiano.mp3'),
    ('NCAVE','ncave.mp3'),
    ('NCLOCKTOWER','nclocktower.mp3'),
    ('NCRAB','ncrab.mp3'),
    ('NELECTROBOAT','nelectroboat.mp3'),
    ('NFAIR','nfair.mp3'),
    ('NFILM','nfilm.mp3'),
    ('NFILM2','nfilm2.mp3'),
    ('NFIRE','nfire.mp3'),
    ('NFISH','nfish.mp3'),
    ('NFOREST','nforest.mp3'),
    ('NGOLD','ngold.mp3'),
    ('NGUITAR','nguitar.mp3'),
    ('NLIGHT','nlight.mp3'),
    ('NLIGHTHOUSE','nlighthouse.mp3'),
    ('NLIGHTHOUSEINSIDE','nlighthouseinside.mp3'),
    ('NMERMAID','nmermaid.mp3'),
    ('NMILKY','nmilky.mp3'),
    ('NMOON','nmoon.mp3'),
    ('NOCTOPUS','noctopus.mp3'),
    ('NOGAME','nogame.mp3'),
    ('NOTNEAR','notnear.mp3'),
    ('NO',	'novoiceover.mp3'),
    ('NPIANO','npiano.mp3'),
    ('NPLANET','nplanet.mp3'),
    ('NRADIO','nradio.mp3'),
    ('NRAIN','nrain.mp3'),
    ('NRIVER','nriver.mp3'),
    ('NROCKET','nrocket.mp3'),
    ('NROWINGBOAT','nrowingboat.mp3'),
    ('NSAILINGBOAT','nsailingboat.mp3'),
    ('NSHOOTINGSTAR','nshootingstar.mp3'),
    ('NSINGINGSHIPS','nsingingships.mp3'),
    ('NSPACESHIP','nspaceship.mp3'),
    ('NSTARFISH','nstarfish.mp3'),
    ('NSUB','nsub.mp3'),
    ('NSUN','nsun.mp3'),
    ('NTRAIN','ntrain.mp3'),
    ('NTREASURE','ntreasure.mp3'),
    ('NWINDCHIME','nwindchime.mp3'),
    ('OCTOPUS',	'octopus.mp3'),
    ('OPENANDCLOSE',	'openandcloseinventory.mp3'),
    ('OPENJAR',	'openjar.mp3'),
    ('PIANO',	'piano.mp3'),
    ('PLANET',	'planetsoundscape1.mp3'),
    ('PLANET2',	'Planetsoundscape2.mp3'),
    ('PROJECT','project.mp3'),
    ('RADIO',	'radio.mp3'),
    ('RADIOATMOS','radioatmos.mp3'),
    ('RAIN',	'rain.mp3'),
    ('REMOVE',	'removejar.mp3'),
    ('RIDE','ride.mp3'),
    ('RIDE2','ride2.mp3'),
    ('RIDE3','ride3.mp3'),
    ('RIVER',	'river.mp3'),
    ('ROCKET',	'rocketsoundscape1.mp3'),
    ('ROCKET2',	'rocketsoundscape2.mp3'),
    ('ROWINGBOAT',	'rowingboat.mp3'),
    ('ROWINGBOAT2',	'rowingboat2.mp3'),
    ('SAILINGBOAT',	'sailingboat.mp3'),
    ('SEA',	'sea.mp3'),
    ('SEAATMOS','seaatmos.mp3'),
    ('SECOND','second.mp3'), 
    ('SHOOTINGSTAR',	'shootingstarsoundscape1.mp3'),
    ('SINGINGSHIP',	'singingship.mp3'),
    ('SINGINGSHIP2',	'singingship2.mp3'),
    ('SINGINGSHIP3',	'singingship3.mp3'),
    ('SKIP','skip.mp3'),
    ('SPACESHIP',	'spaceshipsoundscape1.mp3'),
    ('SPACEWALK','spacewalk.mp3'),
    ('SPLASH',	'splash.mp3'),
    ('STARFISH',	'starfish.mp3'),
    ('START',	'startgamevoiceover.mp3'),
    ('SUB',	'sub.mp3'),
    ('SUN',	'sun.mp3'),
    ('SWIM','swim.mp3'),
    ('THIRD','third.mp3'),
    ('TRAIN','train.mp3'),
    ('TRAINATMOS','trainatmos.mp3'),
    ('TRAINDOOR','traindoor.mp3'),
    ('TRAINOUTSIDE','trainoutside.mp3'),
    ('TRAINVOICE','trainvoice.mp3'),
    ('TRAINVOICE2','trainvoice2.mp3'),
    ('TREASURE',	'treasure.mp3'),
    ('VOCAFE','vocafe.mp3'),
    ('VOCIN','vocin.mp3'),
    ('VOELECTROBOAT','voelectroboat.mp3'),
    ('VOFUN','vofun.mp3'),
    ('VOHARBOUR','voharbour.mp3'),
    ('VOLIGHTHOUSE','volighthouse.mp3'),
    ('VOOUT','voout.mp3'),
    ('VORIVER','voriver.mp3'),
    ('VOROWINGBOAT','vorowingboat.mp3'),
    ('VOSAILINGBOAT','vosailingboat.mp3'),
    ('VOTRAIN','votrain.mp3'),
    ('WATER',	'water.mp3'),
    ('WIND',	'wind.mp3'),
    ('WINDCHIME',	'windchime.mp3'),
    ('WINDCHIME2',	'windchime2.mp3'),
    ('WINDCHIMEATMOS','windchimeatmos.mp3'),
    ('YAY',	'yay.mp3'),
    ('YES',	'yesvoiceover.mp3')
     ]
    

# Create a dictionary from all the short names to
# the full filenames of the sounds we want to use



# Initialisation code
mixer.pre_init(44100,-16,2,8192, allowedchanges=AUDIO_ALLOW_ANY_CHANGE)
bundle_dir=path.abspath(path.dirname(__file__))
mixer.init()
mixer.set_reserved(3)
bg_music=mixer.Channel(1)
speech=mixer.Channel(2)
smap={}
mmap={}
prog=sys.argv[0]

for i in range(len(SF)):
    short,name=SF[i]
    smap[short]=bundle_dir+"/Sounds/"+name
    #mmap[short]=mixer.Sound(bundle_dir+"/Sounds/"+name)

"""       Set up Soundscapes      """
spacescape=ss.SoundMap("Space",
                       cutscene_sound='FIRST',
                       entry_sound='DOOROPENSPACE',
                       exit_sound=None,
                       background_sound='MILKY',
                       foot='SPACEWALK',
                       sounds=[ss.Source("Mars",'PLANET',-40,-40, namesound='NPLANET'),
                       ss.Source('planet2','PLANET',70,70, namesound='NPLANET'),
                       ss.Source("Apollo",'ROCKET',-50,-50, namesound='NROCKET', atm='GUITARATMOS'),
#                       ss.Source("rocket2",'ROCKET2',-30,30, namesound='NBLACKWHOLE'),
                       ss.Source("shooting star",'SHOOTINGSTAR',40,-40, namesound='NSHOOTINGSTAR'),
                       ss.Source("sun","SUN",00,00, namesound='NSUN'),
                       ss.Source("spaceship","SPACESHIP",00,-70, namesound='NSPACESHIP'),
                            ],
                       size=80,
                       entry=(0,0),
                       nextscape=None) 

riverscape=ss.SoundMap('River',
                       entry_sound='SPLASH',
                       entryvo='VORIVER',
                       exit_sound=None,
                       background_sound='WATER',
                       foot='SWIM',
                       sounds=[ss.Source('bubbles','BUBBLES',-30,30, namesound='NBUBBLES'),
#                       ss.Source('cave','CAVE',20,49, namesound='NCAVE'),
                       ss.Source('fish','FISH',19,22, namesound='NFISH'),
                       ss.Source('lights','LIGHTS',-5,10, namesound='NLIGHT'),
                       ss.Source('sub','SUB',-39,-39, namesound='NGOLD'),
                       ss.Source('treasure','TREASURE',-20,-20, namesound='NTREASURE')],
                       size=41,
                       entry=(0,0),
                       nextscape=None)

outsidescape=ss.SoundMap("Outside",
                       entry_sound='CABINDOOR',
                       entryvo='VOOUT',
                       exit_sound=None,
                       background_sound='RAIN',
                       foot='GARDENWALK',
                       sounds=[ss.Source('birds','BIRDS',40,-40, namesound='NBIRDS', atm='FORESTATMOS'),
                       ss.Source('hello','HELLO',49,40,loop=0),
                       ss.Source('guitar','GUITAR',10,0, namesound='NGUITAR',loop=0, atm='GUITARATMOS'),
                       ss.Source('guitar2','GUITAR2',0,-4, namesound='NGUITAR',loop=0, atm='GUITARATMOS'),
                       ss.Source('river','RIVER',49,49,ex=riverscape, namesound='NRIVER', atm='FORESTATMOS'),
                            ],
                       size=55,
                       entry=(0,0),
                       nextscape=None)

cabinscape=ss.SoundMap("Cabin",
                       cutscene_sound='SECOND',
                       entry_sound='DOOROPENCABIN',
                       exit_sound=None,
                       background_sound='CABIN',
                       foot='CABINWALK',
                       sounds=[ss.Source("fire",'FIRE',-43,-47, namesound='NFIRE',atm='FIREATMOS'),
                       ss.Source('piano','PIANO',40,40, namesound='NPIANO', atm='ATMPIANO'),
                       ss.Source('chime','CHIME',49,-49, loop=0),
                       ss.Source('radio','RADIO',-40,-39, namesound='NRADIO',loop=0,atm='RADIOATMOS'),
                       ss.Source('windchime2','WINDCHIME2',0,-50,ex=outsidescape,),
                            ],
                       size=50,
                       entry=(0,0),
                       nextscape=None)

cinimascape=ss.SoundMap('CINIMA',
                       entry_sound='CINIMADOOR',
                       entryvo='VOCIN',
                       exit_sound=None,
                       background_sound='AIRCON',
                       foot='CABINWALK',
                       sounds=[ss.Source('film','FILM',0,20,loop=0, namesound='NFILM2', atm='CINIMAATMOS'),
                       ss.Source('project','PROJECT',0,-15, namesound='NFILM',loop=0, atm='CINIMAATMOS')],
                       size=20,
                       entry=(0,0),
                       nextscape=None)

fairscape=ss.SoundMap('FAIR',
                       entry_sound='TRAINDOOR',
                       entryvo='VOFUN',
                       exit_sound=None,
                       background_sound='FAIR',
                       foot='FAIRWALK',
                       sounds=[ss.Source('car','CAR',-10,10, namesound='NFAIR',loop=0, atm='FAIRATMOS'),
                       ss.Source('car2','CAR2',15,15,loop=0, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('cinima','CINIMA',-22,15,ex=cinimascape, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('cinvoice','CINVOICE',-25,18,ex=cinimascape, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('games','GAMES',-20,20,loop=2, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('games2','GAMES2',22,22,loop=0, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('ride','RIDE',23,19, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('ride2','RIDE2',-26,33, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('ride3','RIDE3',25,30, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('busk','BUSK',20,30, namesound='NGUITAR', atm='FAIRATMOS'),
                       ss.Source('carousel','CAROUSEL',34,-9,loop=0, namesound='NFAIR', atm='FAIRATMOS'),
                       ss.Source('air','AIR',-25,7,ex=cinimascape, namesound='NFAIR', atm='FAIRATMOS')
                            ],
                       size=50,
                       entry=(0,0),
                       nextscape=None)

trainscape=ss.SoundMap('TRAIN',
                       entry_sound='TRAINDOOR',
                       entryvo='VOTRAIN',
                       exit_sound=None,
                       background_sound='TRAIN',
                       foot='CABINWALK',
                       sounds=[ss.Source('trainvoice','TRAINVOICE',-15,15,loop=0, namesound='NTRAIN', atm='TRAINATMOS'),
                       ss.Source('leavetrain','LEAVETRAIN',-10,15,ex=fairscape, namesound='NTRAIN', atm='TRAINATMOS')],
                       size=16,
                       entry=(0,0),
                       nextscape=None)

trainscape2=ss.SoundMap('TRAIN2',
                       entry_sound='TRAINDOOR',
                       entryvo='VOTRAIN',
                       exit_sound=None,
                       background_sound='TRAIN',
                       foot='CABINWALK',
                       sounds=[ss.Source('trainvoice2','TRAINVOICE2',-15,15,loop=0, namesound='NTRAIN', atm='TRAINATMOS'),
                       ss.Source('leavetrain2','LEAVETRAIN2',14,15)],
                       size=16,
                       entry=(0,0),
                       nextscape=None)

sailingboatscape=ss.SoundMap('SAILINGBOAT',
                       entry_sound='BOATSTEP',
                       entryvo='VOSAILINGBOAT',
                       exit_sound=None,
                       background_sound='SAILINGBOAT',
                       sounds=[ss.Source('octopus','OCTOPUS',19,29, namesound='NOCTOPUS', atm='SEAATMOS'),
                       ss.Source('singingship','SINGINGSHIP',-32,34, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                       ss.Source('singingship2','SINGINGSHIP2',45,48, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                       ss.Source('singingship3','SINGINGSHIP3',3,5, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                            ],
                       size=50,
                       entry=(0,0),
                       nextscape=None)

rowingboatscape=ss.SoundMap('ROWINGBOAT',
                       entry_sound='BOATSTEP',
                       entryvo='VOROWINGBOAT',
                       exit_sound=None,
                       background_sound='ROWINGBOAT',
                       sounds=[ss.Source('octopus','OCTOPUS',29,19, namesound='NOCTOPUS', atm='SEAATMOS'),
                       ss.Source('singingship','SINGINGSHIP',-32,34, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                       ss.Source('singingship2','SINGINGSHIP2',45,48, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                       ss.Source('singingship3','SINGINGSHIP3',3,5, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                            ],
                       size=29,
                       entry=(0,0),
                       nextscape=None)

electroboatscape=ss.SoundMap('ELECTROBOAT',
                       entry_sound='BOATSTEP',
                       entryvo='VOELECTROBOAT',
                       exit_sound=None,
                       background_sound='ELECTROBOAT',
                       sounds=[ss.Source('octopus','OCTOPUS',29,19, namesound='NOCTOPUS', atm='SEAATMOS'),
                       ss.Source('singingship','SINGINGSHIP',-32,34, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                       ss.Source('singingship2','SINGINGSHIP2',45,48, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                       ss.Source('singingship3','SINGINGSHIP3',3,5, namesound='NSINGINGSHIPS', atm='SEAATMOS'),
                            ],
                       size=29,
                       entry=(0,0),
                       nextscape=None)

caffescape=ss.SoundMap('caffe',
                       entry_sound='CAFFEDOOR',
                       entryvo='VOCAFE',
                       exit_sound=None,
                       background_sound='CAFFEINSIDE',
                       foot='CABINWALK',
                       sounds=[ss.Source('caffepiano','CAFFEPIANO',15,15, namesound='NCAFEPIANO', atm='ATMPIANO'),
                       ss.Source('closit','CLOSIT',-24,24, namesound='NCAFE', atm='CAFEATMOS'),
                       ss.Source('drink','DRINK',-16,-16, namesound='NCAFE', atm='CAFEATMOS'),
                       ss.Source('drop','DROP',-5,-9, namesound='NCAFE', atm='CAFEATMOS'),
                       ss.Source('kitchen','KITCHEN',20,20, namesound='NCAFE', atm='CAFEATMOS'),
                       ss.Source('yay','YAY',-17,-23, namesound='NCAFE', atm='CAFEATMOS'),
                            ],
                       size=25,
                       entry=(0,0),
                       nextscape=None)
 
lighthousescape=ss.SoundMap('lighthouse',
                       entry_sound='LIGHTHOUSEDOOR',
                       entryvo='VOLIGHTHOUSE',
                            exit_sound=None,
                       background_sound='LIGHTHOUSEINSIDE',
                       foot='LIGHTHOUSEWALK',
                       sounds=[ss.Source('ahoy','AHOY',20,100,loop=0, namesound='NLIGHTHOUSEINSIDE', atm='LIGHTHOUSEATMOS')],
                       size=100,
                       entry=(0,0),
                       nextscape=None)

harbourscape=ss.SoundMap("Harbour",
                       cutscene_sound='THIRD',
                       entry_sound='DOOROPEN',
                       entryvo='VOHARBOUR',
                       exit_sound=None,
                       background_sound='WIND',
                       foot='BAYWALK',
                       sounds=[ss.Source('birds2','BIRDS2',-40,-40, namesound='NBIRDS', atm='FORESTATMOS'),
                       ss.Source('birds3','BIRDS3',11,11, namesound='NBIRDS', atm='FORESTATMOS'),
                       ss.Source('caffe','CAFFE',30,30,ex=caffescape, namesound='NCAFFE', atm='CAFEATMOS'),
                       ss.Source('clocktower','CLOCKTOWER',22,-29, namesound='NCLOCKTOWER'),
                       ss.Source('crab','CRAB',8,-5, namesound='NCRAB'),
                       ss.Source('electroboat2','ELECTROBOAT2',-10,58, namesound='NELECTROBOAT',ex=electroboatscape, atm='SEAATMOS'),
                       ss.Source('forest','FOREST',-48,-48, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('forest2','FOREST2',-39,-37, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('FOREST3','FOREST3',-44,-37, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('forest4','FOREST4',-31,-36, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('forest5','FOREST5',-1,-1, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('forest6','FOREST6',-4,-4, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('forest7','FOREST7',-15,5, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('forest8','FOREST8',-9,-9, namesound='NFOREST', atm='FORESTATMOS'),
                       ss.Source('lighthouse','LIGHTHOUSE',21,23,ex=lighthousescape, namesound='NLIGHTHOUSE', atm='LIGHTATMOS'),
                       ss.Source('rowingboat2','ROWINGBOAT2',6,57, namesound='NROWINGBOAT',ex=rowingboatscape, atm='SEAATMOS'),
                       ss.Source('sailingboat','SAILINGBOAT',-1,58, namesound='NSAILINGBOAT',ex=sailingboatscape, atm='SEAATMOS'),
#                       ss.Source('starfish','STARFISH',-22-22, namesound='NSTARFISH'),
                       ss.Source('trainoutside','TRAINOUTSIDE',0,-20,ex=trainscape, namesound='NTRAIN', atm='TRAINATMOS')],
                       size=61,
                       entry=(0,0,),
                       nextscape=None)
# Set all values that couldm't be set due to being forward references
boat1=ss.SoundMap("ELECTROBOAT")
boat2=ss.SoundMap("ROWINGBOAT")
boat3=ss.SoundMap("SAILINGBOAT")

spacescape.next=cabinscape
cabinscape.next=harbourscape
outsidescape.next=harbourscape
riverscape.next=harbourscape
harbourscape.next=None
lighthousescape.next=None
electroboatscape.next=None
sailingboatscape.next=None
trainscape.next=None
fairscape.next=None
cinimascape.next=None
rowingboatscape.next=None
trainscape2.next=None
spacescape.prev= None
cabinscape.prev= None
outsidescape.prev= cabinscape
riverscape.prev= outsidescape
lighthousescape.prev= harbourscape
caffescape.prev= harbourscape
trainscape.prev= harbourscape
fairscape.prev= trainscape
cinimascape.prev= fairscape
trainscape2.prev= fairscape
harbourscape.prev= None
electroboatscape.prev= harbourscape
sailingboatscape.prev= harbourscape
rowingboatscape.prev= harbourscape
trainscape2.ex=harbourscape

trainscape2.tlist.append( ss.Source('leavetrain2','LEAVETRAIN2',-10,15,ex=harbourscape, atm='TRAINATMOS'))
fairscape.tlist.append(ss.Source('trainoutside','TRAINOUTSIDE',0,-29,ex=trainscape2, atm='TRAINATMOS'))

startscape=spacescape
nextscape=startscape
currentscape=startscape

