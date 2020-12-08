import re
import pprint

def howMany(l, findColor, aVisited=[]):
	count = 0

	for c in l[findColor]["inside"]:
		if c not in aVisited:
			count += 1
			aVisited.append(c)
			count += howMany(l, c, aVisited)

	return count

def calcCosts(l, findColor):
	costs = 0

	for (color, count) in l[findColor]["contains"]:
		costs += int(count) + int(count)*calcCosts(l, color)

	return costs

rLine = re.compile(r'^(?P<color>[a-z]+ [a-z]+) bag[s]? contain (?P<bags>.*)[.]$')
rBags = re.compile(r'(?P<count>[0-9]+) (?P<color>[a-z]+ [a-z]+) bag[s]?')

#file = open("input_example.txt", "r")
file = open("input.txt", "r")

colorBags = dict()

for line in file:
	s1 = rLine.match(line.strip()).groupdict()

	if s1["color"] not in colorBags.keys():
		colorBags[s1["color"]] = { "contains" : [], "inside" : []}

	s2 = rBags.findall(s1["bags"])
	for (count, color) in s2:
		colorBags[s1["color"]]["contains"].append([color, count])

		if color not in colorBags.keys():
			colorBags[color] = { "contains" : [], "inside" : []}

		colorBags[color]["inside"].append(s1["color"])

#pprint.pprint(colorBags)

print("How many colors?", howMany(colorBags, "shiny gold"))
print("Your costs are", calcCosts(colorBags, "shiny gold"))

file.close()