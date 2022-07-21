from random import randrange

# ------------------------THE MAIN 1D LINE
mainLine = ['⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜']

def spaceLoop(): # empty space
    for x in '1234567890':
        print('\t\t\t\t\t\t\t\t\t\t')

spaceLoop()
print('\nMove:', ''.join(mainLine), end=' ')

# ------------------------TERRAIN
squares = ['🟫','🟦','⬛','🟩','🟩']

n=30 # how many sqaures
for x in '1234567890abcdefghijploasdcxzv':
    randomNumber = randrange(-1,5)
    mainLine[n-1] = squares[randomNumber] # change respective index of mainLine with a square
    n-=1
    
# new list to hold og terrian layout
dupeList = tuple(mainLine)

# ------------------------MOVEMENT
"""
mainLine has terrain
bar mainLine is modified as per movement to change where 👨 is placed
"""


x=0
while x < 1:
    c = input()
    if c == 'w' or c == 'd':
        spaceLoop()

        if '👨' in mainLine: 
            countLine = mainLine.count('👨') # how many 👨 are there (sometimes bugs out)
            indLine = mainLine.index('👨') # location of 👨

            if countLine == 1: # it exists solo(no double 👨), and at a actual location
                if indLine == len(mainLine)-1:
                    mainLine[indLine] = dupeList[len(dupeList)-1]  
                    mainLine[0] = '👨' 
                else:
                    mainLine[indLine+1] = '👨'
                    mainLine[indLine] = dupeList[indLine]
            else: # does not exist
                mainLine[0] = '👨'
        else: # does not exist
            mainLine[0] = '👨'

        print(''.join(mainLine))
    
    elif c == 's' or c == 'a':
        spaceLoop()

        if '👨' in mainLine:
            countLine = mainLine.count('👨')
            indLine = mainLine.index('👨')

            if countLine == 1: # it exists solo, and at a actual location
                if indLine == len(mainLine)-1:
                    mainLine[indLine] = dupeList[len(dupeList)-1]
                    mainLine[indLine-1] = '👨'
                else:
                    mainLine[indLine] = dupeList[indLine]
                    mainLine[indLine-1] = '👨'
            else: # does not exist
                mainLine[0] = '👨'
        else: # does not exist
            mainLine[0] = '👨'

        print(''.join(mainLine)) # since mainLine is a list, print it as objects

predone = []