baseLineMod = [[],[],[],[],[],[],[],[],[],[]]
from copy import deepcopy
from random import randint, randrange

# -----------INITIALIZATION
# print('\nMove:', '', end='\n')
STORE_DATA, i, n, l = [], 0, 10, 0
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
print(typeList)
while i <= 10:
    for x in 'abcdefghijklmnopqrstuvwzyx1234':
        randomListFS = randint(0,11)
        baseLineMod[n-1] = ''.join(typeList[randomListFS])
        if n == 0:
            n=10
            i+=1
        else:
            n -= 1
    dupeList = tuple(baseLineMod)
    STORE_DATA.insert(len(STORE_DATA), list(dupeList))
    print(''.join(dupeList), end='\n')

BACKUP_DATA = deepcopy(STORE_DATA)

# -----------MISC

for v in STORE_DATA:
    print("".join(v))




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
