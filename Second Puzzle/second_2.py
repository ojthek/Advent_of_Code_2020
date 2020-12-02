import re
#16-18 h: hhhhhhhhhhhhhhhhhh
elemPattern = re.compile(r'^(?P<first>\d+)-(?P<second>\d+) (?P<letter>[a-z]{1}): (?P<password>\w+)')

goodOnes = 0
badOnes = 0

file = open("input2.txt", "r")
for line in file:
    elems = elemPattern.match(line).groupdict()
    if (elems["password"][int(elems["first"])-1] == elems["letter"]) & (elems["password"][int(elems["second"])-1] == elems["letter"]):
        badOnes += 1
    elif (elems["password"][int(elems["first"])-1] == elems["letter"]) | (elems["password"][int(elems["second"])-1] == elems["letter"]):
        goodOnes += 1
    else:
        badOnes += 1
    print(line, elems, goodOnes, badOnes)




print("GoodOnes: ", goodOnes, "BadOnes: ", badOnes)




file.close()