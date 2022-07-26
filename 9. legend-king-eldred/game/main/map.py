# The Legend of King Eldred
# Code Angel
# Map module


# Return a 2D list of the town map
# Each location is a room number or not a room ('--')
def get_town_map():

    town_map = [
        ['15', '--', '01', '--', '09', '30', '31'],
        ['14', '--', '02', '03', '06', '--', '32'],
        ['13', '12', '04', '--', '07', '11', '--'],
        ['16', '--', '05', '--', '08', '--', '29'],
        ['17', '--', '--', '--', '10', '25', '26'],
        ['18', '--', '22', '--', '--', '--', '27'],
        ['19', '20', '21', '23', '24', '--', '28'],
                ]

    return town_map


# Get a dictionary of room descriptions
def get_room_descriptions():

    room_descriptions = {
        '01': "You are standing on a wooden drawbridge. To the south lies the village of Wildemoor.\
\nThere's only one way you can go from here.",

        '02': "You are in the Wildemoor town square. The townsfolk are going about their daily business. \
\nA butcher's shop lies to the east. To the south you can see a set of stairs leading underground. \
\nThere is a drawbridge to the north.",

        '03': "You enter the butcher's shop. All around are carcasses of what you hope are just pigs and sheep. \
\nThe butcher is standing behind the counter. Behind him you see a doorway to the east. \
\nGoing west will take you back to the town square.",

        '04': 'You are standing at the foot of a set of stone spiral stairs. \
\nTo the west you can just make out a gloomy alcove. To the south is a large wooden door. The town square is north.',

        '05': 'You are in a small dungeon cell. There is a chest in the far corner of the room. \
\nTo the north is a large wooden door which is now open.',

        '06': "You are standing in the cold meat store of the butcher's shop. \
\nA large box marked 'Tools' sits in one corner. \
\nThe shop is to the west. To the south a doorway leads into a side street. \
\nThere an outhouse to the north. It has a solid oak door.",

        '07': "You emerge into the sunlit cobbled street.\
\nThere is a ramshackle house to the south. A wooden barrel is propped up agains the wall of the house.\
\nYou can see The Bank of Wildemoor is to the east.\
\nHeading north will take you back into the butcher shop's cold meat store.",

        '08': "You are in Iwa's house. A picture on the wall reads 'Home Sweet Home'. \
You wonder if this is meant to be ironic. There are exits to the north and south.",

        '09': "You enter the outhouse.\
\nJudging by the blood on the walls and floor, and the numerous sharp looking tools scattered about, \
the outhouse must belong to the butcher. \
\nAt least that's what you are telling yourself! \
\nA wood block rests against one of the walls. \
\nThe cold store is to the south and a doorway opens out into an alley to the east. \
\nSomething tells you it's best not to hang around.",

        '10': "You are standing in the kitchen of Adelmo's house. \
\nYou can't help thinking the decor is not what you would have chosen. \
\nBut then you remember you are an intrepid explorer and not an interior designer. \
\nThere are exits to the north and east.",

        '11': "You are in the Bank of Wildemoor. \
\nThere is po-faced banker sitting behind a desk at the far end of the room. \
\nHer desk is uncluttered, with just some papers and a wooden name plate which reads 'Sian Lloyd-Wiggins, Manager'\
\nTo her right lies a wooden chest and to her left a sign is suspended on a pole. \
\nA wicker wastebasket sits underneath a very large portrait.\
\nThe only exit is west, back to the side street.",

        '12': 'You find yourself in a gloomily lit alcove.\
\nIt is difficult to make out anything in the darkness, but as you feel your way along the walls you come across \
a solid wooden door leading west. \
\nTo the east are some spiral stairs.',

        '13': 'You are in a long winding tunnel which has been bored into the earth. There appears to be some \
kind of message written on the wall. \
\nThere are exits to the north, south and east.',

        '14': 'You are in the prison guard room. Other than a desk and chair, there is nothing of note in the room. \
\nTo the north you can see the bars of a prison cell. The tunnel is to the south.',

        '15': "You enter the prison cell. It smells like the previous occupant may have died in here. \
\nSomething has been scrawled on the wall but it makes little sense to you. \
\nJust want gold, don't want to die, been stitched up by the complacent hat guy. \
\nThere is a small bed and hidden underneath it a small chest. The only way out is south.",

        '16': 'You are in a narrow tunnel, and the only way through is to go on your hands and knees. \
\nBeneath you is a mound of dirt.\nThere is a glimmer of light coming from the exits north and south.',

        '17': 'You continue along the dark tunnel. You feel water at your feet. At first you think that the gentle \
hissing sound you are hearing is trickling water. \nAnd then you realise that ahead of you is a nest of vipers. \
\nThe vipers have made their nest on what seems to be a large bed of straw. \
\nThere are tunnels running to the north and the south.',

        '18': 'It seems like an endless tunnel. Without your torch it is virtually impossible to see anything. \
The stench of burned flesh still hangs in the air.\
\nThere is bright light coming from the exit to the south. North takes you back along the tunnel. ',

        '19': 'You are standing in a cave. Shards of moonlight are bursting in from a large gap in the cave roof but \
the cave walls are sheer and there is no way you could climb up. \
\nIn the middle of the cave is a lake. You can see the moon and a couple of stars reflecting off the surface of \
the water. \
\nA dark tunnel lies to the north. There is small gap in the cave wall to the east',

        '20': 'You find yourself on a rocky path. To the east are a set of marble steps which lead up to an old \
oak door. The door is open.\
\nA large black dog is lying at the top of the steps in front of the open door. \
There is a small gap leading to a cave in the west.',

        '21': 'You enter a large room, notable for its lack of features and furniture. The floors, walls and \
ceiling are all fashioned from marble.\
\nThere is a silver door leading to the east. A guard stands menacingly in front of the door.\
\nThere are exits to the west and north.',

        '22': 'You find yourself in a room which is completely empty except for two levers and a chest. \
\nThere is an exit to the south.',

        '23': 'You have entered the tomb of King Eldred. Marble pillars rise up to the celing from each corner \
of a marble sarcophagus.\
\nOn one wall you can see three dials. The first dial is made of copper, the second bronze and the third dial is made \
of silver.\
\nEach dial has three different settings: sun, crescent moon and star.\
\nBehind the sarcophogus to the east there is a solid marble door. The floor between the sarcophogus and the door has \
been completely removed leaving a pit in its place. \
\nThere are lethal looking spikes rising up from the bottom of the pit.\
\nThere is no way to reach the door without falling into the pit first.\
\nA marble lever sits to the right of the sarcophogus.',

        '24': 'You are in a meadow. The sun is warm and there is a stream running past your feet.\
\nYou bend to drink, the water is cool and clear. You hear birds in the trees, \
their song carried by the gentle breeze.',

        '25': "You are in a small garden. The grass is overgrown and the flowerbeds overrun with weeds. \
There is a fountain here. \
\nWest will take you back to Adelmo's house and you can see what appears to be a graveyard to the east",

        '26': "You are standing in the town's graveyard.  There is a mausoleum to the north with a heavy iron door. \
\nA paddock runs to the south of the graveyard and Adelmo's garden is east.",

        '27': 'You are in a paddock, and from the hoof marks on the ground you can see it is used to exercise horses. \
The area is covered in a combination of short grass and dry dirt. \
\nTo the south you can see a gate which has a sign attached to it. The gate has been left open. \
The graveyard is north of here.',

        '28': 'You have arrived at some stables. A grey horse is tethered to a wooden post. The only exit is north.',

        '29': "You are inside a dark mausoleum. The builiding is made entirely from stone and there is a single \
tiny window which lets in only a feint glimmer of light. \
\nThere is a large marble coffin in the centre of the room. Thick spider webs hang everywhere. It is \
very cold in here. \
\nA wooden chest has been placed at the foot of the coffin. ",

        '30': 'You enter an alleyway. A young girl is sitting on the ground. She appears to have been crying.\
\nThere is a bakery to the east and an outhouse lies to the west.',

        '31': "You are in the bakery. The baker stands behind the counter. \
\nThe strong aroma of freshly baked bread is making you feel quite hungry. \
\nHeading west will take you back out to the alleyway. The sign above the doorway to the south reads 'Mill'",

        '32': 'You are standing in the mill. Sacks of flour are stacked up against the far wall beside a chest.\
\nA large mill stone is turning slowly in the centre of the room.\
\nA hen is sitting on a bed of straw underneath the only window.',
    }

    return room_descriptions


