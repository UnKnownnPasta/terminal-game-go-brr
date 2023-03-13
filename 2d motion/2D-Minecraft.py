"""
2D MINECRAFT

mechanics: w/a/s/d movement ✔
e -> place a block ✔
q -> remove a block ✔
f -> scroll hotbar ✔ (now x)
/ -> command prompt ✔
    contains: creative, hotbar overview, switch items from hotbar to inv, crafting
                              ✔                        ✔                    ✔
r to stop the game, x to show controls etc ✔ (instead of x, /)

world: biomes | huge fucking map ✔ sorta?
caves ✔
portal craftable -> nether only
villages -> one per world always at corner
    only has 1 villager, 1 chest

future future future wish:
make render distance a thing
mobs
actual fucking logic in the game

"""

# Creating Terrain
from copy import deepcopy
from random import randint
import pickle
import subprocess

# This is where the lists for terrain is prepared
TerrainOne, TerrainTwo, TerrainThree, CaveMap = ([] for i in range(4)) # Unpack three uninitialized lists
for i in range(3):
    for j in range(6):
        ns = []
        for k in range(30):
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
        if i == 0: TerrainOne.append(ns) 
        if i == 1: TerrainTwo.append(ns)
        if i == 2: TerrainThree.append(ns)

for j in range(7): # Cave map gen
    ns = []
    for k in range(30):
        if j%2 == 0:
            percent = randint(1,100)
            if percent > 70:
                ns.append('🔘')
            else:
                ns.append('🟪')
        else:
            if randint(0,10) < 1:
                ns.append('🟧')
            else:
                ns.append('  ')
    CaveMap.append(ns)

CaveMap[1][29] = CaveMap[3][29] = CaveMap[3][0] = CaveMap[5][0] = '🔘'
CaveMap[2][28] = CaveMap[4][1] = '  ' # fixing walls

TerrainOne += ['T-0', {'dropcount':0}]
TerrainTwo += ['T-1', {'dropcount':0}]
TerrainThree += ['T-2', {'dropcount':0}] # Just list identifiers
CaveMap += ['C-0', {'dropcount':0}]

hotbar = ['💓']*9+[' '*11,'👨',' '*11]+['🔲']*9 # just a simpler way of making the list
inventory = ['🔲']*25

bckpT1 = deepcopy(TerrainOne)
bckpT2 = deepcopy(TerrainTwo)
bckpT3 = deepcopy(TerrainThree)
textTemp = """ Type a number
    1 => Switch items
    2 => Crafting
    3 => Heal (food)
    4 => Drop item (from hotbar)"""

# Now Moving To Player Movement
import msvcrt
TerrainOne[0][0] = '👨'
x, y = 0, 0
currentTerrain, errorList, placeableBlocks, noMoveBlocks = 0, [], ['🟫', '🧮'], ['🔘', '🟪']
obtainableItems = ['stone|🔘', 'wood|🟫', 'craft|💠', 'furnace|🧮', 'iron|🟪']
terrainMapStorage = {
    't0': TerrainOne, 'b0': bckpT1,
    't1': TerrainTwo, 'b1': bckpT2,
    't2': TerrainThree, 'b2': bckpT3,
    't3': CaveMap, 'b3': CaveMap # supposed to be backup map
}

def createCave(x, y, map, bkpMap): # Generate the entrance to the cave in the map
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

dx, dy, dxy = randint(14,18), randint(1,3), []
createCave(dx, dy, TerrainTwo, bckpT2)

def mapLog(listType): # Print the current map
    # for i in range(0,len(listType)-2):
    #     for j in listType[i]:
    #         print(j,end='')
    #     print()
    with open('2DMC/terrain.pkl', 'wb') as f:
        pickle.dump(TerrainOne, f)
        pickle.dump(TerrainTwo, f)
        pickle.dump(TerrainThree, f)
        pickle.dump(CaveMap, f)
    
    subprocess.run(['python', 'guidisplay.py'])

def hbLog(listType): # Print the hearts + hotbar
    for i in listType:
        print(i,end='')

def healthModify(listInv): # Register damage
    for i in range(8,-1,-1): # 0,1,..,8
        if listInv[i] == '💓':
            if i == 0:
                listInv[i] = '🖤'
                return 'dead'
            else:
                listInv[i] = '🖤'
                return 'alive'

def invModify(item, listPrim): # Register picking up wood from trees
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

