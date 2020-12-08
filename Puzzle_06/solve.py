
def sumYes(answers):
    s = 0
    for group in answers:
#        print(group)
        s += len(group["answers"])

    return s

def sumAllYesAnswers(answers):
    s = 0
    for group in answers:
 #       print(group)
        for key in group["answers"].keys():
            if group["answers"][key] == group["persons"]:
 #               print(group["answers"][key], group["persons"])
                s += 1
    
    return s

groupAnswers = []
answers = dict()
persons = 0

#file = open("input_example.txt", "r")
file = open("input.txt", "r")

for line in file:
    line = line.strip()
    if line == "":
        groupAnswers.append({"persons": persons, "answers": answers})
        answers = dict()
        persons = 0
    else:
        persons += 1
        for a in range(len(line)):
            b = line[a]
            if b not in answers:
                answers[b] = 1
            else:
                answers[b] = answers[b] + 1

groupAnswers.append({"persons": persons, "answers": answers})


#print(groupAnswers)
print("This many answers were yes", sumYes(groupAnswers))
print("This many answers were yes over all in the group", sumAllYesAnswers(groupAnswers))

file.close()