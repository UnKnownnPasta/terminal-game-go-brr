"""
2D MINECRAFT

mechanics: w/a/s/d movement ✔
r -> place a block
q -> remove a block
f -> scroll hotbar
/ -> command prompt
    contains: creative, hotbar overview, switch items from hotbar to hotbar, crafting
e to exit, x to show controls etc

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

hotbar = ['💓','💓','💓','💓','💓','💓','💓','💓','💓','          ','👨','            ','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜']
inventory = ['⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜']

bckpT1 = deepcopy(TerrainOne)
bckpT2 = deepcopy(TerrainTwo)
bckpT3 = deepcopy(TerrainThree)

# ----------------------> NOTE TO SELF: have finished and perfected movement

# Now Moving To Player Movement
import msvcrt

TerrainOne[0][0] = '👨'
x, y = 0, 0
currentTerrain, errL = 0, []

def mapLog(listType):
    for i in listType:
        for j in i:
            print(j,end='')
        print()

def invModify(item, listPrim):
    for i in range(12,len(listPrim)):
        found = -1
        if found == -1 and listPrim[i] == '⬜':
            found = i
            listPrim[found] = item
            break
    else:
        for i in range(0,len(inventory)):
            if inventory[i] == '⬜':
                inventory[i] = item
                break
    
def queueerror(msg, typ):
    errL.append(f'{typ} | {msg}')

# Movement loop
while True:
    if currentTerrain == 0: mapLog(TerrainOne)
    elif currentTerrain == 1: mapLog(TerrainTwo)
    elif currentTerrain == 2: mapLog(TerrainThree)
    for i in hotbar:
        print(i,end='')
    print()
    for i in range(len(errL)-1,0,-1):
        print(errL[i])
        errL.pop()
        
    c = msvcrt.getwch()

    if currentTerrain == 0:
        match c:
            case 'w':
                if y == 0:
                    TerrainOne[y][x], TerrainOne[5][x] = bckpT1[y][x], '👨'
                    if bckpT1[5][x] == '🌳':
                        invModify('🟫',hotbar)
                    x, y = x, 5
                else:
                    TerrainOne[y][x], TerrainOne[y-1][x] = bckpT1[y][x], '👨'
                    if bckpT1[y-1][x] == '🌳':
                        invModify('🟫',hotbar)
                    x, y = x, y-1

            case 's':
                if y == 5:
                    TerrainOne[y][x], TerrainOne[0][x] = bckpT1[y][x], '👨'
                    if bckpT1[0][x] == '🌳':
                        invModify('🟫',hotbar)
                    x, y = x, 0
                else:
                    TerrainOne[y][x], TerrainOne[y+1][x] = bckpT1[y][x], '👨'
                    if bckpT1[y+1][x] == '🌳':
                        invModify('🟫',hotbar)
                    x, y = x, y+1

            case 'a':
                if x == 0:
                    TerrainOne[y][x], TerrainOne[y][29] = bckpT1[y][x], '👨'
                    if bckpT1[y][29] == '🌳':
                        invModify('🟫',hotbar)
                    x, y = 29, y
                else:
                    TerrainOne[y][x], TerrainOne[y][x-1] = bckpT1[y][x], '👨'
                    if bckpT1[y][x-1] == '🌳':
                        invModify('🟫',hotbar)
                    x, y = x-1, y

            case 'd':
                if x == 29:
                    currentTerrain = 1
                    TerrainOne[y][29], TerrainTwo[y][0] = bckpT1[y][29], '👨'
                    if bckpT2[y][0] == '🌳':
                        invModify('🟫',hotbar)
                    x = 0
                else:
                    TerrainOne[y][x], TerrainOne[y][x+1] = bckpT1[y][x], '👨'
                    if bckpT1[y][x+1] == '🌳':
                        invModify('🟫',hotbar)
                    x, y = x+1, y
            
            case 'x': #ignore
                for i in inventory:
                    print(i,end='')
                print()

            case 'r':
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
                                TerrainOne[y][x], TerrainOne[y][x-1] = '🟫', '👨'
                                x, y = x-1, y
                            else:
                                TerrainOne[y][x], TerrainOne[y][x+1] = '🟫', '👨'
                                x, y = x+1, y
                            hotbar[i] = '⬜'
                            break
                

            case 'e':
                break

    if currentTerrain == 1:
        match c:
            case 'w':
                if y == 0:
                    TerrainTwo[y][x], TerrainTwo[5][x] = bckpT2[y][x], '👨'
                    x, y = x, 5
                else:
                    TerrainTwo[y][x], TerrainTwo[y-1][x] = bckpT2[y][x], '👨'
                    x, y = x, y-1

            case 's':
                if y == 5:
                    TerrainTwo[y][x], TerrainTwo[0][x] = bckpT2[y][x], '👨'
                    x, y = x, 0
                else:
                    TerrainTwo[y][x], TerrainTwo[y+1][x] = bckpT2[y][x], '👨'
                    x, y = x, y+1

            case 'a':
                if x == 0:
                    currentTerrain = 0
                    TerrainTwo[y][0], TerrainOne[y][29] = bckpT2[y][0], '👨'
                    x = 29
                else:
                    TerrainTwo[y][x], TerrainTwo[y][x-1] = bckpT2[y][x], '👨'
                    x, y = x-1, y

            case 'd':
                if x == 29:
                    currentTerrain = 2
                    TerrainTwo[y][29], TerrainThree[y][0] = bckpT2[y][29], '👨'
                    x = 0
                else:
                    TerrainTwo[y][x], TerrainTwo[y][x+1] = bckpT2[y][x], '👨'
                    x, y = x+1, y

            case 'e':
                break

    if currentTerrain == 2:
        match c:
            case 'w':
                if y == 0:
                    TerrainThree[y][x], TerrainThree[5][x] = bckpT3[y][x], '👨'
                    x, y = x, 5
                else:
                    TerrainThree[y][x], TerrainThree[y-1][x] = bckpT3[y][x], '👨'
                    x, y = x, y-1

            case 's':
                if y == 5:
                    TerrainThree[y][x], TerrainThree[0][x] = bckpT3[y][x], '👨'
                    x, y = x, 0
                else:
                    TerrainThree[y][x], TerrainThree[y+1][x] = bckpT3[y][x], '👨'
                    x, y = x, y+1

            case 'a':
                if x == 0:
                    currentTerrain = 1
                    TerrainThree[y][0], TerrainTwo[y][29] = bckpT2[y][0], '👨'
                    x = 29
                else:
                    TerrainThree[y][x], TerrainThree[y][x-1] = bckpT3[y][x], '👨'
                    x, y = x-1, y

            case 'd':
                if x == 29:
                    TerrainThree[y][x], TerrainThree[y][0] = bckpT3[y][x], '👨'
                    x, y = 0, y
                else:
                    TerrainThree[y][x], TerrainThree[y][x+1] = bckpT3[y][x], '👨'
                    x, y = x+1, y

            case 'e':
                break

    # print('\n\n\n\n')