def objEncounterCheck(terrainMap, xCord, yCord, listInv, bckpTerrain): # Check if you walked into lava or tree or walls of cave
    if terrainMap[6] == 'T-1' and bckpTerrain[yCord][xCord] in ['⬛', '  ']:
        match bckpTerrain[yCord][xCord]:
            case '⬛': return 'nomove'
            case '  ': return 'entercave'
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

def queueerror(msg, typ): # If requirements arent met for a action, queue the error here to print during next interation of the loop
    errorList.append(f"{typ} | {msg}")

def dropItem(list, hb): # drop an item at a spot in map
    countDrop = list[-1]['dropcount'] + 1
    text = f'drop-{countDrop}'
    list[-1][text] = f'{hb[int(c4)+11]}|x{x}y{y}'
    list[-1]['dropcount'] += 1
    hb[int(c4)+11] = '🔲'

def itemCraftingRem(thing, crafting, cou, *listSent): # Remove all resources used for crafting from inventroy
    strrr = ['-1']
    listSent = list(listSent)
    for i in range(0,len(listSent)-1):
        if crafting == 'pickaxe' and f'{thing}|{cou}' == 'wood|12' and i == int(cou): break
        elif crafting == 'furnace' and f'{thing}|{cou}' == 'stone|10' and i == int(cou): break
        elif crafting == 'craft' and f'{thing}|{cou}' == 'wood|6' and i == int(cou): break
        elif crafting == 'ironpick' and f'{thing}|{cou}' in ['wood|2', 'iron|3'] and i == int(cou): break # i have to verify both are done, doesnt work 
        i = listSent[i]
        if i[0] == 'h':
            pos = i[1:]
            hotbar[int(pos)] = '🔲'
            if strrr[0] == '-1': strrr[0] = f'h|{pos}'
        if i[0] == 'i':
            pos = i[1:]
            inventory[int(pos)] = '🔲'
            if strrr[0] == '-1': strrr[0] = f'i|{pos}'
    return strrr[0]

def updateInvItem(itemList, item): # Craft the item
    idk = ['']
    posListIron = itemList['🟣'][1].split('|')
    posListWood = itemList['🟫'][1].split('|')
    posListStone = itemList['🔘'][1].split('|')

    match item:
        case '🧮':
            if (not (itemList['🔘'][0] >= 10) == True):
                queueerror(f"Do not have enough items to craft a furnace.", f'Could not craft {item}')
                return 'nomat'

            tempVar1 = itemCraftingRem('stone', 'furnace', 10, *posListStone)
            if tempVar1 != '-1': idk[0] = tempVar1
            idk = idk[0].split('|')

        case '🔨':
            if (not (itemList['🟣'][0] >= 3) == True) or (not (itemList['🟫'][0] >= 4) == True):
                queueerror(f"Do not have enough items to craft a iron pickaxe.", f'Could not craft {item}')
                return 'nomat'
            
            tempVar1 = itemCraftingRem('iron', 'ironpick', 3, *posListIron)
            tempVar2 = itemCraftingRem('wood', 'ironpick', 2, *posListWood)
            if tempVar1 != '-1': idk[0] = tempVar1
            elif tempVar2 != '-1': idk[0] = tempVar2
            idk = idk[0].split('|')

        case '⛏':
            if (not (itemList['🟫'][0] >= 12) == True):
                queueerror(f"Do not have enough items to craft a pickaxe.", f'Could not craft {item}')
                return 'nomat'

            tempVar2 = itemCraftingRem('wood', 'pickaxe', 12, *posListWood)
            if tempVar2 != '-1': idk[0] = tempVar2
            idk = idk[0].split('|')

        case '🔪':
            if (not (itemList['🟣'][0] >= 2) == True) or (not (itemList['🟫'][0] >= 4) == True):
                queueerror(f"Do not have enough items to craft a sword", f'Could not craft {item}')
                return 'nomat'

            tempVar1 = itemCraftingRem('iron', 'sword', 2, *posListIron)
            tempVar2 = itemCraftingRem('wood', 'sword', 4, *posListWood)
            if tempVar1 != '-1': idk[0] = tempVar1
            elif tempVar2 != '-1': idk[0] = tempVar2
            idk = idk[0].split('|')

        case '📦':
            if (not (itemList['🟫'][0] >= 6) == True):
                queueerror(f"Do not have enough items to craft a crafting table", f'Could not craft {item}')
                return 'nomat'

            tempVar1 = itemCraftingRem('wood', 'craft', 6, *posListWood)
            if tempVar1 != '-1': idk[0] = tempVar1
            idk = idk[0].split('|')

    # look its weird; im basically doing overcautious steps to get a accurate index to put pickaxe in
    if idk[0] == 'h': hotbar[int(idk[1])] = item
    if idk[0] == 'i': inventory[int(idk[1])] = item

