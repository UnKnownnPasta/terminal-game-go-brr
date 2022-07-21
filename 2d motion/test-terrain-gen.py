baseLineMod = [[],[],[],[],[],[],[],[],[],[]]
from copy import deepcopy
from random import randint, randrange
from re import template
from turtle import back

# -----------INITIALIZATION
STORE_DATA, i, n, l = [], 0, 9, 0
switch = 0

# -----------TERRAIN
type1 = ['🟩','🟩','🟩','🟩','🟩']
type2 = ['🟩','🥦','🟦','🟩','🟩']
type3 = ['🟩','🟧','🟧','🟩','🟩']
type4 = ['🟦','🟦','🟦','🟦','🟦']
type5 = ['🥦','🟩','🟦','🟦','🟩']
type5 = ['🟧','🟩','🟩','🟦','🟦']
type6 = ['🟩','🥦','🟦','🟩','🟩']
type7 = ['🟩','🟩','🟩','🟩','🟩']
type10 = ['🟩','🟦','🟩','🥦','🟩']
type8 = ['🟩','🟦','🟦','🥦','🟩']
type9 = ['🟩','🟧','🟧','🟩','🟩']
type11 = ['🟩','🟦','🟩','🟦','🟩']
type12 = ['🥦','🟩','🟦','🟦','🟩']

typeList = [type1]+[type2]+[type6]+[type3]+[type4]+[type5]+[type7]+[type8]+[type9]+[type10]+[type11]+[type12]
# [[x,y,z], [1,2,3], [yes,maybe,no], [yin,neutral,yang]]

# typeList = []
# for x in type1, type2, type3, type4, type5, type6, type7, type8, type9, type10, type11, type12:
#     typeList.insert(len(typeList), x)

while i <= 11:
    for x in '1234567890':#abcdefghijklmnopqrstuvwzyx1234
        randomListFS = randint(0,11)
        baseLineMod[n-1] = typeList[randomListFS]
        if n == 0:
            n, i = 9, i+1
        else:
            n-=1
    dupeList = tuple(baseLineMod)
    STORE_DATA.insert(len(STORE_DATA), list(dupeList))
    # print(''.join(dupeList), end='\n')

BACKUP_DATA = []
for x in STORE_DATA:
    tempList = []
    for y in x:
        tempList = y + tempList
    BACKUP_DATA.insert(len(BACKUP_DATA), tempList)
    tempList = []

STORE_DATA = deepcopy(BACKUP_DATA)

for v in BACKUP_DATA:
    print(''.join(v))

# -----------MISC
# print(len(BACKUP_DATA))

# -----------DUMP
'''
# for x in '123456789012345678901234567890':
#     trialOne = randrange(-1, 6)
#     trialTwo = randrange(-1, 5)
#     if switch == 0:
#         baseLineMod[n-1] = squares[trialOne][trialTwo]
#         switch = 1
#     else:
#         baseLineMod[n-1] = empty[trialOne][trialTwo]
#         switch = 0
    
#     if n == 0:
#         n=30
#         i+=1
#     else:
#         n-=1

#     STORE_DATA.insert(len(STORE_DATA), baseLineMod)
'''
