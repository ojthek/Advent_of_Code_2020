import re
#16-18 h: hhhhhhhhhhhhhhhhhh
elemPattern = re.compile(r'^(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]{1}): (?P<password>\w+)')

goodOnes = 0
badOnes = 0

file = open("input2.txt", "r")
for line in file:
    elems = elemPattern.match(line).groupdict()
    pwLen = len(elems["password"])
    subLen = len(elems["password"].replace(elems["letter"], ""))
    resLen = pwLen - subLen
    if (int(elems["min"]) <= resLen) & (int(elems["max"]) >= resLen):
        goodOnes += 1
    else:
        badOnes += 1
    print(line, elems, pwLen, subLen, resLen, goodOnes, badOnes)


print("GoodOnes: ", goodOnes, "BadOnes: ", badOnes)




file.close()