baseLineMod = [[],[],[],[],[],[],[],[],[],[]]
from copy import deepcopy
from distutils.command.build import build
from random import randint, randrange
import msvcrt

# -----------INITIALIZATION
STORE_DATA, i, n, l, moveCount = [], 0, 9, 0, 0
creativeMode = False
TERRAIN_DATA = []

# def buildTerrain():
#     for p in STORE_DATA:
#         print(''.join(p))

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
type10 = ['🟩','🟦','🟩','🟦','🟩']
type12 = ['🥦','🟩','🟦','🟦','🟩']

typeList = [type1]+[type2]+[type6]+[type3]+[type4]+[type5]+[type7]+[type8]+[type9]+[type10]+[type10]+[type12]

# GET THE BASE RANDOMIZED STATE
while i <= 10:
    for x in '1234567890':
        randomListFS = randint(0,10)
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

INVENTORY_DATA = ['💓','💓','💓','💓',' ',' ',' ',' ',' ','(','0',')','Inventory:',' ','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳','🔳']

BACKUP_DATA.append(INVENTORY_DATA)

print("""  2 𝑫   𝑷 𝑳 𝑨 𝑵 𝑬   𝑴 𝑰 𝑵 𝑬 𝑪 𝑹 𝑨 𝑭 𝑻  

    ❓ Here's how to play:
        - 'w' or 's' for moving up (north) or down (south)
        - 'a' or 'd' for moving left (west) or right (east)
        - 'e' to exit the game, 'c' for creative mode
        - 'r' to build, 'q' to remove a block

    💓 You have 4 hearts, stepping on lava kills you.
    🥦 Walk in tree squares to collect wood.
    🔨 You can build and destroy built blocks.

    [ ENTER TO CONTINUE ]""", end='')
input()
for n in BACKUP_DATA:
    print(''.join(n))

STORE_DATA = deepcopy(BACKUP_DATA) # main terrain
TERRAIN_DATA = deepcopy(BACKUP_DATA)

# -----------MOVEMENT
"""
checks for w/a/s/d
shifts position w.r.t:
    - first finds which list in STORE_DATA has 👨
    - second finds in which position 👨 is in that list
"""

