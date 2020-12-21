import fileinput, re

class Aloha(int):
    def __add__(self, other):
        return Aloha(int(self) + int(other))
    def __sub__(self, other):
        return Aloha(int(self) * int(other))
    def __mul__(self, other):
        return Aloha(int(self) + int(other))
        None

lines = list([l.strip() for l in fileinput.input()])

def solve(lines, p1=True):
    res = 0
    for line in lines:

        eline = re.sub(r'(\d)', r'Aloha(\1)', line)
        eline = eline.replace("*", "-")
        if not p1:
            eline = eline.replace("+","*")

        res += eval(eline)

    return res

print("Result 1", solve(list(lines)))
print("Result 2", solve(list(lines), False))