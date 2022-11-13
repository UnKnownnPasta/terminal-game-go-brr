"""
2D MINECRAFT

mechanics: w/a/s/d movement ✔
e -> place a block ✔
q -> remove a block ✔
f -> scroll hotbar
/ -> command prompt
    contains: creative, hotbar overview, switch items from hotbar to hotbar, crafting
r to stop the game, x to show controls etc

world: biomes | huge fucking map
portal craftable -> nether only
villages -> one per world always at corner
    only has 1 villager, 1 chest

future future future wish:
caves :D
make render distance a thing
mobs
actual fucking logic in the game

"""

# Creating Terrain
from copy import deepcopy
from random import randint

# This is where the lists for movemable terrain is prepared
TerrainOne = []
for i in range(0,6):
    ns = []
    for j in range(0,30):
        percent = randint(1,100)
        if percent > 80:
            ns.append('🟨')
        elif percent > 20 and percent < 80:
            ns.append('🟩')
        elif percent < 20 and percent > 10:
            ns.append('🟦')
        elif percent < 5:
            ns.append('🟧')
        else:
            ns.append('🌳')
    TerrainOne.append(ns)

TerrainTwo = []
for i in range(0,6):
    ns = []
    for j in range(0,30):
        percent = randint(1,100)
        if percent > 80:
            ns.append('🟨')
        elif percent > 20 and percent < 80:
            ns.append('🟩')
        elif percent < 20 and percent > 10:
            ns.append('🟦')
        elif percent < 5:
            ns.append('🟧')
        else:
            ns.append('🌳')
    TerrainTwo.append(ns)

TerrainThree = []
for i in range(0,6):
    ns = []
    for j in range(0,30):
        percent = randint(1,100)
        if percent > 80:
            ns.append('🟨')
        elif percent > 20 and percent < 80:
            ns.append('🟩')
        elif percent < 20 and percent > 10:
            ns.append('🟦')
        elif percent < 5:
            ns.append('🟧')
        else:
            ns.append('🌳')
    TerrainThree.append(ns)

hotbar = ['💓']*9+[' '*11,'👨',' '*11]+['🔲']*9 # just a simpler way of making the list
inventory = ['🔲']*25

bckpT1 = deepcopy(TerrainOne)
bckpT2 = deepcopy(TerrainTwo)
bckpT3 = deepcopy(TerrainThree)

def createCave(x, y, map, bkpMap):
    for i in range(y, y+3):
        for j in range(x,x+4):
            if i == y or i == y+2:
                map[i][j], bkpMap[i][j] = '⬛', '⬛'
                continue
            elif i == y+1:
                if j == x:
                    map[i][j], bkpMap[i][j] = '⬛', '⬛'
                if j in [x+1, x+2]:
                    map[i][j], bkpMap[i][j] = '  ', '  '
                
dx, dy = randint(14,18), randint(1,3)
createCave(dx, dy, TerrainTwo, bckpT2)

# ----------------------> NOTE TO SELF: have finished and perfected movement

# Now Moving To Player Movement
import msvcrt
TerrainOne[0][0] = '👨'
x, y = 0, 0
currentTerrain, errL, placeable = 0, [], ['🟫']

def mapLog(listType): # Print the current map
    for i in listType:
        for j in i:
            print(j,end='')
        print()

def hbLog(listType): # Print the hearts + hotbar
    for i in listType:
        print(i,end='')

def healthModify(listInv): # Register damage
    # 0,1,..,8 health also shift + enter for python ide
    for i in range(8,-1,-1):
        if listInv[i] == '💓':
            if i == 0:
                listInv[i] = '🖤'
                return 'dead'
            else:
                listInv[i] = '🖤'
                return 'alive'

def invModify(item, listPrim): # Register pickinh up wood from trees
    for i in range(12,len(listPrim)):
        found = -1
        if found == -1 and listPrim[i] == '🔲':
            found = i
            listPrim[found] = item
            break
    else:
        for i in range(0,len(inventory)):
            if inventory[i] == '🔲':
                inventory[i] = item
                break

def objEncounterCheck(terrainMap, xCord, yCord, listInv, bckpTerrain): # Check if you walked into lava or tree
    if bckpTerrain[yCord][xCord] == '🌳':
        invModify('🟫',listInv)
    elif bckpTerrain[yCord][xCord] == '🟧':
        hpCall = healthModify(listInv)
        if hpCall == 'dead':
            listInv[10] = '💀'
            mapLog(terrainMap)
            hbLog(listInv)
            print('\nYou Died by Stepping On Lava!')
            return 'quit'

