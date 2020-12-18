import fileinput
import pprint

inp = list([l.strip() for l in fileinput.input()])

active = set()

print(inp)
for y, z in enumerate(inp):
    print(z)
    for x in range(len(z)):
        if z[x] == "#":
            active.add((x,y,0,0))

print(active)

def envolve(active, rw):
    for c in range(6):
        print("Round",c)
        na = set()
        for x in range(-20,20):
            for y in range(-20,20):
                for z in range(-20,20):
                    for w in rw:
                        aa = 0
                        for dx in [-1,0,1]:
                            for dy in [-1,0,1]:
                                for dz in [-1,0,1]:
                                    for dw in [-1,0,1]:
            #                            print(x,y,z,dx,dy,dz,(x+dx, y+dy, z+dz), (x+dx, y+dy, z+dz) in active)
                                        if dx != 0 or dy != 0 or dz != 0 or dw!=0:
                                            if (x+dx, y+dy, z+dz, w+dw) in active:
                                                aa += 1

        #                print(aa)
                        if (x,y,z,w) in active and aa in [2,3]:
                            na.add((x,y,z,w))
                        if (x,y,z,w) not in active and aa == 3:
                            na.add((x,y,z,w))

        active = na
#        pprint.pprint(active)

    return len(active)

print(envolve(active.copy(),[0]))
print(envolve(active.copy(),range(-20,20)))