# Get a dictionary of room doors
def get_doors():
    doors = {
        'door 1': {
            'room': '04',
            'locked': True,
            'unlock key': 'key 2',
            'open': False,
            'examine': 'It is a heavy wooden door with an iron handle.',
            'direction': 's'
        },

        'door 2': {
            'room': '12',
            'locked': True,
            'unlock key': 'key 1',
            'open': False,
            'examine': 'It is a heavy wooden door with a golden lock.',
            'direction': 'w'
        },

        'door 3': {
            'room': '06',
            'locked': True,
            'unlock key': 'key 3',
            'open': False,
            'examine': 'It is a heavy wooden door with a bronze lock.',
            'direction': 'n'
        },

        'door 4': {
            'room': '14',
            'locked': True,
            'unlock key': 'key 5',
            'open': False,
            'examine': 'The cell door is made of thick steel bars.',
            'direction': 'n'
        },

        'door 5': {
            'room': '26',
            'locked': True,
            'unlock key': 'code',
            'unlock code': '2405',
            'open': False,
            'examine': 'The mausoleum door is held shut with a combination lock - you need the code.',
            'direction': 'n'
        },

        'king': {
            'room': '21',
            'locked': True,
            'unlock key': 'guard',
            'unlock code': 'king',
            'open': False,
            'examine': 'The door has been crafted out of pure silver. It glints in the sunlight.',
            'direction': 'e'
        },

        'exit': {
            'room': '23',
            'locked': True,
            'unlock key': 'lever',
            'unlock code': 'dials',
            'open': False,
            'examine': 'Like the rest of the room, the door has been fashioned from marble. There is no lock.',
            'direction': 'e'
        }
    }

    return doors


