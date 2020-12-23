import fileinput, pprint, functools

class Tile():
    def __init__(self,  id, lines):
        self.id = id
        self.tile = lines
        self.edges = set([
            lines[0],
            ''.join(list([x[0] for x in lines])),
            lines[-1],
            ''.join(list([x[-1] for x in lines]))
        ])
        self.medges = set(list([edge[::-1] for edge in self.edges]))
        self.connections = 0

    def rotateRight(self):
        top = self.top_edge
        right = self.right_edge
        bottom = self.bottom_edge
        left = self.left_edge

        self.right_edge = top

        self.bottom_edge = right[::-1]

        self.left_edge = bottom

        self.self_top = left[::-1]

        return self

    def flipV(self):
        left = self.left_edge
        self.left_edge = self.right_edge
        self.right_edge = left
        self.top_edge = self.top_edge[::-1]
        self.bottom_edge = self.bottom_edge[::-1]

        return self

    def flipH(self):
        top = self.top_edge
        self.top_edge = self.bottom_edge
        self.bottom_edge = top
        self.left_edge = self.left_edge[::-1]
        self.right_edge = self.right_edge[::-1]

        return self

    def __str__(self):
        return "\nTile(" + self.id + ")" #\n\ttop:\t" + self.top_edge +"\n\tright:\t" + self.right_edge + "\n\tbottom:\t" + self.bottom_edge + "\n\tleft:\t" + self.left_edge

    def connects(self, tile):
        c = 0
        c += len(self.edges & tile.edges)
        c += len(self.edges & tile.medges)
        c += len(self.medges & tile.edges)
        c += len(self.medges & tile.medges)

        return c

def collectTiles():
    tileKey = -1
    tile = []
    for line in  fileinput.input():
        line = line.strip()

        if "Tile" in line:
            tileKey = line.split(" ")[1][:-1]
        elif line:
            tile.append(line)
        else:
            tiles.append(Tile(tileKey,tile))
            tile = []

def solvePuzzle():
    for tile in tiles:
        print(tile)
        c = 0
        for tile2 in tiles:
            if tile.id == tile2.id:
                continue

            count = tile.connects(tile2)
            if count > 0:
                print("Connections found", tile2.id, count)
                c += 1
        tile.connections = c

tiles = []
gC = []

collectTiles()


solvePuzzle()

print([(x.id, x.connections) for x in tiles])

print("Result:", functools.reduce(lambda x,y: x*y, [int(x.id) for x in tiles if x.connections == 2]))




