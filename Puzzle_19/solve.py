import fileinput, pprint

lines = list([l.strip() for l in fileinput.input()])

rules = {}
constants = {}
values = []

dp2 = {}
def verifyList(inp, rules):
    key = (inp, tuple(rules))

    if not inp and not rules:
        return True
    if not rules:
        return False
    if not inp:
        return False

    if key in dp2:
        return dp2[key]
#    print("++++>", inp, rules)
    for z in range(len(inp)+1):
        if verify(inp[:z], rules[0]) and verifyList(inp[z:], rules[1:]):
            dp2[key] = True
            return True

    dp2[key] = False
    return False

dp = {}
def verify(inp, ruleId):
    key = (inp, ruleId)
#    print("---->", inp, ruleId)
    if ruleId not in rules:
#        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", inp, ruleId)
        return (inp == ruleId)
    if key in dp:
        return dp[key]

    for z in rules[ruleId]:
        if verifyList(inp, z):
            dp[key] = True
            return True

    dp[key] = False
    return False

s = 0
for line in lines:
    if ":" in line:
        k, r = line.split(":")[0], line.split(":")[1].strip()
#        print(k, r)
        if "\"" not in r:
            rules[k] = [x.split(" ") for x in r.split(" | ")]
        else:
            rules[k] = r.replace("\"", "")

    elif line:
#        print(line)
        if verify(line, "0"):
            s +=1
            print(line, True)
        else:
            print(line, False)

#    pprint.pprint(rules)

print("Result", s)