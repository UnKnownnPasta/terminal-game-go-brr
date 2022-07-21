baseLineMod = [[],[],[],[],[]]
from copy import deepcopy
from random import randint, randrange

# -----------INITIALIZATION
# print('\nMove:', '', end='\n')
STORE_DATA, i, n, l = [], 0, 6, 0
switch = 0

# -----------TERRAIN
squares = [['🟩','🟩','🟩','🟩','🟩'],['🟩','🟩','🟩','🟩','🟩'],['🟩','🟫','🟫','🟫','🟩'],['🟩','🟩','🟩','🟩','🟩'],['🟩','🟫','🟫','🟫','🟩'],['🟩','🟩','🟩','🟩','🟩']]
empty = [['🟩','🟩','🟩','🟩','🟩'],['🟦','🟦','🟦','🟦','🟦'],['🟩','🟩','🟩','🟩','🟩'],['🟩','🟦','🟦','🟩','🟩'],['🟩','🟩','🟩','🟩','🟩'],['🟩','🟩','🟩','🟩','🟩',]]

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

for x in range(0, 12):

    for y in range(0,6):
        randSquare = randint(0,4)
        randList = randint(0,5)
        baseLineMod[n-1] = ''.join(squares[randList])
        if y == 5:
            baseLineMod = [[],[],[],[],[]]

    STORE_DATA.insert(len(STORE_DATA), baseLineMod)

BACKUP_DATA = deepcopy(STORE_DATA)
        

# -----------MISC

for mnop in STORE_DATA:
    print("".join(mnop))

# -----------DUMP
'''
while i <= 10:
    for x in 'abcdefghijklmnopqrstuvwzyx1234':
        randCbLock = randrange(-1,5)
        baseLineMod[n-1] = changes[randCbLock]
        if n == 0:
            n=30
            i+=1
        else:
            n -= 1
    dupeList = tuple(baseLineMod)
    STORE_DATA.insert(len(STORE_DATA), list(dupeList))
'''