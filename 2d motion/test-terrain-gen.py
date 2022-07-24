baseLineMod = [[],[],[],[],[],[],[],[],[],[],[]]
from copy import deepcopy
from random import randint, randrange

# -----------INITIALIZATION
STORE_DATA_DE, STORE_DATA_PL, x, i, j, y = [], [], 8, 0, 9, 0

# -----------TERRAIN
# type1 = ['🟩','🟩','🟩','🟩','🟩']
# type2 = ['🟩','🥦','🟦','🟩','🟩']
# type3 = ['🟩','🟧','🟧','🟩','🟩']
# type4 = ['🟦','🟦','🟦','🟦','🟦']
# type5 = ['🟧','🟩','🟩','🟦','🟦']
# type6 = ['🟩','🥦','🟦','🟩','🟩']
# type7 = ['🟩','🟩','🟩','🟩','🟩']
# type10 = ['🟩','🟦','🟩','🥦','🟩']
# type8 = ['🟩','🟦','🟦','🥦','🟩']
# type9 = ['🟩','🟧','🟧','🟩','🟩']
# type10 = ['🟩','🟦','🟩','🟦','🟩']
# type12 = ['🥦','🟩','🟦','🟦','🟩']

desertList = [['🟨','🟨','🟨','🟨'],['🟨','🌵','🟨','🟨'],['🟨','🟨','🟩','🟨'],['🟨','🟨','🟨','🟨'],['🟨','🟨','🟨','🟩']]#+[type5]+[type7]+[type8]+[type9]+[type10]+[type10]+[type12]
plainsList = [['🟩','🟩','🥦','🟩'],['🟩','🟩','🟦','🟦'],['🟩','🥦','🟩','🟩'],['🟩','🟩','🟩','🟦'],['🟦','🟩','🟦','🟩']]

# ------- D E S E R T
abc = []
while i <= 4:
    for xx in '12345':
        randList = randint(0,4)
        abc.insert(len(abc), desertList[randList])
        x-=1
        if x == 0:
            i+=1
            x=8
    STORE_DATA_DE.insert(len(STORE_DATA_DE), abc)
    abc=[]
x, i = 8, 0

BACKUP_DATA_DE = [] # make a second copy of terrain, this is refined
for l in STORE_DATA_DE:
    tempList = []
    for m in l:
        for n in m:
            tempList.insert(len(tempList), n)
    BACKUP_DATA_DE.insert(len(BACKUP_DATA_DE), tempList)
    tempList = []

# ------- P L A I N S
efg = []
while i <= 4:
    for xx in '12345':
        randList = randint(0,4)
        efg.insert(len(abc), plainsList[randList])
        x-=1
        if x == 0:
            i+=1
            x=8
    STORE_DATA_PL.insert(len(STORE_DATA_PL), efg)
    efg=[]

BACKUP_DATA_PL = [] # make a second copy of terrain, this is refined
for l in STORE_DATA_PL:
    tempList = []
    for m in l:
        for n in m:
            tempList.insert(len(tempList), n)
    BACKUP_DATA_PL.insert(len(BACKUP_DATA_PL), tempList)
    tempList = []


# GET THE BASE RANDOMIZED STATE
# while j <= 10: # line
#     for y in '1234567890': # 10 array joined, 5 elements each, 10*5 = 50 total elements
#         randomListFS = randint(0,4) # random of the preset of 10 arrays
#         baseLineMod[l-1] = plainsList[randomListFS] # put each of 10 array into a array
#         if l == 0: # when 10 arrays are finished sorting
#             l, j = 9, j+1 # reset to 10 array pending, shift line by +1
#         else:
#             l-=1 # register a array as finished entering
#     dupeList = tuple(baseLineMod)
#     STORE_DATA.insert(len(STORE_DATA), list(dupeList)) # insert current chosen array of 10 (x5)

INVENTORY_DATA = ['💓','💓','💓','💓',' ',' ',' ',' ',' ','(','0',')','Inventory:',' ','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳']

tmp = [
    ['(','0',')','Inventory:',' ',' ',' ',' '],
    ['🔳','🔳','🔳','🔳','🔳','🔳',' ','🔳','🔳'],
    ['🔳','🔳','🔳','🔳','🔳','🔳',' ','🔳','🔳'],
    ['🔳','🔳','🔳','🔳','🔳','🔳',' ','🔳','🔳'],
    ['🔳','🔳','🔳','🔳','🔳','🔳',' ','🔳','🔳'],
    ['🔳','🔳','🔳','🔳','🔳','🔳',' ','🔳','🔳'],
    ['🔳','🔳','🔳','🔳','🔳','🔳',' ','🔳','🔳'],
    ['💓','💓','💓','💓',' ',' ',' ',' ',' '],
]

# BACKUP_DATA_DE.append(INVENTORY_DATA)
# BACKUP_DATA_PL.append(INVENTORY_DATA)
STORE_DATA_DE = deepcopy(BACKUP_DATA_DE) # main terrain
STORE_DATA_PL = deepcopy(BACKUP_DATA_PL) # main terrain

# for v in BACKUP_DATA_DE:
#     print(''.join(v))
# for v in BACKUP_DATA_PL:
#     print(''.join(v))
# for v in INVENTORY_DATA:
#     print(''.join(v), end='')

for x in range(0,8): # PLAINS
    print(''.join(BACKUP_DATA_PL[x]), '                      ', ''.join(tmp[x]))
for x in range(0,8): # DESERT
    print(''.join(BACKUP_DATA_DE[x]), '                      ', ''.join(tmp[x]))


# -----------MISC
# print(len(BACKUP_DATA))

# -----------DUMP