def queueerror(msg, typ): # If requirements arent met for a action, queue the error here
    errL.append(f'{typ} | {msg}')

queueerror('Movement: w/a/s/d Place blocks(q) and Remove blocks(r)', 'Game is Ready!') # Sample run of queueerror()

# Movement loop
while True:
    if currentTerrain == 0: mapLog(TerrainOne)
    elif currentTerrain == 1: mapLog(TerrainTwo)
    elif currentTerrain == 2: mapLog(TerrainThree)
    hbLog(hotbar)
    print()
    for i in range(len(errL)-1,-1,-1): # Shit out all stored errors from previous loop iteration
        print(errL[i], end='')
        errL.pop()

    """
    Basic principle is:
        TerrainX[y][x] = '👨'
        TerrainX[y+/-1][x+/-1] = bckpTX[y][x]

        Assigning the position in the list a new value, recovering previous positions' block from the deepcopy of og terrain we have

        As for placing/removing blocks, you check hotbar first for seeing if u can place anything or hotbar to check if u can pick it up
    """

    
    print()
    c = msvcrt.getwch()
    # each "biome" has its own code, just looks same rn
    if currentTerrain == 0:
        match c: # check for fw/ bw/ sideways and shift x and y coord correspondingly
            case 'w':
                if y == 0:
                    TerrainOne[y][x], TerrainOne[5][x] = bckpT1[y][x], '👨'
                    call = objEncounterCheck(TerrainOne, x, 5, hotbar, bckpT1)  
                    if call == 'quit': break
                    x, y = x, 5
                else:
                    TerrainOne[y][x], TerrainOne[y-1][x] = bckpT1[y][x], '👨'
                    call = objEncounterCheck(TerrainOne, x, y-1, hotbar, bckpT1) # its a object check for tree, lava under one thing and implemented only for t1 w
                    if call == 'quit': break
                    x, y = x, y-1

            case 's':
                if y == 5:
                    TerrainOne[y][x], TerrainOne[0][x] = bckpT1[y][x], '👨'
                    call = objEncounterCheck(TerrainOne, x, 0, hotbar, bckpT1)
                    if call == 'quit': break
                    x, y = x, 0
                else:
                    TerrainOne[y][x], TerrainOne[y+1][x] = bckpT1[y][x], '👨'
                    call = objEncounterCheck(TerrainOne, x, y+1, hotbar, bckpT1)
                    if call == 'quit': break
                    x, y = x, y+1

            case 'a':
                if x == 0:
                    continue
                else:
                    TerrainOne[y][x], TerrainOne[y][x-1] = bckpT1[y][x], '👨'
                    call = objEncounterCheck(TerrainOne, x-2, y, hotbar, bckpT1)
                    if call == 'quit': break
                    x, y = x-1, y

            case 'd':
                if x == 29:
                    currentTerrain = 1
                    TerrainOne[y][29], TerrainTwo[y][0] = bckpT1[y][29], '👨'
                    call = objEncounterCheck(TerrainTwo, 0, y, hotbar, bckpT2)
                    if call == 'quit': break
                    x = 0
                else:
                    TerrainOne[y][x], TerrainOne[y][x+1] = bckpT1[y][x], '👨'
                    call = objEncounterCheck(TerrainOne, x+1, y, hotbar, bckpT1)
                    if call == 'quit': break
                    x, y = x+1, y
            
            case 'x': #ignore
                for i in inventory:
                    print(i,end='')
                print()

            case 'e': # Code to place blocks
                d = 0
                for i in hotbar[12:]:
                    if i == '🟫': d+=1
                if d == 0:
                    queueerror('Need active place able blocks in hotbar.', 'Cannot do action')
                else:
                    for i in range(12,len(hotbar)):
                        if hotbar[i] == '🟫':
                            TerrainOne[y][x] = '🟫'
                            if x == 29:
                                TerrainOne[y][x], TerrainOne[y][x-1], bckpT1[y][x] = '🟫', '👨', '🟫'
                                x, y = x-1, y
                            else:
                                TerrainOne[y][x], TerrainOne[y][x+1], bckpT1[y][x] = '🟫', '👨', '🟫'
                                x, y = x+1, y
                            hotbar[i] = '🔲'
                            break
                
            case 'q': # Code to pickup a block placed by you
                if bckpT1[y][x] not in placeable:
                    queueerror('Can only pick up blocks placed by you.', 'Cannot do action')
                else:
                    if x == 29:
                        TerrainOne[y][x-1], bckpT1[y][x], TerrainOne[y][x], x = '👨', '🟩', '🟩', x-1
                    else:
                        TerrainOne[y][x+1], bckpT1[y][x], TerrainOne[y][x], x = '👨', '🟩', '🟩', x+1
                    for i in range(12,len(hotbar)):
                        if hotbar[i] == '🔲':
                            hotbar[i] = '🟫'
                            break
                    else:
                        invModify('🟫', inventory)

            case 'r':
                break