while 1 < 2:
    c = msvcrt.getwch()
    test_for_ = 0

    # TEST FOR PLAYER
    xxxxyyyzzz = 0 # so that it runs once
    for hj in STORE_DATA:
        if ('👨' in hj) and test_for_ == 0 and xxxxyyyzzz == 0:
            test_for_ = 1
        if ('👨' not in hj) and (hj == STORE_DATA[10]) and (test_for_ == 0) and xxxxyyyzzz == 0:
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

    moveCount+=1
    # FORWARD
    if c == 'w':
        if (STORE_DATA[10][lrS_d] == '🟧' and indS_D == 0) or (STORE_DATA[indS_D-1][lrS_d] == '🟧') and creativeMode == False:
            print(STORE_DATA[10][lrS_d], STORE_DATA[indS_D-1][lrS_d])
            if INVENTORY_DATA[3] == '💓':
                INVENTORY_DATA[3] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[2] == '💓':
                INVENTORY_DATA[2] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[1] == '💓':
                INVENTORY_DATA[1] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[0] == '💓':
                INVENTORY_DATA[0] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
                for p in STORE_DATA:
                    if '👨' in p:
                        tempIndex = p.index('👨')
                        p[tempIndex] = '💀'
                        print(''.join(p))
                    else:
                        print(''.join(p))
                del STORE_DATA
                del BACKUP_DATA
                del INVENTORY_DATA
                exit('Game Over! You stepped on lava')

        elif (STORE_DATA[10][lrS_d] == '🥦' and indS_D == 0) or (STORE_DATA[indS_D-1][lrS_d] == '🥦'):
            # inventory data 10 ;;; inv starts at 14
            invCount = INVENTORY_DATA[10]
            if invCount == 0:
                INVENTORY_DATA[14] = '🟫'
                STORE_DATA[11] = INVENTORY_DATA
            
            for x in range(14, 44):
                if INVENTORY_DATA[x] == '🔳':
                    INVENTORY_DATA[x] = '🟫'
                    INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10])+1)
                    STORE_DATA[11] = INVENTORY_DATA
                    break

        # actual
        if STORE_DATA[0][lrS_d] == '👨':
            STORE_DATA[0][lrS_d] = BACKUP_DATA[0][lrS_d]
            STORE_DATA[10][lrS_d] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D-1][lrS_d] = '👨'
    
    # BACKWARD
    if c == 's':

        if (STORE_DATA[0][lrS_d] == '🟧'and indS_D == 10) or (indS_D !=10 and STORE_DATA[indS_D+1][lrS_d] == '🟧') and creativeMode == False:
            print(STORE_DATA[0][lrS_d], STORE_DATA[indS_D+1][lrS_d])
            if INVENTORY_DATA[3] == '💓':
                INVENTORY_DATA[3] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[2] == '💓':
                INVENTORY_DATA[2] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[1] == '💓':
                INVENTORY_DATA[1] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[0] == '💓':
                INVENTORY_DATA[0] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
                for p in STORE_DATA:
                    if '👨' in p:
                        tempIndex = p.index('👨')
                        p[tempIndex] = '💀'
                        print(''.join(p))
                    else:
                        print(''.join(p))
                del STORE_DATA
                del BACKUP_DATA
                del INVENTORY_DATA
                exit('Game Over! You stepped on lava')

        elif (STORE_DATA[0][lrS_d] == '🥦') or (indS_D !=10 and STORE_DATA[indS_D+1][lrS_d] == '🥦'):
            invCount = INVENTORY_DATA[10]
            if invCount == 0:
                INVENTORY_DATA[14] = '🟫'
                STORE_DATA[11] = INVENTORY_DATA
            
            for x in range(14, 44):
                if INVENTORY_DATA[x] == '🔳':
                    INVENTORY_DATA[x] = '🟫'
                    INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10])+1)
                    STORE_DATA[11] = INVENTORY_DATA
                    break

        if STORE_DATA[10][lrS_d] == '👨':
            STORE_DATA[10][lrS_d] = BACKUP_DATA[10][lrS_d]
            STORE_DATA[0][lrS_d] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D+1][lrS_d] = '👨'

    # RIGHTWARDS
    if c == 'd':

        if (STORE_DATA[indS_D][0] == '🟧' and lrS_d == 49) or (lrS_d != 49 and STORE_DATA[indS_D][lrS_d+1] == '🟧') and creativeMode == False:
            print(STORE_DATA[indS_D][0], STORE_DATA[indS_D][lrS_d+1])
            if INVENTORY_DATA[3] == '💓':
                INVENTORY_DATA[3] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[2] == '💓':
                INVENTORY_DATA[2] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[1] == '💓':
                INVENTORY_DATA[1] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[0] == '💓':
                INVENTORY_DATA[0] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
                for p in STORE_DATA:
                    if '👨' in p:
                        tempIndex = p.index('👨')
                        p[tempIndex] = '💀'
                        print(''.join(p))
                    else:
                        print(''.join(p))
                del STORE_DATA
                del BACKUP_DATA
                del INVENTORY_DATA
                exit('Game Over! You stepped on lava')

        elif (STORE_DATA[indS_D][0] == '🥦' and lrS_d == 49) or (lrS_d != 49 and STORE_DATA[indS_D][lrS_d+1] == '🥦'):
            invCount = INVENTORY_DATA[10]
            if invCount == 0:
                INVENTORY_DATA[14] = '🟫'
                STORE_DATA[11] = INVENTORY_DATA
            
            for x in range(14, 44):
                if INVENTORY_DATA[x] == '🔳':
                    INVENTORY_DATA[x] = '🟫'
                    INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10])+1)
                    STORE_DATA[11] = INVENTORY_DATA
                    break
        
        if lrS_d == 49: # 49 since its at end of list, index is 49
            STORE_DATA[indS_D][49] = BACKUP_DATA[indS_D][49]
            STORE_DATA[indS_D][0] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D][lrS_d+1] = '👨'

    # LEFTWARDS
    if c == 'a':

        if (STORE_DATA[indS_D][49] == '🟧' and lrS_d == 0) or (STORE_DATA[indS_D][lrS_d-1] == '🟧') and creativeMode == False:
            print(STORE_DATA[indS_D][49], STORE_DATA[indS_D][lrS_d-1])
            if INVENTORY_DATA[3] == '💓':
                INVENTORY_DATA[3] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[2] == '💓':
                INVENTORY_DATA[2] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[1] == '💓':
                INVENTORY_DATA[1] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
            elif INVENTORY_DATA[0] == '💓':
                INVENTORY_DATA[0] = '🖤'
                STORE_DATA[11] = INVENTORY_DATA
                for p in STORE_DATA:
                    if '👨' in p:
                        tempIndex = p.index('👨')
                        p[tempIndex] = '💀'
                        print(''.join(p))
                    else:
                        print(''.join(p))
                del STORE_DATA
                del BACKUP_DATA
                del INVENTORY_DATA
                exit('Game Over! You stepped on lava')

        elif (STORE_DATA[indS_D][49] == '🥦' and lrS_d == 0) or (STORE_DATA[indS_D][lrS_d-1] == '🥦'):
            invCount = INVENTORY_DATA[10]
            if invCount == 0:
                INVENTORY_DATA[14] = '🟫'
                STORE_DATA[11] = INVENTORY_DATA
            
            for x in range(14, 44):
                if INVENTORY_DATA[x] == '🔳':
                    INVENTORY_DATA[x] = '🟫'
                    INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10])+1)
                    STORE_DATA[11] = INVENTORY_DATA
                    break

        if lrS_d == 0:
            STORE_DATA[indS_D][0] = BACKUP_DATA[indS_D][0]
            STORE_DATA[indS_D][49] = '👨'
        else:
            STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d]
            STORE_DATA[indS_D][lrS_d-1] = '👨'

    # HEART REGEN
    if moveCount%20 == 0:
        for xxx in INVENTORY_DATA[1:4]:
            if xxx == '🖤':
                nx = INVENTORY_DATA.index(xxx)
                INVENTORY_DATA[nx] = '💓'
                STORE_DATA[11] = INVENTORY_DATA
                break

    # QUIT GAME
    if c == 'e':
        del BACKUP_DATA
        del INVENTORY_DATA
        creativeMode = False
        for p in STORE_DATA:
            print(''.join(p))
        del STORE_DATA
        exit('Exited the game.')

    # BUILDING (place)
    if c == 'r':
        currentMax = int(INVENTORY_DATA[10]) # No. of logs
        if currentMax == 0 and creativeMode == False:
            for p in STORE_DATA:
                print(''.join(p))
            print('Not enough building materials.')
            continue

        if BACKUP_DATA[indS_D][lrS_d] == '🟫':
            continue

        STORE_DATA[indS_D][lrS_d] = BACKUP_DATA[indS_D][lrS_d] = '🟫'
        for bx in INVENTORY_DATA:
            if bx == '🟫' and creativeMode == False:
                INVENTORY_DATA[INVENTORY_DATA.index(bx)] = '🔳'
                break
        if creativeMode == False:
            INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10])-1)
        else:
            INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10]))
        STORE_DATA[11] = INVENTORY_DATA

        # shifting man
        if lrS_d == 0:
            STORE_DATA[indS_D][lrS_d+1] = '👨'
        elif lrS_d > 0:
            if lrS_d == 49:
                STORE_DATA[indS_D][lrS_d-1] = '👨'
            else:
                STORE_DATA[indS_D][lrS_d+1] = '👨'

    # CREATIVE
    if c == 'c':
        if creativeMode == False:
            creativeMode = True
            for p in STORE_DATA:
                print(''.join(p))
            print('Shifted gamemodes!')
            continue
        else:
            creativeMode = False
            for p in STORE_DATA:
                print(''.join(p))
            print('Shifted gamemodes!')
            continue

    # BUILDING (pick)
    if c == 'q':
        currentMax = int(INVENTORY_DATA[10])
        if currentMax == 30:
            for p in STORE_DATA:
                print(''.join(p))
            print('No space in inventory to pick up this block.')
            continue
        
        if BACKUP_DATA[indS_D][lrS_d] != '🟫':
            for p in STORE_DATA:
                print(''.join(p))
            print('You can only pick up blocks you place.')
            continue

        for lm in INVENTORY_DATA:
            if lm == '🔳' and creativeMode == False:
                INVENTORY_DATA[INVENTORY_DATA.index(lm)] = '🟫'
                # INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10])+1)
                break

        if creativeMode == False:
            INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10])+1)
        else:
            INVENTORY_DATA[10] = str(int(INVENTORY_DATA[10]))
        
        STORE_DATA[11] = INVENTORY_DATA

        STORE_DATA[indS_D][lrS_d] = TERRAIN_DATA[indS_D][lrS_d]
        print(TERRAIN_DATA[indS_D][lrS_d])
        BACKUP_DATA[indS_D][lrS_d] = TERRAIN_DATA[indS_D][lrS_d]

        # shifting man
        if lrS_d == 0:
            STORE_DATA[indS_D][lrS_d+1] = '👨'
        elif lrS_d > 0:
            if lrS_d == 49:
                STORE_DATA[indS_D][lrS_d-1] = '👨'
            else:
                STORE_DATA[indS_D][lrS_d-1] = '👨'
        

# -----------------------------------------------------

    # PRINT THE TERRAIN
    for p in STORE_DATA:
        print(''.join(p))
    
    continue
