magic_sum = 2020
file = open("input.txt", "r")
res = dict()
for n in file:
    z = int(n)
    d = magic_sum - z
    if z in res:
        print("Result: x=", z, ", y=", d, " Multiply=",z*d)
    else:
        res[d] = z

file.close()
