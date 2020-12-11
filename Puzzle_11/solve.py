import fileinput
import pprint
import copy

def isTakeable(m, x, y, ca=False):
#    print("isTakeable", x, y, ca)
    c = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if j < 0 or j >= len(m[0]) or i < 0 or i >= len(m) or (i == y and j == x):
                continue
#            print(i,",",j)
            if m[i][j] == "#":
                c += 1
                if not ca:
                    return False
    if not ca:
        return True
#    print(c)
    return c

def placeSeats(m):
    cm = copy.deepcopy(m)
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "L" and isTakeable(m, x, y):
                cm[y][x] = "#"
            elif m[y][x] == "#" and isTakeable(m, x, y, True) >= 4:
                cm[y][x] = "L"

    return cm

lines = list([list(x.strip()) for x in fileinput.input()])

newMap = copy.deepcopy(lines)
c = 0
while True:
    oldMap = copy.deepcopy(newMap)
    newMap = placeSeats(oldMap)

    if oldMap == newMap: break

    c += 1
    # print("Round",c)
    # pprint.pprint(oldMap)
    # pprint.pprint(newMap)
    #if c == 1: break


for x in newMap:
    print("".join(x))

print("Rounds:", c)
s = sum([1 for y in range(len(newMap)) for x in range(len(newMap[0])) if newMap[y][x] == "#"])
print("Occupied seats", s)