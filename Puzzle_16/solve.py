import fileinput
import re
import pprint

dPattern = re.compile(r'^(?P<field>[a-z ]+): (?P<r1>[0-9]+)-(?P<r2>[0-9]+) or (?P<r3>[0-9]+)-(?P<r4>[0-9]+)$')

definition = True
myTicket = False
nearbyTicket = False

fields = {}
myTicketIds = []
errors = []
valids = []
vfields = []
ffields = {}

for line in fileinput.input():
    l = line.strip()
    if l == "": continue

    if l == "your ticket:":
        definition = False
        myTicket = True
        continue

    if l == "nearby tickets:":
        definition = False
        myTicket = False
        nearbyTicket = True
        continue

    if definition:
        d = dPattern.match(l).groupdict()
        fields[d["field"]] = []
        fields[d["field"]] += [x for x in range(int(d["r1"]), int(d["r2"])+1)]
        fields[d["field"]] += [x for x in range(int(d["r3"]), int(d["r4"])+1)]

    if myTicket:
        myTicketIds = [int(x) for x in l.split(",")]

    if nearbyTicket:
        tvalid = True
        tfields = []
        for i, x in enumerate(l.split(",")):
            xx = int(x)
            tfields.append(xx)
            valid = False
            for key in fields.keys():
                if xx in fields[key]:
                    valid = True

            if not valid:
                tvalid = False
                errors.append(xx)
        if tvalid:
            valids.append(l)
            vfields.append(tfields)

#print(errors, sum(errors), valids)

e = []
kk = {}
for i in range(len(vfields[0])):
    for k in fields.keys():
        print(k)
        if k in e: continue
        wrongField = False
        for j in range(len(vfields)):

            if vfields[j][i] not in fields[k]:
                wrongField = True
                break
        if not wrongField:
            print("Bingo", k, i)
            if k in kk:
                kk[k].append(i)
            else:
                kk[k] = [i]

pprint.pprint(kk)

i = 0
nc = True
ffields = {}
while nc:
    i += 1
    nc = False
    for k in kk.keys():
        if len(kk[k]) == 1:
            nc = True
            e = kk[k][0]
            for x in kk:
                if e in kk[x]:
                    kk[x].remove(e)
            ffields[k] = e
pprint.pprint(kk)
pprint.pprint(ffields)

res = 1

for k in ffields.keys():
    if k.startswith("departure"):
        res *= myTicketIds[ffields[k]]
print(res)