baseLineMod = ['⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜']
from random import randrange

# -----------INITIALIZATION
print('\nMove:', ''.join(baseLineMod), end='\n')
STORE_DATA, i, n, l = [], 0, 30, 0


# -----------TERRAIN
changes = ['🟫','🟦','🟩','🟩','🟦','🟩']

while i <= 10:
    for x in '1234567890abcdefghijploasdcxzv':
        randCbLock = randrange(-1,5)
        baseLineMod[n-1] = changes[randCbLock]
        if n <= 0:
            n = 30
            i+=1
        else:
            n -= 1
    dupeList = tuple(baseLineMod)
    STORE_DATA.append(''.join(baseLineMod))
    print(''.join(dupeList), end='\n')


# -----------MOVEMENT
while l < 1: 
    c = input()