# Get a dictionary of room chests
def get_chests():
    chests = {
        'chest 1': {
            'room': '05',
            'locked': False,
            'unlock key': 'none',
            'open': False,
            'examine': 'Just a regular chest.',
            'gold': 6
        },

        'chest 2': {
            'room': '11',
            'locked': True,
            'unlock key': 'key 4',
            'open': False,
            'examine': 'It is a large chest. It looks like it might hold a lot of gold pieces.',
            'gold': 23
        },

        'chest 3': {
            'room': '15',
            'locked': True,
            'unlock key': 'key 6',
            'open': False,
            'examine': 'A beautiful silver chest will need a silver key to unlock it.',
            'gold': 51
        },

        'chest 4': {
            'room': '29',
            'locked': False,
            'unlock key': 'none',
            'open': False,
            'examine': 'A chest designed especially for holding gold coins. Someone forgot to lock it.',
            'gold': 14
        },

        'chest 5': {
            'room': '32',
            'locked': True,
            'unlock key': 'key 7',
            'open': False,
            'examine': 'A chest covered in flour. The lock has been decorated in some sort of animal bone.',
            'gold': 31
        },

        'lever room': {
            'room': '22',
            'locked': True,
            'unlock key': 'none',
            'open': False,
            'examine': 'The left side of the chest has been made from gold.\
    The right side of the chest has been made from gold.\
    \nOddly the chest has no keyhole.',

            'gold': 72
        },

        'marble': {
            'room': '00',
            'locked': False,
            'unlock key': 'none',
            'open': False,
            'examine': "It is a beautiful marble chest inscribed with the 'King Eldred' in gold. \
    \nThe chest is not locked.",

            'gold': 173
        }
    }

    return chests


