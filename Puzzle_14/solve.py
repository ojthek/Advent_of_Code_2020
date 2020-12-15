import fileinput
from bitarray import bitarray, util
import pprint
import re

mask = ""
memory = {}
memory2 = {}

def setMask(cmd):
    global mask
    mask = cmd[cmd.rfind(" ")+1:]


def setMem(cmd):
    global memory, memory2
    val = re.match(r'^mem\[(?P<id>[0-9]+)\] = (?P<value>[0-9]+)$', cmd).groupdict()
    memory[val["id"]] = trans(int(val["value"]))
    for id in trans2(int(val["id"])):
        memory2[id] = int(val["value"])

def trans(value):
    global mask
    a = util.int2ba(value, length=36)
    for i, v in enumerate(mask):
        if v != "X":
            a[i] = (v == "1")
    return a

def multipyMask(mm, pre="", offset=0):
    global mask
    m = pre
    for i, x in enumerate(mask[offset:]):
        if x != "X":
            if x == "1":
                m += "1"
            else:
                m += "X"
        else:
            multipyMask(mm, m + "0", i+offset+1)
            multipyMask(mm, m + "1", i+offset+1)

    if len(m) == len(mask):
        mm.append(m)

def trans2(value):
    global mask
    mm = []
    multipyMask(mm)
    res = []
    for m in mm:
        a = util.int2ba(value, length=36)
        for i, v in enumerate(m):
            if v != "X":
                a[i] = (v == "1")
        res.append(util.ba2int(a))
    return res

CMD = {
    "mas" : setMask,
    "mem" : setMem
}


for cmd in fileinput.input():
    CMD[cmd[0:3]](cmd.strip())

sum = 0
for key, val in memory.items():
    sum += util.ba2int(val)

print("Processing 1:", sum)

mm = []
multipyMask(mm)

sum = 0
for key, val in memory2.items():
    sum += val
print("Prozessing 2:", sum)
