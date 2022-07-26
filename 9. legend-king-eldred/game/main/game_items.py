# The Legend of King Eldred
# Code Angel
# Items module


# Get a dictionary of all the game items
def get_items():

    all_items = {
        'bottle': {
            'name': 'bottle',
            'room': '01',
            'description': 'glass bottle',
            'examine': 'It is a solid glass bottle. \
\nThe label has faded but you can just make out that it once hailed from the renowned John Connell distillery \
located to the south of Wildemoor.\
\nThe bottle appears to have something inside.',
            'inv': True
        },

        'hammer': {
            'name': 'hammer',
            'room': '00',
            'description': 'rusty hammer',
            'examine': 'It is an old hammer from a toolbox.',
            'inv': True
        },

        'toy': {
            'name': 'toy',
            'room': '00',
            'description': "child's toy",
            'examine': '5 tiny metal balls and a brass spinner. But no instructions.',
            'inv': True
        },

        'egg': {
            'name': 'egg',
            'room': '00',
            'description': 'egg',
            'examine': 'A freshly laid egg.',
            'inv': True
        },

        'bucket': {
            'name': 'bucket',
            'room': '03',
            'description': 'empty battered bucket',
            'examine': "An old bucket with a handle. It's quite battered but there are no holes in it.",
            'inv': True,
            'status': 'empty'
        },

        'nail': {
            'name': 'nail',
            'room': '00',
            'description': 'rusty nail',
            'examine': "It's an old rusty nail. It's about 8 cm long.",
            'inv': True
        },

        'spoon': {
            'name': 'spoon',
            'room': '00',
            'description': 'large serving spoon',
            'examine': 'It looks like Adelmo uses this spoon to serve up food to his guests.',
            'inv': True
        },

        'torch': {
            'name': 'torch',
            'room': '08',
            'description': 'lit torch',
            'examine': 'Basically a stick with fire at one end. It could probably set something alight.',
            'inv': True
        },

        'oil can': {
            'name': 'oil can',
            'room': '00',
            'description': 'sealed oil can',
            'examine': "It is an oil can which has been sealed so the oil won't spill out.",
            'inv': True,
            'status': 'sealed'
        },

        'bone': {
            'name': 'bone',
            'room': '00',
            'description': 'bone',
            'examine': 'It is a long bone. Is it human? Maybe. It looks like a femur.',
            'inv': True
        },

        'floor plan': {
            'name': 'floor plan',
            'room': '00',
            'description': 'floor plan',
            'examine': "These are the detailed floor plans for a King Eldred's tomb.\
\nIn the bottom right hand corner, in small print, you see that the architect was Liam Cookson.\
\nOn the back of the plan someone has written '3=sun, 1=moon, 2=1'.",
            'inv': True
        },

        'crown': {
            'name': 'crown',
            'room': '00',
            'description': 'golden crown of anquira',
            'examine': 'A golden crown studded with emeralds and diamonds.',
            'inv': True
        },

        'barrel': {
            'name': 'barrel',
            'room': '07',
            'description': 'wooden barrel',
            'examine': "Looking into the barrel you see some tiny metal balls and a brass spinner. \
It's some sort of child's toy.",
            'secret item': 'toy',
            'discovered': False,
            'inv': False
        },

        'hen': {
            'name': 'hen',
            'room': '32',
            'description': 'hen',
            'examine': 'The hen seems startled by your interested and hops off the straw revealing an egg. ',
            'secret item': 'egg',
            'discovered': False,
            'inv': False
        },

        'desk': {
            'name': 'desk',
            'room': '14',
            'description': 'prison guard desk',
            'examine': 'It is an old wooden desk.\
\nYou can make out the name Peter Gibson carved along one side although its not clear if Mr Gibson was a guard or \
a convict.\
\nYou open the drawer in the desk and discover a sealed can of oil.',
            'secret item': 'oil can',
            'discovered': False,
            'inv': False
        },

        'toolbox': {
            'name': 'toolbox',
            'room': '06',
            'description': 'old toolbox',
            'examine': 'This toolbox has seen better days. The only thing in it is a rusty hammer.',
            'secret item': 'hammer',
            'discovered': False,
            'inv': False
        },

        'table': {
            'name': 'table',
            'room': '10',
            'description': 'kitchen table',
            'examine': "Adelmo's kitchen table. The unusual tablecloth matches the unusual wallpaper. \
There is a large greasy spoon in the middle of the table. It doesn't look like Adelmo does much washing up.",
            'secret item': 'spoon',
            'discovered': False,
            'inv': False
        },

        'wood block': {
            'name': 'wood block',
            'room': '09',
            'description': 'wood block',
            'examine': 'The wood block has some nails hammered into it. One falls to the floor.',
            'secret item': 'nail',
            'discovered': False,
            'inv': False
        },

        'picture': {
            'name': 'picture',
            'room': '08',
            'description': 'home sweet home picture',
            'examine': 'This is the kind of picture that people hide their keys behind. \
\nIt is by the well-known artist Chris January but you are not really a fan of his work.\
\nA small black iron key falls to the floor.',
            'secret item': 'key 5',
            'discovered': False,
            'inv': False
        },

        'wastebasket': {
            'name': 'wastebasket',
            'room': '11',
            'description': 'wicker wastebasket',
            'examine': 'After rooting around the bin for a couple of minutes you find a silver key \
below the mound of waste paper, a bank statement in the name of Wayne Richardson, and 2 old apple cores.',
            'secret item': 'key 6',
            'discovered': False,
            'inv': False
        },

        'lake': {
            'name': 'lake',
            'room': '19',
            'description': 'lake',
            'examine': 'There water is still and the moon casts a stunning reflection over the lake. \
The water looks good enough to drink. \
\nYou notice something floating on the surface.',
            'secret item': 'wood',
            'discovered': False,
            'inv': False
        },

        'coffin': {
            'name': 'coffin',
            'room': '29',
            'description': 'marble coffin',
            'examine': "A plaque on top of the coffin reads: 'In memorium, our beloved Queen Naga, \
Queen of all Wildemoor.' \
\nAs you lean over to read the inscription you accidentally dislodge the coffin lid and it falls to the floor \
shattering with an almighty crash. \
\nYou are just about to make a run for it when you notice something odd about the \
skeleton lying inside the coffin.\
\nThere is an extra femur bone propped up in the corner of the coffin. \
\nAs there are already two smaller femur bones which form part of the main skeleton, \
you conclude that this larger bone has to belong to someone else.",
            'secret item': 'bone',
            'discovered': False,
            'inv': False
        },

        'carcass': {
            'name': 'carcass',
            'room': '03',
            'description': 'pig carcass',
            'examine': "It's a carcass of a pig. Enough to turn you vegetarian.",
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'ice block': {
            'name': 'ice block',
            'room': '06',
            'description': 'a very large ice block',
            'examine': 'The block of ice is cold. Very cold. How cold...? You try licking it. \
Three minutes elapse before you are able to separate your tongue from the ice.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'kitchen sink': {
            'name': 'sink',
            'room': '10',
            'description': 'the kitchen sink',
            'examine': 'Some dirty dishes piled up in some dirty dishwater. \
A few dead flies float on the surface.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'toilet': {
            'name': 'toilet',
            'room': '10',
            'description': 'toilet',
            'examine': 'Who has their toilet in the kitchen. The Wildemoor health and safety laws seem pretty relaxed.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'ornament': {
            'name': 'ornament',
            'room': '08',
            'description': 'ornament',
            'examine': "It depicts a king on a throne. The inscription underneath reads 'We worship King Eldred,\
the first born son of King Asrani and Queen Delicia Fernandes'.",
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'portrait': {
            'name': 'portrait',
            'room': '11',
            'description': 'portrait',
            'examine': "The portrait shows someone who looks very important. \
The plaque reads: 'Sir Michael Patrick Reyes Flores, Chairman of The Bank of Wildemoor'",
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'bed': {
            'name': 'bed',
            'room': '15',
            'description': 'prison bed',
            'examine': 'Given the colour and smell of the bedding, you decide against taking a quick nap.',
            'secret item': 'none',
            'discovered': False,
            'inv': False},

        'dirt': {
            'name': 'dirt',
            'room': '16',
            'description': 'mound of dirt',
            'examine': 'It is a mound of soft dirt, as if someone has been digging it quite recently.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'straw': {
            'name': 'straw',
            'room': '17',
            'description': 'bed of straw',
            'examine': 'The straw is very dry. It looks highly flammable.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'dog': {
            'name': 'dog',
            'room': '20',
            'description': 'large black dog',
            'examine': "You observe the dog from a safe distance. It is the size of a small horse. It has what \
only be described as fangs jutting from its mouth. The large tag around the dog's neck reads 'Niu' which you take \
to be the beast's name. \
\nAs you look at the dog it raises its head and delivers a low growl in your direction. It looks hungry.",
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'fountain': {
            'name': 'fountain',
            'room': '25',
            'description': 'fountain',
            'examine': 'The fountain is made of marble and in the centre is a golden bust of a king. \
The water spurts out of his mouth into a pool below.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'tombstone': {
            'name': 'tombstone',
            'room': '26',
            'description': 'old tombstone',
            'examine': "It reads: 'Bill Blake - was hanged by mistake.'",
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'horse': {
            'name': 'horse',
            'room': '28',
            'description': 'horse',
            'examine': 'It is a grey horse about 16 hands in size. It looks as though it might be thirsty.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'gold lever': {
            'name': 'gold lever',
            'room': '22',
            'description': 'gold lever',
            'examine': 'It is a gold lever with a wooden handle. \
You wonder what will happen if you pull it.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'silver lever': {
            'name': 'silver lever',
            'room': '22',
            'description': 'silver lever',
            'examine': 'It is a silver lever with a wooden handle. \
You wonder what will happen if you pull it.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'marble lever': {
            'name': 'marble lever',
            'room': '23',
            'description': 'marble lever',
            'examine': 'It is a lever made from marble. At the foot you can see the cogs which look to \
be quite badly rusted.',
            'secret item': 'none',
            'discovered': False,
            'inv': False,
            'status': 'rusted'
        },

        'copper dial': {
            'name': 'copper dial',
            'room': '23',
            'description': 'copper dial',
            'examine': 'It is a copper dial. There are 3 settings: sun, crescent moon and star. \
The dial is currently set to: ',
            'secret item': 'none',
            'discovered': False,
            'inv': False,
            'status': 'star',
            'display status': True
        },

        'bronze dial': {
            'name': 'bronze dial',
            'room': '23',
            'description': 'bronze dial',
            'examine': 'It is a bronze dial. There are 3 settings: sun, crescent moon and star. \
The dial is currently set to: ',
            'secret item': 'none',
            'discovered': False,
            'inv': False,
            'status': 'sun',
            'display status': True
        },

        'silver dial': {
            'name': 'silver dial',
            'room': '23',
            'description': 'silver dial',
            'examine': 'It is a silver dial. There are 3 settings: sun, crescent moon and star. \
The dial is currently set to: ',
            'secret item': 'none',
            'discovered': False,
            'inv': False,
            'status': 'moon',
            'display status': True},

        'guard': {
            'name': 'guard',
            'room': '21',
            'description': 'guard',
            'examine': 'The man guarding the door towers above you. He must be at least 8 feet tall, and he \
clearly works out regularly. \
\nHe has a scimitar tucked into his belt and his giant-sized hands are weapons in their own right. \
\nThis goliath of a man has a tattoo on his left forearm bearing the name Marie K, whilst a tattoo on his right \
forearm shows two crescent moons and a sun.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'butcher': {
            'name': 'butcher',
            'room': '03',
            'description': 'butcher',
            'examine': 'The butcher is wearing a set of white overalls, and a white apron. \
Both are stained with blood. He appears to only have 3 fingers on his right hand.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'baker': {
            'name': 'baker',
            'room': '31',
            'description': 'baker',
            'examine': 'The baker is a well built man, probably around 50 years of age. \
\nIt is not clear if his hair is naturally grey, or whether it is because he is covered in flour.\
\nHis name tag suggests that his name is Laurence Perales Guerrero.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'banker': {
            'name': 'banker',
            'room': '11',
            'description': 'banker',
            'examine': 'The banker looks down at you over the spectacles balanced at the end of her nose.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'andrid': {
            'name': 'andrid',
            'room': '30',
            'description': 'andrid',
            'examine': 'A young girl, possibly 7 or 8 years old.',
            'secret item': 'none',
            'discovered': False,
            'inv': False
        },

        'leather': {
            'name': 'leather',
            'room': '12',
            'description': 'patch of leather',
            'examine': "The patch of leather has the letter 'g' scratched onto it.",
            'inv': True
        },

        'slate': {
            'name': 'slate',
            'room': '05',
            'description': 'broken slate',
            'examine': "The slate has the letter 'k' written on it.",
            'inv': True
        },

        'rock': {
            'name': 'rock',
            'room': '00',
            'description': 'carved rock',
            'examine': "It is a rock. The letter 'n' has been carved into it.",
            'inv': True
        },

        'wood': {'name': 'wood',
                 'room': '00',
                 'description': 'carved block of wood',
                 'examine': "It is an ornate piece of wood that has the letter 'i' carved into it.",
                 'inv': True
                 },

        'parchment': {
            'name': 'parchment',
            'room': '00',
            'description': 'old parchment',
            'examine': "It is a large piece of parchment with writing on it. You read it: \
\nTHE DAILY WILDEMOOR \nWildemoor Mourns King Eldred\
\nYou begin to read the article, but your eye catches a second story nearer the bottom of the page:\
\nBlackmore Stables Robbed Again\
\nMajor Major, a white stallion was taken from his stables at the dead of night on Friday past. Stable owners, \
The Blackmore brothers Taylor, Marcus, Hunter, Seth, Griffin and Lars have released a statement:\
\nWe are devastated to lose another of our horses to rustlers. Major Major was like one of the family.\
\nWe ask all of Wildemoor to be vigilant and let us know if they see a white stallion anywhere in the town.\
\nYou turn the parchment over and notice that someone has scribbled something in ink. \
\nIt appears to be the numbers 2 4 0 5.",
            'inv': True},

        'key 1': {
            'name': 'key',
            'room': '00',
            'description': 'golden key',
            'examine': 'It looks like the key to a door.',
            'inv': True
        },

        'key 2': {
            'name': 'key',
            'room': '10',
            'description': 'rusty iron key',
            'examine': 'This is a rusted old iron key. Looks like it should still work.',
            'inv': True
        },

        'key 3': {
            'name': 'key',
            'room': '02',
            'description': 'bronze key',
            'examine': 'It is a bronze key. The kind that might unlock an outhouse door.',
            'inv': True
        },

        'key 4': {
            'name': 'key',
            'room': '09',
            'description': 'steel key',
            'examine': 'It is a steel key. The letters K-N-A-B are etched around the outside.',
            'inv': True
        },

        'key 5': {
            'name': 'key',
            'room': '00',
            'description': 'black iron key',
            'examine': 'A black iron key - the kind a prison guard might have.',
            'inv': True
        },

        'key 6': {
            'name': 'key',
            'room': '00',
            'description': 'silver key',
            'examine': 'A small but beautifully crafted silver key.',
            'inv': True
        },

        'key 7': {
            'name': 'key',
            'room': '00',
            'description': 'bone key',
            'examine': 'The key has been made from bone. It looks like it is the key to a chest.',
            'inv': True
        },

    }

    return all_items