# Get a dictionary of room deadly exits
def get_deadly_exits():
    deadly_exits = {
        'vipers': {
            'room': '17',
            'safe': False,
            'death': "As soon as you get withing 2 metres of the viper nest, they strike. \
\nIt doesn't take long for the venom to take effect and as you close your eyes for the last time you \
are left to wonder what treasures actually lie in King Eldred's tomb.",

            'direction': 's'},

        'dog': {
            'room': '20',
            'safe': False,
            'death': "As you move towards the dog it growls then gets slowly to its feet. \
\nAs you try to edge past, the dog pounces and you become dog food.",

            'direction': 'e'},

        'spikes': {
            'room': '23',
            'safe': False,
            'death': "As you drop into the pit of spikes you wonder how sharp they really are. \
\nPretty sharp it seems!",

            'direction': 'e'},
    }

    return deadly_exits


# Get a dictionary of room signs
def get_signs():
    signs = {
        '13': {'read': 'Water over earth,\
\nYoung over old,\
\nAnd when it comes to making lever choices,\
\nPick silver over gold.',

               'visible': True
               },

        '11': {
            'read': "The sign reads 'Bank of Wildemoor customers please queue here.'",
            'visible': True
        },

        '27': {
            'read': "Welcome to the best stables in the whole of Wildemoor. \
\nHorses available to rent from just 3 gold pieces per day. \
\nEnquire within. \
\nThe Blackmore Brothers.",
            'visible': True
        },

        '23': {
            'read': 'Here lies our beloved King Eldred, who died in battle protecting the people of Wildemoor. \
\nHe is buried with the magical Crown of Anquira which brings untold power and wealth to whomever wears it.\
\nLook closely in the sky at night and you will see a copper moon, a bronze moon, and a silver sun.',
            'visible': False
        },
    }

    return signs


# Get a dictionary of talking room characters
def get_talking():
    talking = {
        '21': {
            'says': "The guard looks at you with his cold eyes and mutters 'Password...?'"
        },

        '03': {
            'says': "The butcher smiles and says 'I have a toolbox in the back, take anything you need."
        },

        '30': {
            'says': "I'm Andrid <sob>. I lost my <sob> favourite toy <sob>. Have you seen <sob> it?"
        },

        '31': {
            'says': "I am supposed to be baking a cake but I am all out of eggs!"
        },

        '32': {
            'says': "Cluckity cluck, cluckity cluck cluck."
        },

        '11': {
            'says': "The banker tuts and says through gritted teeth 'Do you wish to deposit or withdraw?\
\nTo withdraw you will need a key. This chest belongs to Mathieu Arnold, the butcher. Did he give you a key?'."
        }
    }

    return talking


# Get a dictionary of roomn hints
def get_hints():
    hints = {
        '04': {
            'hint': 'Adelmo sometimes has a key.',
            'cost': 4
        },

        '11': {
            'hint': 'The butcher keeps a key in his outhouse.',
            'cost': 5
        },

        '12': {
            'hint': 'You need what is in the bottle. Smash it with something.',
            'cost': 3
        },

        '14': {
            'hint': 'Did you know Iwa once worked as a prison guard?',
            'cost': 7
        },

        '16': {
            'hint': 'You need something to dig with. A spoon might just do it.',
            'cost': 5
        },

        '17': {
            'hint': 'If only you had something like a torch to burn the straw...',
            'cost': 10
        },

        '20': {
            'hint': 'Give the dog a bone - you need to visit the mausoleum by the graveyard in the east of \
Wildemoor.',
            'cost': 10
        },

        '21': {
            'hint': 'The guard is looking for a password - have you collected any letters that might make \
up a word?',
            'cost': 2
        },

        '22': {
            'hint': 'Just make sure you pull the correct lever. That is all!',
            'cost': 2
        },

        '23': {
            'hint': "Get the oil can from the guard's room. Pierce it with something sharp found in the butcher's \
outhouse.\
\nThen oil the lever...",
            'cost': 30
        },

        '26': {
            'hint': 'The only way to unlock the mausoleum door is with a code. Maybe the horse might know it?',
            'cost': 6
        },

        '28': {
            'hint': 'The thirsty horse could do with a drink of water - find a bucket and fill it up.',
            'cost': 8
        }
    }

    return hints
