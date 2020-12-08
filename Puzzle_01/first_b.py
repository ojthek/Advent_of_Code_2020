def findtribble(zahlen, ms):
    for x in zahlen:
        if x > ms:
            continue
        for y in zahlen:
            if (x+y) > ms:
                continue
            for z in zahlen:
                s = x + y + z
                d = ms - s
                if d == 0:
                    return [x, y, z]


magic_sum = 2020
file = open("input.txt", "r")
res = []
zahlen = []
for n in file:
    zahlen.append(int(n))

pairs = findtribble(zahlen, magic_sum)

print(pairs, pairs[0]*pairs[1]*pairs[2])

file.close()