def mineBlock(cavelist, inve, x, y): # Picking up blocks placed on the map
    toMine = cavelist[y-1][x]
    if toMine in ['🟫', '  ', '⬛']: return 'cantmine'
    emptIndex = -1
    if '🔲' in inve: emptIndex = inve.index('🔲')
    if emptIndex == -1: return 'nomine'
    inve[emptIndex] = toMine
    cavelist[y-1][x] = '  '
    return 'mined'

queueerror('Movement: w/a/s/d Place blocks(q), Remove blocks(r), Mine blocks (f), / To access more options; Move around in 3 different maps - build anywhere!', 'Game is Ready!') # Sample run of queueerror()

"""
NOTE: Coded movement in and out of cave, no bugs - stable
To add cave functionality, but add inventory mechanic and crafting first
                |--> Added crafting, added mining, added tools, added making/placing crafting table/furnace, cave is partially ready

Now starting adding cave features
|----> custom blocks
    -> lava damage
    -> water extinguish
    -> obsidian
    -> keys to mine up/down
    -> jumping over obbi
    -> random damage, torch, ores
-----|
"""

# Movement loop
while True:
    print()
    if currentTerrain == 0: mapLog(TerrainOne)
    elif currentTerrain == 1: mapLog(TerrainTwo)
    elif currentTerrain == 2: mapLog(TerrainThree)
    elif currentTerrain == 3: mapLog(CaveMap)
    hbLog(hotbar)
    print()
    for i in range(len(errorList)-1,-1,-1): # Shit out all stored errors from previous loop iteration
        print(errorList[i], end='')
        errorList.pop()
    print()
    dynTerrain, dynBckp = terrainMapStorage[f't{currentTerrain}'], terrainMapStorage[f'b{currentTerrain}']

    """
    Basic principle is:
        TerrainX[y][x] = '👨'
        TerrainX[y+/-1][x+/-1] = bckpTX[y][x]

        Assigning the position in the list a new value, recovering previous positions' block from the deepcopy of og terrain we have

        As for placing/removing blocks, you check hotbar first for seeing if u can place anything or hotbar to check if u can pick it up
    """
    c = msvcrt.getwch().lower()

    if c == 'x': # Display inventory
        prntSwch = 0
        print('Inventory:      Crafting:\t\tMaterials:')
        for i in range(0,len(inventory)):
            prntSwch += 1
            print(inventory[i],end='')
            if prntSwch % 5 == 0:
                match prntSwch:
                    case 5:
                        print('      🔨 - Iron Pickaxe     ' + '|| 3x 🟣 + 4x 🟫',end='')
                    case 10:
                        print('      🧮 - Furnace          ' + '|| 10x 🔘',end='')
                    case 15:
                        print('      🔪 - Sword            ' + '|| 2x 🟣 + 4x 🟫',end='')
                    case 20:
                        print('      ⛏  - Pickaxe          ' + '|| 12x 🟫',end='')
                if i == len(inventory)-1: pass
                else: print()
        
    elif c == 'r': break

    elif c == '/': # Console - SWitch item / CRaft item / DRop items
        print('>>> Select a quick action:' + textTemp)
        cc = msvcrt.getwch()
        match cc:
            case '1': # Switch items code
                print("      Select a item to switch: (Type the term)\n    > wood (🟫)\n    > craft (💠)\n    > furnace (🧮)\n    > iron (🟪)\n    > stone (🔘)")
                itemAsk = input().lower() # ['stone|🔘', 'wood|🟫', 'craft|💠', 'furnace|🧮', 'iron|🟪']
                for i in obtainableItems:
                    if i[:-2] == itemAsk:
                        itemAsk = i[-1]
                        break
                else:
                    queueerror('Invalid item given to switch', 'Could not switch'); continue

                itemFound = [-1, False]
                try: # check if its in hotbar
                    temp = hotbar.index(itemAsk)
                    itemFound[0], itemFound[1] = temp, True
                except ValueError:
                    pass

                if itemFound[1] == False: # not in hotbar, switch to hotbar
                    try:
                        temp = inventory.index(itemAsk)
                        print('Select a hotbar slot to modify: [Choose from 1 to 9]')
                        cPlace = msvcrt.getwch()
                        if cPlace.isdigit() == False:
                            queueerror('Hotbar slot should be a valid number in range 1 to 9 inclusive of both', 'Could not do action'); continue
                        if int(cPlace) not in range(1,10):
                            queueerror('Hotbar slot should be a valid number in range 1 to 9 inclusive of both', 'Could not do action'); continue

                        if cPlace == itemAsk: # item already was there, command rejected
                            queueerror(f'{itemAsk} already exists at position {cPlace} in the hotbar.', 'Could not do action'); continue
                        inventory[temp], hotbar[int(cPlace)+11] = hotbar[int(cPlace)+11], inventory[temp]
                    except ValueError:
                        queueerror('Item not found in inventory or hotbar', 'Could not do action'); continue
                else:
                    try:
                        empSpace = inventory.index('🔲')
                        inventory[empSpace], hotbar[itemFound[0]] = hotbar[itemFound[0]], inventory[empSpace]
                    except ValueError:
                        queueerror('No free space in inventory to switch item to', 'Could not do action')

            case '2': # Crafting code
                print('      Choose an item to craft:\n     1. 🔨 - Iron Pickaxe       || 3x 🟣 + 4x 🟫\n     2. 🧮 - Furnace\t       || 10x 🔘\n     3. 🔪 - Sword\t        || 2x 🟣 + 4x 🟫\n     4. ⛏ - Pickaxe\t        || 12x 🟫\n     5. 📦 - Crafting Table\t|| 6x 🟫',end='   Choose:')
                itemAsk = msvcrt.getwch()
                if itemAsk.isdigit() == False or int(itemAsk) not in range(1,6):
                        queueerror('Can only accept number inputs in range 1-4', 'Command failed')
                        continue
                # [a,b,c] a is number of times that item was found, b is index, c is where (inv or hotbar)
                foundItems = {'🟣':[0,''], '🟫':[0,''], '🔘':[0,'']}

                for i in range(12,21): # check in hotbar
                    xx = hotbar[i]
                    if xx in foundItems:
                        foundItems[xx][0] += 1
                        foundItems[xx][1] += f'h{i}|'
                for i in range(25): # check in invetory
                    xx = inventory[i]
                    if xx in foundItems:
                        foundItems[xx][0] += 1
                        foundItems[xx][1] += f'i{i}|' # i = found in inventory, h = found in hotbar, {i} is index
                print()

                match itemAsk:
                    case '1': # iron hamm- ahem pickaxe
                        updateInvItem(foundItems, '🔨')

                    case '2': # furnace
                        updateInvItem(foundItems, '🧮')

                    case '3': # sword
                        updateInvItem(foundItems, '🔪')
                    
                    case '4': # normal pickaxe
                        updateInvItem(foundItems, '⛏')

                    case '5': # crafting
                        updateInvItem(foundItems, '📦')

                """
                NOTE TO SELF: Coded crafting pickaxe; all log used bug fixed - nned to just code other items and stuff below
                rest yet to be tested - also make mining
                ofc no way to test rn
                """

            case '4': # Drop items code
                    print('Enter hotbar item to be dropped: (Number) || 1 2 3 4 5 6 7 8 || <- Order') 
                    c4 = msvcrt.getwch()
                    if c4.isdigit() == False or (int(c4) > 8):
                        queueerror('Can only accept number inputs in range 1-8', 'Cannot do action')
                        continue
                    if hotbar[int(c4)+11] == '🔲':
                        queueerror('Nothing in that hotbar slot to drop.', 'Cannot do action')
                        continue
                    queueerror('Dropped a item at that spot', f'Lost {hotbar[int(c4)+11]}')
                    if currentTerrain == 0: dropItem(TerrainOne, hotbar) # TerrainOne[-1]['dropcount']+1
                    elif currentTerrain == 1: dropItem(TerrainTwo, hotbar)
                    elif currentTerrain == 2: dropItem(TerrainThree, hotbar)
                    elif currentTerrain == 3: dropItem(CaveMap, hotbar)

    
