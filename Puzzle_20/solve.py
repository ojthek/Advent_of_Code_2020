import fileinput, pprint

class Tile():
    def __init__(self,  id, lines):
        self.id = id
        self.tile = lines
        self.top_edge = lines[0]
        self.bottom_edge = lines[-1]
        left, right = "", ""
        for l in lines:
            left += l[0]
            right += l[-1]

        self.left_edge = left
        self.right_edge = right

    def rotateRight(self):
        top = self.top_edge
        right = self.right_edge
        bottom = self.bottom_edge
        left = self.left_edge

        self.right_edge = top

        self.bottom_edge = right
        self.bottom_edge.reverse()

        self.left_edge = bottom

        self.self_top = left
        self.self_top.reverse()

    def flipV(self):
        left = self.left_edge
        self.left_edge = self.right_edge
        self.right_edge = left

    def flipH(self):
        top = self.top_edge
        self.top_edge = self.bottom_edge
        self.bottom_edge = top

    def __str__(self):
        return "\nTile(" + self.id + ")\n\ttop:\t" + self.top_edge +"\n\tright:\t" + self.right_edge + "\n\tbottom:\t" + self.bottom_edge + "\n\tleft:\t" + self.left_edge

    def connects(self, tile):
        if self.top_edge == tile.bottom_edge:
            return "top"
        if self.right_edge == tile.left_edge:
            return "right"
        if self.bottom_edge == tile.top_edge:
            return "bottom"
        if self.left_edge == tile.right_edge:
            return "left"

        return None

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

def solvePuzzle(tile, t2connect):
    for n in t2connect:
        c = tile.connects(n)
        if c:
            print("Found neighbour", c, tile, n)
        else:
            print("Nope")

tiles = []

collectTiles()

for t in tiles:
    print(t)

solvePuzzle(tiles[0], tiles[1:])






