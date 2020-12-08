def verifyPassports(lPassports, rFields, oFields):
    minNumFields = len(rFields)

    validPassports = []
    for passport in lPassports:
        if len(list(filter(lambda x: x in passport.keys(), rFields))) == minNumFields:
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