# --------------------------------------------------------------------------------------------------------------------------------------------
    elif currentTerrain != 3: # Biome code for 0,1,2 as well as placing/removing blocks and entering cave
        match c:
            case 'w':
                if y == 0:
                    call = objEncounterCheck(dynTerrain, x, 5, hotbar, dynBckp)  
                    if call == 'quit': break
                    elif currentTerrain == 1 and call == 'nomove': continue
                    else:
                        dynTerrain[y][x], dynTerrain[5][x] = dynBckp[y][x], '👨'
                        x, y = x, 5
                else:
                    call = objEncounterCheck(dynTerrain, x, y-1, hotbar, dynBckp) 
                    if call == 'quit': break
                    elif currentTerrain == 1 and call == 'nomove': continue
                    else:
                        dynTerrain[y][x], dynTerrain[y-1][x] = dynBckp[y][x], '👨'
                        x, y = x, y-1

            case 's':
                if y == 5:
                    call = objEncounterCheck(dynTerrain, x, 0, hotbar, dynBckp)
                    if call == 'quit': break
                    elif currentTerrain == 1 and call == 'nomove': continue
                    else:
                        dynTerrain[y][x], dynTerrain[0][x] = dynBckp[y][x], '👨'
                        x, y = x, 0
                else:
                    call = objEncounterCheck(dynTerrain, x, y+1, hotbar, dynBckp) 
                    if call == 'quit': break
                    elif currentTerrain == 1 and call == 'nomove': continue
                    else:
                        dynTerrain[y][x], dynTerrain[y+1][x] = dynBckp[y][x], '👨'
                        x, y = x, y+1

            case 'a':
                if x == 0:
                    if currentTerrain != 0:
                        dynTerrain[y][x] = dynBckp[y][x]
                        currentTerrain -= 1
                        terrainMapStorage[f't{currentTerrain}'][y][29] = '👨'
                        call = objEncounterCheck(dynTerrain, 29, y, hotbar, dynBckp)
                        if call == 'quit': break
                        x, y = 29, y
                    else:
                        continue
                else:
                    call = objEncounterCheck(dynTerrain, x-1, y, hotbar, dynBckp)
                    if call == 'quit': break
                    elif currentTerrain == 1 and call == 'nomove': continue # Check if you moved into a spot occuiped by entrance to cave
                    elif currentTerrain == 1 and call == 'entercave':
                        currentTerrain = 3
                        dynTerrain[y][x] = dynBckp[y][x]
                        dxy += [x,y] # record position of cave entrance
                        CaveMap[1][0] = '👨'
                        x, y = 0, 1
                        continue
                    else:
                        dynTerrain[y][x], dynTerrain[y][x-1] = dynBckp[y][x], '👨'
                        x, y = x-1, y

            case 'd':
                if x == 29:
                    if currentTerrain != 2:
                        dynTerrain[y][x] = dynBckp[y][x]
                        currentTerrain += 1
                        terrainMapStorage[f't{currentTerrain}'][y][0] = '👨'
                        call = objEncounterCheck(dynTerrain, 0, y, hotbar, dynBckp)
                        if call == 'quit': break
                        x, y = 0, y
                    else:
                        continue
                else:
                    call = objEncounterCheck(dynTerrain, x+1, y, hotbar, dynBckp)
                    if call == 'quit': break
                    elif currentTerrain == 1 and call == 'nomove': continue # Check if you moved into a spot occuiped by entrance to cave
                    else:
                        dynTerrain[y][x], dynTerrain[y][x+1] = dynBckp[y][x], '👨'
                        x, y = x+1, y
    
            case 'q':
                if dynBckp[y][x] not in placeableBlocks:
                    queueerror('Can only pick up blocks placed by you.', 'Cannot do action')
                else:
                    try: 
                        tX = hotbar.index('🔲')
                        if tX not in range(12,21):
                            inventory.index('🔲')
                    except ValueError: queueerror('No space in inventory to store blocks', 'Cannot do action.'); continue
                    if x == 29:
                        dynTerrain[y][x-1], dynBckp[y][x], dynTerrain[y][x], x = '👨', '🟩', '🟩', x-1
                    else:
                        dynTerrain[y][x+1], dynBckp[y][x], dynTerrain[y][x], x = '👨', '🟩', '🟩', x+1
                    for i in range(12,len(hotbar)):
                        if hotbar[i] == '🔲':
                            hotbar[i] = '🟫'
                            break
                    else:
                        invModify('🟫', inventory)

            case 'e':
                print("  [1] 🟫 - Wood\n  [2] 🧮 - Furnace\n  [3] 📦 - Crafting Table\nChoose a item to place (number):",end='')
                stuff = ['🟫', '🧮', '📦']
                placing = msvcrt.getwch()
                if placing.isdigit() == False: queueerror('Invalid selection', 'Could not do action'); continue
                elif int(placing) > 3: queueerror(f'Given option is not a valid choice [Entered: {placing}]', 'Error'); continue

                if (stuff[int(placing)-1] in hotbar[12:21]) == False:
                    queueerror(f'Do not have any {stuff[int(placing)-1]} in hotbar to place', 'Cannot do action'); continue

                for i in range(12,len(hotbar)):
                    if hotbar[i] == stuff[int(placing)-1]:
                        dynTerrain[y][x] = stuff[int(placing)-1]
                        if x == 29:
                            dynTerrain[y][x], dynTerrain[y][x-1], dynBckp[y][x] = stuff[int(placing)-1], '👨', stuff[int(placing)-1]
                            x, y = x-1, y
                        else:
                            dynBckp[y][x], dynTerrain[y][x+1], dynBckp[y][x] = stuff[int(placing)-1], '👨', stuff[int(placing)-1]
                            x, y = x+1, y
                        hotbar[i] = '🔲'
                        break

