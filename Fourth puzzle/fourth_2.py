import re

def validYearHelper(arg, fr, to, length):
    return (len(arg) == length) and (fr <= int(arg)) and (int(arg) <= to)

def byr(arg):
    return validYearHelper(arg, 1920, 2002, 4)

def ecl(arg):
    eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return arg in eyeColor

def pid(arg): #int(val["value"])
    if re.match("^[0-9]{9}$", arg):
        return True
    return False

def eyr(arg):
    return validYearHelper(arg, 2020, 2030, 4)

def hcl(arg):
    if re.match("^#[0-9a-f]{6}$", arg):
        return True
    return False

def iyr(arg):
    return validYearHelper(arg, 2010, 2020, 4)

def hgt(arg):
    val = re.match(r'^(?P<value>[0-9]+)(?P<scale>[cmin]{2})$', arg)
    if (val != None) and (val.groupdict()["scale"] == "cm"):
        return (150<= int(val["value"])) and (int(val["value"]) <= 193)
    elif (val != None) and (val.groupdict()["scale"] == "in"):
        return (59 <= int(val["value"])) and (int(val["value"]) <= 76)

    return False

def validatePassport(pp, rFields):
    minNumFields = len(rFields)

    switcher = {
            "byr": byr,
            "ecl": ecl,
            "pid": pid,
            "eyr": eyr,
            "hcl": hcl,
            "iyr": iyr,
            "hgt": hgt
    }

    if len(list(filter(lambda x: x in pp.keys(), rFields))) != minNumFields:
        return False

    for field in rFields:
        val = pp[field]
        if not switcher[field](val):
#            print(pp," -> ", field, val)
            return False

    return True
        

def verifyPassports(lPassports, rFields, oFields):
    validPassports = []
    for passport in lPassports:
        if validatePassport(passport, rFields):
#            print(" --> ", passport["hgt"])
            validPassports.append(passport)

    return validPassports

#file = open("input4_example.txt", "r")
file = open("input4.txt", "r")

requiredFields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
optionalFields = ["cid"]

passports = []
passport = dict()

for line in file:
    l = line.strip()
    if l == "":
        passports.append(passport)
        #Start new passport
        passport = dict()
    else:
        b = l.split(" ")
        for e in b:
            eb = e.split(":")
            passport[eb[0]] = eb[1]
passports.append(passport)

vp = verifyPassports(passports, requiredFields, optionalFields)

print("Valid numbers of passports:",len(vp))

file.close()