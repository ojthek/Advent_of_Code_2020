def generateSeatplan(plan, code='', min=0, max=127, depth=0):
    #print(code, min, max, depth)
    if depth < 7:
        r = divmod(max-min,2)[0]
        generateSeatplan(plan, code+'F', min, min+r, depth+1)
        generateSeatplan(plan, code+'B', min+r+1, max, depth+1)
    else:
        generateSeatplanColumn(plan, min, code)

def generateSeatplanColumn(plan, row, code='', min=0, max=7, depth=0):
    if depth < 3:
        r = divmod(max-min,2)[0]
        generateSeatplanColumn(plan, row, code+'L', min, min+r, depth+1)        
        generateSeatplanColumn(plan, row, code+'R', min+r+1, max, depth+1)
    else:
        seatId = row*8 + min
        plan[code] = seatId
        plan[seatId] = code


seatplan = dict()

generateSeatplan(seatplan)
#print(sitplanRow, len(sitplanRow))
#print(sitplanColumn, len(sitplanColumn))

file = open("input.txt", "r")
maxSeatId = 0
seatIds = []
for code in file:
    seatId = seatplan[code.strip()]
    seatIds.append(seatId)
    if seatId > maxSeatId:
        maxSeatId = seatId

print("Max seatId:", maxSeatId)
seatIds = sorted(seatIds)
#print(seatIds)
first = seatIds[0]
last = seatIds[-1]
#print(first, last)

for x in range(first, last):
    if x not in seatIds:
        print("Your seatId is", x)



file.close()