# --------------------------------------------------------------------------------------------------------------------------------------------
    elif currentTerrain == 3: # Cave
        match c:
            case 'w':
                if y == 0:
                    continue
                if CaveMap[y-1][x] in noMoveBlocks:
                    continue
                else:
                    call = objEncounterCheck(dynTerrain, x, y, hotbar, dynBckp)
                    if call == 'quit': break
                    elif call == 'nomove': continue
                    else:
                        CaveMap[y][x], CaveMap[y-1][x] = '  ', '👨'
                        x, y = x, y-1

            case 's':
                if y == 5:
                    continue
                if CaveMap[y+1][x] in noMoveBlocks:
                    continue
                else:
                    call = objEncounterCheck(dynTerrain, x, y, hotbar, dynBckp)
                    if call == 'quit': break
                    elif call == 'nomove': continue
                    else:
                        CaveMap[y][x], CaveMap[y+1][x] = '  ', '👨'
                        x, y = x, y+1

            case 'd':
                if y == 5:
                    if x == 29:
                        currentTerrain = 1
                        x, y = dxy[0], dxy[1]
                        TerrainTwo[y][x] = '👨'
                        CaveMap[5][29] = '  '
                    else:
                        if CaveMap[y][x+1] in noMoveBlocks:
                            continue
                        else:
                            CaveMap[y][x], CaveMap[y][x+1] = '  ', '👨'
                            x, y = x+1, y
                else:
                    if x == 29:
                        continue
                    elif CaveMap[y][x+1] in noMoveBlocks:
                        continue
                    else:
                        call = objEncounterCheck(CaveMap, 29, y, hotbar, CaveMap)
                        if call == 'quit': break
                        elif call == 'nomove': continue
                        else:
                            CaveMap[y][x], CaveMap[y][x+1] = '  ', '👨'
                            x, y = x+1, y

            case 'a':
                if y == 1:
                    if x == 0:
                        currentTerrain = 1
                        x,y = dxy[0], dxy[1]
                        TerrainTwo[y][x] = '👨'
                        CaveMap[1][0] = '  '
                    else:
                        if CaveMap[y][x-1] in noMoveBlocks:
                            continue
                        else:
                            objEncounterCheck(CaveMap, x, y, hotbar, CaveMap)
                            CaveMap[y][x], CaveMap[y][x-1] = '  ', '👨'
                            x, y = x-1, y
                else:
                    if x == 0:
                        continue
                    if CaveMap[y][x-1] in noMoveBlocks:
                        continue
                    else:
                        call = objEncounterCheck(CaveMap, x, y, hotbar, CaveMap)
                        if call == 'quit': break
                        elif call == 'nomove': continue
                        else:
                            CaveMap[y][x], CaveMap[y][x-1] = '  ', '👨'
                            x, y = x-1, y

            case 'f':
                hbb = str(hotbar[12:21])
                if hbb.find('⛏') == -1 and hbb.find('🔨') == -1:
                    queueerror('Need a pickaxe to mine blocks', 'Cannot mine'); continue
                
                call = mineBlock(CaveMap, inventory, x, y)
                if call == 'cantmine':
                    queueerror('Not a valid block to mine with pickaxe', 'Cannot mine'); continue
                if call == 'nomine':
                    queueerror('No free space in invetory to put items in', 'Cannot mine'); continue
