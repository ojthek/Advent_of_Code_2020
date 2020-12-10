import pprint
import fileinput

m={}
def findCombinations(l, i=0):
    if i == len(l)-1:
        return 1
    if i in m:
        return m[i]
    r = 0
    for j in range(i+1, len(l)):
        if l[j]-l[i]<= 3:
            r += findCombinations(l, j)
    m[i] = r
    return r

lines = list([int(x) for x in fileinput.input()])
lines.append(0)
lines.append(max(lines)+3)
lines = sorted(lines)

d_1 = 0
d_3 = 0
av = 0
max_d = 3

for l in lines:
    tl = av + max_d
    if av < l <= tl:
        d = l - av
        if d == 1: d_1 +=1
        if d == 3: d_3 +=1
        av = l

print("Result 1:", d_1*d_3)
print("Result 2:", findCombinations(lines))






