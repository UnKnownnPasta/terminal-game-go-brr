baseLineMod = [[],[],[],[],[],[],[],[],[],[]]
from copy import deepcopy
from random import randint, randrange

# -----------INITIALIZATION
STORE_DATA, i, n, l = [], 0, 9, 0

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

# GET THE BASE RANDOMIZED STATE
while i <= 11:
    for x in '1234567890':
        randomListFS = randint(0,11)
        baseLineMod[n-1] = typeList[randomListFS]
        if n == 0:
            n, i = 9, i+1
        else:
            n-=1
    dupeList = tuple(baseLineMod)
    STORE_DATA.insert(len(STORE_DATA), list(dupeList))

"""
what is going on here is that
when STORE_DATA is created, the list in in form of [[],[],[],[]]
and .join() ignores that and generates terrain fine
but modification of indivisual tiles cannot be done

here every [] element's elements are being added to a new [], so a master STORE_DATA in the form of ['', '', '', ...] is made
"""

# THEN FIX IT HERE
BACKUP_DATA = [] # make a second copy of terrain, this is refined
for x in STORE_DATA:
    tempList = []
    for y in x:
        tempList = y + tempList
    BACKUP_DATA.insert(len(BACKUP_DATA), tempList)
    tempList = []

for v in BACKUP_DATA:
    print(''.join(v))

STORE_DATA = deepcopy(BACKUP_DATA) # main terrain

# -----------MOVEMENT
"""
checks for w/a/s/d
shifts position w.r.t:
    - first finds which list in STORE_DATA has 👨
    - second finds in which position 👨 is in that list
"""

while 1 < 2:
    c = input()
    test_for_ = 0

    # TEST FOR PLAYER
    xxxxyyyzzz = 0 # so that it runs once
    for hj in STORE_DATA:
        if ('👨' in hj) and test_for_ == 0 and xxxxyyyzzz == 0:
            test_for_ = 1
        if ('👨' not in hj) and (hj == STORE_DATA[11]) and (test_for_ == 0) and xxxxyyyzzz == 0:
            STORE_DATA[0][0] = '👨'
            test_for_ = 1
            xxxxyyyzzz = 1
            break
        else:
            continue
    
    # MAN LOCATION
    indS_D = 0 # list
    lrS_d = 0 # where in list
    for hh in STORE_DATA:
        if '👨' in hh:
            lrS_d = hh.index('👨')
            indS_D = STORE_DATA.index(hh)

    # SYNTAX
    '''
    STOREDATA[indS_D][lrS_D]
      |        |         |
      |      which list it is in
      |      eg index 3 has a list [1, 2, 3, 4]
      |                  |
      |                  |
      |              now that it is in list 3, where in list 3
      |              eg 2 is at index 1 in [1, 2, 3, 4]
      |
    the main list holding all of the squares
    '''

    # FORWARD
    if c == 'w':
        if STORE_DATA[11][lrS_d] == '🟧' or STORE_DATA[indS_D-1][lrS_d] == '🟧':
            for p in STORE_DATA:
                if '👨' in p:
                    tempIndex = p.index('👨')
                    p[tempIndex] = '💀'
                    print(''.join(p))
                else:
                    print(''.join(p))
            exit('Game Over! You stepped on lava')

        if STORE_DATA[0][lrS_d] == '👨':
            STORE_DATA[0][lrS_d] = BACKUP_DATA[0][lrS_d]
            STORE_DATA[11][lrS_d] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D-1][lrS_d] = '👨'
    
    # BACKWARD
    if c == 's':

        if STORE_DATA[0][lrS_d] == '🟧' or indS_D !=11 and STORE_DATA[indS_D+1][lrS_d] == '🟧':
            for p in STORE_DATA:
                if '👨' in p:
                    tempIndex = p.index('👨')
                    p[tempIndex] = '💀'
                    print(''.join(p))
                else:
                    print(''.join(p))
            exit('Game Over! You stepped on lava')

        if STORE_DATA[11][lrS_d] == '👨':
            STORE_DATA[11][lrS_d] = BACKUP_DATA[11][lrS_d]
            STORE_DATA[0][lrS_d] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D+1][lrS_d] = '👨'

    # RIGHTWARDS
    if c == 'd':

        if STORE_DATA[indS_D][0] == '🟧' or lrS_d != 49 and STORE_DATA[indS_D][lrS_d+1] == '🟧':
            for p in STORE_DATA:
                if '👨' in p:
                    tempIndex = p.index('👨')
                    p[tempIndex] = '💀'
                    print(''.join(p))
                else:
                    print(''.join(p))
            exit('Game Over! You stepped on lava')
        
        if lrS_d == 49: # 49 since its at end of list, index is 49
            STORE_DATA[indS_D][49] = BACKUP_DATA[indS_D][49]
            STORE_DATA[indS_D][0] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D][lrS_d+1] = '👨'

    # LEFTWARDS
    if c == 'a':

        if STORE_DATA[indS_D][49] == '🟧' or STORE_DATA[indS_D][lrS_d-1] == '🟧':
            for p in STORE_DATA:
                if '👨' in p:
                    tempIndex = p.index('👨')
                    p[tempIndex] = '💀'
                    print(''.join(p))
                else:
                    print(''.join(p))
            exit('Game Over! You stepped on lava')

        if lrS_d == 0:
            STORE_DATA[indS_D][0] = BACKUP_DATA[indS_D][0]
            STORE_DATA[indS_D][49] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D][lrS_d-1] = '👨'

# -----------------------------------------------------

    # PRINT THE TERRAIN
    for p in STORE_DATA:
        print(''.join(p))
    
    continue
