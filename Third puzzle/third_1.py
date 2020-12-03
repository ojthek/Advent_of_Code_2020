def expandMap(lMap, stepWidth):
	x_len = len(lMap[0])
	y_len = len(lMap)
	f = divmod(y_len, x_len)[0] * (stepWidth[0] + 1)
	print(x_len, y_len, f, divmod(y_len, x_len))

	for i in range(len(lMap)):
		line = lMap[i]
		z_line = "" 
		for z in range(f):
			z_line += line
		lMap[i] = z_line

	return lMap


def run(lMap, pos, stepWidth):
	x_len = len(lMap[0])
	y_len = len(lMap)

	expandMap(lMap, stepWidth)
	trees = 0

	while (pos[1] < y_len):
		if lMap[pos[1]][pos[0]] == "#":
			trees += 1

		new_x_pos = pos[0] + stepWidth[0]
		new_y_pos = pos[1] + stepWidth[1]

		pos[0] = new_x_pos
		pos[1] = new_y_pos

	return trees

#file = open("input3_example.txt", "r")
file = open("input3.txt", "r")

landMap = []
manPos = [0,0]
step = [3,1]

for line in file:
    landMap.append(line.strip())
file.close()

trees = run(landMap, manPos, step)

print(trees)