# movement to be modified to check if player enters cave
# --------------------------------------------------------------------------------------------------------------------------------------------
    if currentTerrain == 1: # 2nd Biome
        match c:
            case 'w':
                if y == 0:
                    TerrainTwo[y][x], TerrainTwo[5][x] = bckpT2[y][x], '👨'
                    call = objEncounterCheck(TerrainTwo, x, 5, hotbar, bckpT2)  
                    if call == 'quit': break
                    x, y = x, 5
                else:
                    TerrainTwo[y][x], TerrainTwo[y-1][x] = bckpT2[y][x], '👨'
                    call = objEncounterCheck(TerrainTwo, x, y-1, hotbar, bckpT2) # its a object check for tree, lava under one thing and implemented only for t1 w
                    if call == 'quit': break
                    x, y = x, y-1

            case 's':
                if y == 5:
                    TerrainTwo[y][x], TerrainTwo[0][x] = bckpT2[y][x], '👨'
                    call = objEncounterCheck(TerrainTwo, x, 0, hotbar, bckpT2)
                    if call == 'quit': break
                    x, y = x, 0
                else:
                    TerrainTwo[y][x], TerrainTwo[y+1][x] = bckpT2[y][x], '👨'
                    call = objEncounterCheck(TerrainTwo, x, y+1, hotbar, bckpT2)
                    if call == 'quit': break
                    x, y = x, y+1

            case 'a':
                if x == 0:
                    currentTerrain = 0
                    TerrainTwo[y][x], TerrainOne[y][29] = bckpT2[y][x], '👨'
                    call = objEncounterCheck(TerrainOne, 29, y, hotbar, bckpT1)
                    if call == 'quit': break
                    x, y = 29, y
                else:
                    TerrainTwo[y][x], TerrainTwo[y][x-1] = bckpT2[y][x], '👨'
                    call = objEncounterCheck(TerrainTwo, x-2, y, hotbar, bckpT2)
                    if call == 'quit': break
                    x, y = x-1, y

            case 'd':
                if x == 29:
                    currentTerrain = 2
                    TerrainTwo[y][29], TerrainThree[y][0] = bckpT2[y][29], '👨'
                    call = objEncounterCheck(TerrainThree, 0, y, hotbar, bckpT3)
                    if call == 'quit': break
                    x = 0
                else:
                    TerrainTwo[y][x], TerrainTwo[y][x+1] = bckpT2[y][x], '👨'
                    call = objEncounterCheck(TerrainTwo, x+1, y, hotbar, bckpT2)
                    if call == 'quit': break
                    x, y = x+1, y
            
            case 'x': #ignore
                for i in inventory:
                    print(i,end='')
                print()

            case 'e':
                d = 0
                for i in hotbar[12:]:
                    if i == '🟫': d+=1
                if d == 0:
                    queueerror('Need active place able blocks in hotbar.', 'Cannot do action')
                else:
                    for i in range(12,len(hotbar)):
                        if hotbar[i] == '🟫':
                            TerrainTwo[y][x] = '🟫'
                            if x == 29:
                                TerrainTwo[y][x], TerrainTwo[y][x-1], bckpT2[y][x] = '🟫', '👨', '🟫'
                                x, y = x-1, y
                            else:
                                TerrainTwo[y][x], TerrainTwo[y][x+1], bckpT2[y][x] = '🟫', '👨', '🟫'
                                x, y = x+1, y
                            hotbar[i] = '🔲'
                            break
                
            case 'q':
                if bckpT2[y][x] not in placeable:
                    queueerror('Can only pick up blocks placed by you.', 'Cannot do action')
                else:
                    if x == 29:
                        TerrainTwo[y][x-1], bckpT2[y][x], TerrainTwo[y][x], x = '👨', '🟩', '🟩', x-1
                    else:
                        TerrainTwo[y][x+1], bckpT2[y][x], TerrainTwo[y][x], x = '👨', '🟩', '🟩', x+1
                    for i in range(12,len(hotbar)):
                        if hotbar[i] == '🔲':
                            hotbar[i] = '🟫'
                            break
                    else:
                        invModify('🟫', inventory)

            case 'r':
                break


