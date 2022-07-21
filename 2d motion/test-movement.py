baseLineMod = ['⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜']
from copy import deepcopy
from random import randrange
from xmlrpc.client import Boolean

# -----------INITIALIZATION
print('\nMove:', ''.join(baseLineMod), end='\n')
STORE_DATA, i, n = [], 0, 30


# -----------TERRAIN
changes = ['🟫','🟦','🟩','🟩','🟦','🟩']

while i <= 10:
    for x in 'abcdefghijklmnopqrstuvwzyx1234':
        randomNumber = randrange(-1,5)
        baseLineMod[n-1] = changes[randomNumber]
        if n == 0:
            n=30
            i+=1
        else:
            n -= 1
    dupeList = tuple(baseLineMod)
    STORE_DATA.insert(len(STORE_DATA), list(dupeList))
    print(''.join(dupeList), end='\n')


BACKUP_DATA = deepcopy(STORE_DATA)

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
        if STORE_DATA[11][lrS_d] == '👨':
            STORE_DATA[11][lrS_d] = BACKUP_DATA[11][lrS_d]
            STORE_DATA[0][lrS_d] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D+1][lrS_d] = '👨'
    
    # BACKWARD
    if c == 's':
        if STORE_DATA[0][lrS_d] == '👨':
            STORE_DATA[0][lrS_d] = BACKUP_DATA[0][lrS_d]
            STORE_DATA[11][lrS_d] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D-1][lrS_d] = '👨'

    # RIGHTWARDS
    if c == 'd':
        if lrS_d == 29: # 29 since its at end of list, index is 29
            STORE_DATA[indS_D][29] = BACKUP_DATA[indS_D][29]
            STORE_DATA[indS_D][0] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D][lrS_d+1] = '👨'

    # LEFTWARDS
    if c == 'a':
        if lrS_d == 0:
            STORE_DATA[indS_D][0] = BACKUP_DATA[indS_D][0]
            STORE_DATA[indS_D][29] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D][lrS_d-1] = '👨'

# -----------------------------------------------------

    # PRINT THE TERRAIN
    for p in STORE_DATA:
        print(''.join(p))
    
    continue