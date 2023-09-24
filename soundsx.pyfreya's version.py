import sys
import os
PYGAME_HIDE_SUPPORT_PROMPT=1
from pygame import *
import Soundscape as ss
from os import path



SF=[
    ('1.56',	'1.56.mp3'),
    ('40',	'40.mp3'),
    ('44',	'44.mp3'),
    ('AHOY',	'ahoy.mp3'),
    ('AIR','air.mp3'),
    ('AIRCON','aircon.wav'),
    ('ATMCABINPIANO','atmcabinpiano.wav'),
    ('ATMPIANO','atmpiano.wav'),
    ('BAYWALK',	'baywalk.wav'),
    ('BIRDS',	'birds.wav'),
    ('BIRDS2',	'birds2.wav'),
    ('BIRDS3',	'birds3.wav'),
    ('BLACK',	'blackwholelandscape1.mp3'),
    ('BLACK2',	'blackwholelandscape2.mp3'),
    ('BOATSTEP','boatstep.wav'),
    ('BUBBLES',	'bubbles.wav'),
    ('BUSK','busk.mp3'),
    ('CABIN',	'cabin.wav'),
    ('CABINDOOR',	'cabindoor.wav'),
    ('CABINWALK',	'cabinwalk.mp3'),
    ('CAFEATMOS','cafeatmos.wav'),
    ('CAFFE',	'caffe.wav'),
    ('CAFFEDOOR',	'caffedoor.mp3'),
    ('CAFFEINSIDE',	'caffeinside.wav'),
    ('CAFFEPIANO',	'caffepiano.mp3'),
    ('CAFFEWALK','caffewalk.mp3'),
    ('CANCEL',	'Cancelvoiceover.wav'),
    ('CAR','car.mp3'),
    ('CAR2','car2.mp3'),
    ('CAROUSEL','carousel.mp3'),
    ('CAVE',	'cave.wav'),
    ('CINIMA','cinima.wav'),
    ('CINIMAATMOS','cinimaatmos.wav'),
    ('CINIMADOOR','cinimadoor.mp3'),
    ('CINVOICE','cinvoice.mp3'),
    ('CLICK2','click2.wav'),
    ('CLICK',	'clickingmenuoption.wav'),
    ('CLOCKTOWER',	'clocktower.wav'),
    ('CLOSIT',	'closit.mp3'),
    ('CONTINUE',	'continuegamevoiceover.wav'),
    ('CRAB',	'crab.wav'),
    ('CREDITS',	'creditsvoiceover.mp3'),
    ('DOORCLOSE',	'doorclose.mp3'),
    ('DOOROPEN',	'dooropen.mp3'),
    ('DOOROPENCABIN','dooropencabin.wav'),
    ('DOOROPENHARBOUR','dooropenharbour.mp3'),
    ('DOOROPENSPACE','dooropenspace.mp3'),
    ('DRINK',	'drink.mp3'),
    ('DROP',	'drop.mp3'),
    ('ELECTROBOAT',	'electroboat.wav'),
    ('ELECTROBOAT2',	'electroboat2.wav'),
    ('FAIR','fair.wav'),
    ('FAIRATMOS','fairatmos.wav'),
    ('FILM','film.wav'),
    ('FAIRWALK','fairwalk.mp3'),
    ('FIRE',	'fire.mp3'),
    ('FIREATMOS','fireatmos.wav'),
    ('FIRST',	'firstscene.mp3'),
    ('FISH',	'fish.wav'),
    ('FITH','fith.mp3'),
    ('FOREST',	'forest.wav'),
    ('FOREST2',	'forest2.wav'),
    ('FOREST3',	'forest3.wav'),
    ('FOREST4',	'forest4.wav'),
    ('FOREST5',	'forest5.wav'),
    ('FOREST6',	'forest6.wav'),
    ('FOREST7',	'forest7.wav'),
    ('FOREST8',	'forest8.wav'),
    ('FORESTATMOS','forestatmos.wav'),
    ('FORTH','forth.wav'),
    ('JINGLE',	'gamejingle.wav'),
    ('GAMES','games.mp3'),
    ('GAMES2','games2.mp3'),
    ('GARDENWALK',	'gardenwalk.mp3'),
    ('GOLD',	'gold.mp3'),
    ('GUITAR',	'guitar.wav'),
    ('GUITAR2',	'guitar2.wav'),
    ('GUITARATMOS','guitaratmos.wav'),
    ('HELLO',	'hello.wav'),
    ('INVENT',	'inventory.mp3'),
    ('KITCHEN',	'kitchen.mp3'),
    ('LEAVETRAIN','leavetrain.mp3'),
    ('LEAVETRAIN2','leavetrain2.wav'),
    ('LIGHTHOUSE',	'lighthouse.wav'),
    ('LIGHTHOUSEATMOS','lighthouseatmos.wav'),
    ('LIGHTHOUSEDOOR',	'lighthousedoor.mp3'),
    ('LIGHTHOUSEINSIDE',	'lighthouseinside.wav'),
    ('LIGHTHOUSEWALK','lighthousewalk.mp3'),
    ('LIGHTS',	'lights.wav'),
    ('MENU',	'menusoundscape.wav'),
    ('MERMAID',	'mermaid.wav'),
    ('MILKY',	'milkywaysoundscape1.mp3'),
    ('NBIRDS','nbirds.mp3'),
    ('NBLACKWHOLE','nblackwhole.mp3'),
    ('NBUBBLES','nbubbles.mp3'),
    ('NCABINRAIN','ncabinrain.mp3'),
    ('NCAFE','ncafe.wav'),
    ('NCAFFE','ncaffe.mp3'),
    ('NCAFEPIANO','ncafepiano.mp3'),
    ('NCAVE','ncave.mp3'),
    ('NCLOCKTOWER','nclocktower.mp3'),
    ('NCRAB','ncrab.mp3'),
    ('NELECTROBOAT','nelectroboat.wav'),
    ('NFAIR','nfair.wav'),
    ('NFILM','nfilm.wav'),
    ('NFILM2','nfilm2.wav'),
    ('NFIRE','nfire.mp3'),
    ('NFISH','nfish.mp3'),
    ('NFOREST','nforest.mp3'),
    ('NGOLD','ngold.mp3'),
    ('NGUITAR','nguitar.wav'),
    ('NLIGHT','nlight.mp3'),
    ('NLIGHTHOUSE','nlighthouse.mp3'),
    ('NLIGHTHOUSEINSIDE','nlighthouseinside.mp3'),
    ('NMERMAID','nmermaid.mp3'),
    ('NMILKY','nmilky.mp3'),
    ('NMOON','nmoon.mp3'),
    ('NOCTOPUS','noctopus.mp3'),
    ('NO',	'novoiceover.mp3'),
    ('NPIANO','npiano.mp3'),
    ('NPLANET','nplanet.mp3'),
    ('NRADIO','nradio.mp3'),
    ('NRAIN','nrain.mp3'),
    ('NRIVER','nriver.mp3'),
    ('NROCKET','nrocket.mp3'),
    ('NROWINGBOAT','nrowingboat.wav'),
    ('NSAILINGBOAT','nsailingboat.wav'),
    ('NSHOOTINGSTAR','nshootingstar.mp3'),
    ('NSINGINGSHIPS','nsingingships.mp3'),
    ('NSPACESHIP','nspaceship.mp3'),
    ('NSTARFISH','nstarfish.mp3'),
    ('NSUB','nsub.mp3'),
    ('NSUN','nsun.mp3'),
    ('NTRAIN','ntrain.mp3'),
    ('NTREASURE','ntreasure.mp3'),
    ('NWINDCHIME','nwindchime.mp3'),
    ('OCTOPUS',	'octopus.wav'),
    ('OPENANDCLOSE',	'openandcloseinventory.wav'),
    ('OPENJAR',	'openjar.mp3'),
    ('PIANO',	'piano.wav'),
    ('PLANET',	'planetsoundscape1.mp3'),
    ('PLANET2',	'Planetsoundscape2.mp3'),
    ('PROJECT','project.wav'),
    ('RADIO',	'radio.wav'),
    ('RADIOATMOS','radioatmos.wav'),
    ('RAIN',	'rain.wav'),
    ('REMOVE',	'removejar.mp3'),
    ('RIDE','ride.mp3'),
    ('RIDE2','ride2.mp3'),
    ('RIDE3','ride3.mp3'),
    ('RIVER',	'river.wav'),
    ('ROCKET',	'rocketsoundscape1.wav'),
    ('ROCKET2',	'rocketsoundscape2.mp3'),
    ('ROWINGBOAT',	'rowingboat.wav'),
    ('ROWINGBOAT2',	'rowingboat2.mp3'),
    ('SAILINGBOAT',	'sailingboat.wav'),
    ('SEA',	'sea.wav'),
    ('SEAATMOS','seaatmos.wav'),
    ('SECOND','second.mp3'), 
    ('SHOOTINGSTAR',	'shootingstarsoundscape1.wav'),
    ('SINGINGSHIP',	'singingship.wav'),
    ('SINGINGSHIP2',	'singingship2.wav'),
    ('SINGINGSHIP3',	'singingship3.wav'),
    ('SPACESHIP',	'spaceshipsoundscape1.wav'),
    ('SPACEWALK','spacewalk.wav'),
    ('SPLASH',	'splash.wav'),
    ('STARFISH',	'starfish.wav'),
    ('START',	'startgamevoiceover.wav'),
    ('SUB',	'sub.wav'),
    ('SUN',	'sun.mp3'),
    ('SWIM','swim.mp3'),
    ('THIRD','third.wav'),
    ('TRAIN','train.wav'),
    ('TRAINATMOS','trainatmos.wav'),
    ('TRAINDOOR','traindoor.mp3'),
    ('TRAINOUTSIDE','trainoutside.wav'),
    ('TRAINVOICE','trainvoice.wav'),
    ('TRAINVOICE2','trainvoice2.wav'),
    ('TREASURE',	'treasure.wav'),
    ('VOCAFE','vocafe.wav'),
    ('VOCIN','vocin.wav'),
    ('VOELECTROBOAT','voelectroboat.wav'),
    ('VOFUN','vofun.wav'),
    ('VOHARBOUR','voharbour.wav'),
    ('VOLIGHTHOUSE','volighthouse.wav'),
    ('VOOUT','voout.wav'),
    ('VORIVER','voriver.wav'),
    ('VOROWINGBOAT','vorowingboat.wav'),
    ('VOSAILINGBOAT','vosailingboat.wav'),
    ('VOTRAIN','votrain.wav'),
    ('WATER',	'water.wav'),
    ('WIND',	'wind.wav'),
    ('WINDCHIME',	'windchime.wav'),
    ('WINDCHIME2',	'windchime2.mp3'),
    ('WINDCHIMEATMOS','windchimeatmos.wav'),
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

#print(len(SF))
for i in range(len(SF)):
    #print(SF[i])
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
                       sounds=[ss.Source("Mars",'PLANET',10,10, namesound='NPLANET'),
                       ss.Source('planet2','PLANET',70,70, namesound='NPLANET'),
                       ss.Source("Apollo",'ROCKET',-50,-50, namesound='NROCKET'),
                       ss.Source("rocket2",'ROCKET2',-10,-14, namesound='NROCKET'),
                       ss.Source("shooting star",'SHOOTINGSTAR',40,-40, namesound='NSHOOTINGSTAR'),
                       ss.Source("sun","SUN",00,00, namesound='NSUN'),
                       ss.Source("blackwhole","BLACK",10,-50, namesound='NBLACKWHOLE'),
                       ss.Source("blackwhole2",'BLACK2',-0,55, namesound='NBLACKWHOLE'),
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
                       ss.Source('cave','CAVE',20,49, namesound='NCAVE'),
                       ss.Source('fish','FISH',19,22, namesound='NFISH'),
                       ss.Source('gold','GOLD',-40,-41, namesound='NGOLD'),
                       ss.Source('lights','LIGHTS',-5,10, namesound='NLIGHT'),
                       ss.Source('sub','SUB',-39,-39, namesound='NSUB'),
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
                       ss.Source('windchime','WINDCHIME',-50,-20, namesound='NWINDCHIME', atm='WINDCHIMEATMOS'),
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
                       ss.Source('piano','PIANO',49,49, namesound='NPIANO', atm='ATMCABINPIANO'),
                       ss.Source('radio','RADIO',-40,-39, namesound='NRADIO',loop=0,atm='RADIOATMOS'),
                       ss.Source('windchime2','WINDCHIME2',0,-49,ex=outsidescape,),
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
                       sounds=[ss.Source('mermaid','MERMAID',-25,25, namesound='NMERMAID'),
                       ss.Source('octopus','OCTOPUS',19,29, namesound='NOCTOPUS'),
                       ss.Source('singingship','SINGINGSHIP',-32,34, namesound='NSINGINGSHIPS'),
                       ss.Source('singingship2','SINGINGSHIP2',45,48, namesound='NSINGINGSHIPS'),
                       ss.Source('singingship3','SINGINGSHIP3',3,5, namesound='NSINGINGSHIPS'),
                            ],
                       size=50,
                       entry=(0,0),
                       nextscape=None)

rowingboatscape=ss.SoundMap('ROWINGBOAT',
                       entry_sound='BOATSTEP',
                       entryvo='VOROWINGBOAT',
                       exit_sound=None,
                       background_sound='ROWINGBOAT',
                       sounds=[ss.Source('mermaid','MERMAID',-25,25, namesound='NMERMAID'),
                       ss.Source('octopus','OCTOPUS',29,19, namesound='NOCTOPUS'),
                       ss.Source('singingship','SINGINGSHIP',-32,34, namesound='NSINGINGSHIPS'),
                       ss.Source('singingship2','SINGINGSHIP2',45,48, namesound='NSINGINGSHIPS'),
                       ss.Source('singingship3','SINGINGSHIP3',3,5, namesound='NSINGINGSHIPS'),
                            ],
                       size=29,
                       entry=(0,0),
                       nextscape=None)

electroboatscape=ss.SoundMap('ELECTROBOAT',
                       entry_sound='BOATSTEP',
                       entryvo='VOELECTROBOAT',
                       exit_sound=None,
                       background_sound='ELECTROBOAT',
                       sounds=[ss.Source('mermaid','MERMAID',-25,25, namesound='NMERMAID'),
                       ss.Source('octopus','OCTOPUS',29,19, namesound='NOCTOPUS'),
                       ss.Source('singingship','SINGINGSHIP',-32,34, namesound='NSINGINGSHIPS'),
                       ss.Source('singingship2','SINGINGSHIP2',45,48, namesound='NSINGINGSHIPS'),
                       ss.Source('singingship3','SINGINGSHIP3',3,5, namesound='NSINGINGSHIPS'),
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
                       ss.Source('caffe','CAFFE',30,30,ex=caffescape, namesound='NCAFFE', atm='cafeatmos'),
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
                       ss.Source('lighthouse','LIGHTHOUSE',21,23,ex=lighthousescape, namesound='NLIGHTHOUSE'),
                       ss.Source('rowingboat2','ROWINGBOAT2',6,57, namesound='NROWINGBOAT',ex=rowingboatscape, atm='SEAATMOS'),
                       ss.Source('sailingboat','SAILINGBOAT',-1,58, namesound='NSAILINGBOAT',ex=sailingboatscape, atm='SEAATMOS'),
                       ss.Source('starfish','STARFISH',-22-22, namesound='NSTARFISH'),
                       ss.Source('trainoutside','TRAINOUTSIDE',0,-20,ex=trainscape, namesound='NTRAIN', atm='TRAINATMOS')],
                       size=61,
                       entry=(0,0,),
                       nextscape=None)

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

trainscape2.tlist.append( ss.Source('leavetrain','LEAVETRAIN',-10,15,ex=harbourscape, atm='TRAINATMOS'))
fairscape.tlist.append(ss.Source('trainoutside','TRAINOUTSIDE',0,-29,ex=trainscape2, atm='TRAINATMOS'))

startscape=spacescape
nextscape=startscape
currentscape=startscape
#print(smap)