# --------------------------------------------------------------------------------------------------------------------------------------------
    if currentTerrain == 2: # 3rd Biome
        match c: 
            case 'w':
                if y == 0:
                    TerrainThree[y][x], TerrainThree[5][x] = bckpT3[y][x], '👨'
                    call = objEncounterCheck(TerrainThree, x, 5, hotbar, bckpT3)  
                    if call == 'quit': break
                    x, y = x, 5
                else:
                    TerrainThree[y][x], TerrainThree[y-1][x] = bckpT3[y][x], '👨'
                    call = objEncounterCheck(TerrainThree, x, y-1, hotbar, bckpT3) # its a object check for tree, lava under one thing and implemented only for t1 w
                    if call == 'quit': break
                    x, y = x, y-1

            case 's':
                if y == 5:
                    TerrainThree[y][x], TerrainThree[0][x] = bckpT3[y][x], '👨'
                    call = objEncounterCheck(TerrainThree, x, 0, hotbar, bckpT3)
                    if call == 'quit': break
                    x, y = x, 0
                else:
                    TerrainThree[y][x], TerrainThree[y+1][x] = bckpT3[y][x], '👨'
                    call = objEncounterCheck(TerrainThree, x, y+1, hotbar, bckpT3)
                    if call == 'quit': break
                    x, y = x, y+1

            case 'a':
                if x == 0:
                    currentTerrain = 1
                    TerrainThree[y][x], TerrainTwo[y][29] = bckpT3[y][x], '👨'
                    call = objEncounterCheck(TerrainTwo, 29, y, hotbar, bckpT2)
                    if call == 'quit': break
                    x, y = 29, y
                else:
                    TerrainThree[y][x], TerrainThree[y][x-1] = bckpT3[y][x], '👨'
                    call = objEncounterCheck(TerrainThree, x-2, y, hotbar, bckpT3)
                    if call == 'quit': break
                    x, y = x-1, y

            case 'd':
                if x == 29:
                    continue
                else:
                    TerrainThree[y][x], TerrainThree[y][x+1] = bckpT3[y][x], '👨'
                    call = objEncounterCheck(TerrainThree, x+1, y, hotbar, bckpT3)
                    if call == 'quit': break
                    x, y = x+1, y
            
            case 'x': #ignore
                for i in inventory:
                    print(i,end='')
                print()

            case 'e':
                d = 0
                for i in hotbar[12:]:
                    if i == '🟫': d+=1
                if d == 0:
                    queueerror('Need active place able blocks in hotbar.', 'Cannot do action')
                else:
                    for i in range(12,len(hotbar)):
                        if hotbar[i] == '🟫':
                            TerrainThree[y][x] = '🟫'
                            if x == 29:
                                TerrainThree[y][x], TerrainThree[y][x-1], bckpT3[y][x] = '🟫', '👨', '🟫'
                                x, y = x-1, y
                            else:
                                TerrainThree[y][x], TerrainThree[y][x+1], bckpT3[y][x] = '🟫', '👨', '🟫'
                                x, y = x+1, y
                            hotbar[i] = '🔲'
                            break
                
            case 'q':
                if bckpT3[y][x] not in placeable:
                    queueerror('Can only pick up blocks placed by you.', 'Cannot do action')
                else:
                    if x == 29:
                        TerrainThree[y][x-1], bckpT3[y][x], TerrainThree[y][x], x = '👨', '🟩', '🟩', x-1
                    else:
                        TerrainThree[y][x+1], bckpT3[y][x], TerrainThree[y][x], x = '👨', '🟩', '🟩', x+1
                    for i in range(12,len(hotbar)):
                        if hotbar[i] == '🔲':
                            hotbar[i] = '🟫'
                            break
                    else:
                        invModify('🟫', inventory)

            case 'r':
                break
    # print('\n\n\n\n')
