import fileinput
import pprint
import copy

def look(m,x,y,ax,ay, ca):
    nx = x
    ny = y
    while True:
        nx = nx + ax
        ny = ny + ay
        if nx < 0 or ny < 0: break
        if nx >= len(m[0]) or ny >= len(m): break
        if m[ny][nx] == "#":
            if not ca:
                return True
            else:
                return 1
        elif m[ny][nx] == "L":
            break
    if not ca:
        return False
    return 0

def occupiedInSight(m, x, y, ca=False):
#                        x,y-z
#              x-1,y-1#   #    #x+1,y-1
#                      #  #  #
#                       # # #
#                        ###
# x-z, y #################O################### x + z, y
#                        ###
#                       # # #
#                      #  #  #
#              x-1,y+1#   #   #x+1,y+1
#                        x,y+1
    return  look(m, x, y, -1, -1, ca) + \
            look(m, x, y,  0, -1, ca) + \
            look(m, x, y,  1, -1, ca) + \
            look(m, x, y, -1,  0, ca) + \
            look(m, x, y,  1,  0, ca) + \
            look(m, x, y, -1,  1, ca) + \
            look(m, x, y,  0,  1, ca) + \
            look(m, x, y,  1,  1, ca)

def placeSeats(m):
    cm = copy.deepcopy(m)
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "L":
                r =  occupiedInSight(m, x, y)
                if not r:
#                    print("Switch to #", x, y, r)
                    cm[y][x] = "#"
            elif m[y][x] == "#":
                r = occupiedInSight(m, x, y, True)
                if r>= 5:
#                    print("Switch to L", x, y, r)
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
#    print("Round",c)
#    for x in oldMap:
#        print("".join(x))
#    print("-------------____________________________________________---------------------------------------------___________________________________-")
#    for x in newMap:
#        print("".join(x))
    #pprint.pprint(oldMap)
    #pprint.pprint(newMap)
#    if c == 2: break

print("Rounds:", c)
s = sum([1 for y in range(len(newMap)) for x in range(len(newMap[0])) if newMap[y][x] == "#"])
print("Occupied seats", s)