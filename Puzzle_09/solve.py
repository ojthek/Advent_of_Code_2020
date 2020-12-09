
def findWeakness(il, weakness):
    for i, x in enumerate(il):
        res = []
        if x < weakness:
            res.append(x)
            s = x
            for y in il[i+1:]:
                s += y
                if s > weakness:
                    break
                res.append(y)
                if s == weakness:
                    l = sorted(res)
                    return min(l), max(l)



def findPair(l, s):
    if len(l) < 2:
        return True
    res = dict()
    for e in l:
        d = s - e
        if e in res:
            return True
        else:
            res[d] = e

b = []
#b_size = 5
#file = open("input_example.txt", "r")
b_size = 25
file = open("input.txt", "r")


input = []
pairs = []
weakness = []
for l in file:
    n = int(l)
    input.append(n)

    if len(b) == b_size:
       if not findPair(b, n):
           pairs.append(n)

    if len(b) >= b_size:
        b = b[1:]
    b.append(n)

print("Does not have a pair", pairs)
print("Weakness", sum(findWeakness(input, pairs[0])))
file.close()