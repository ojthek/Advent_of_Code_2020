def process(cmdStack, acc=0, pointer=0, visited=[]):
    if pointer >= len(cmdStack):
        return "Done", acc

    if pointer in visited:
        return "Error", acc

    cmd = cmdStack[pointer]

    visited.append(pointer)
    if cmd[0] == "acc":
        acc += cmd[1]
        return process(cmdStack, acc, pointer + 1, visited)
    elif cmd[0] == "jmp":
        newPointer = pointer + cmd[1]
        return process(cmdStack, acc, newPointer, visited)
    elif cmd[0] == "nop":
        return process(cmdStack, acc, pointer + 1, visited)

def toggleCmd(cmd):
    if cmd == "jmp":
        return "nop"
    return "jmp"

def processFixed(cmdStack):
    r = process(cmdStack)

    if r[0] == "Error":
        for i, cmd in enumerate(cmdStack):
            if cmd[0] == "jmp" or cmd[0] == "nop":
                newStack = cmdStack[:]
                newStack[i] = [toggleCmd(cmd[0]), cmd[1]]
                r = process(newStack, 0, 0, [])
                if r[0] == "Done":
                    return r
    return r

#file = open("input_example.txt")
file = open("input.txt")

stack = []

for instruction in file:
    cmd = instruction.strip().split( )
    stack.append([cmd[0], int(cmd[1])])

print("Process normal", process(stack))
print("Process wth single cmd fix", processFixed(stack))
file.close()