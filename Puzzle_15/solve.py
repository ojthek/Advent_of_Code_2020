import fileinput

ip = list([x.strip() for x in fileinput.input()])

for g in ip:
    z = g.split(",")
    last = None
    visited = {}
    first = True
    for i, v in enumerate(z):
        visited[int(v)] = i+1
        last = int(v)
    i += 1
    while i < 30000000:
        i += 1
#        print("----->", i, last, visited)
        if first:
#            print("first")
            first = False
            last = 0
        else:
            if last in visited.keys():
#                print("visited", last)
                x = visited[last]
                visited[last] = i - 1
                last = i - x - 1
#                print(last, i , x)
            else:
#                print("unkown", last)
                visited[last] = i - 1
                last = 0

#        if i == 10: break
        if i == 2020:
            print(last)
    print(last)
print(ip)