class Interpreter():
    def __init__(self, instructions):
        self.instructions = instructions
        self.pos = 0
        self.acc = 0

    def do_next_instruction(self):
        (op, arg) = self.instructions[self.pos].split(' ')
        if op == "nop":
            self.pos += 1
            return

        if op == "acc":
            self.acc += int(arg) #todo probably this is wrong
            self.pos += 1
            return

        if op == "jmp":
            self.pos = self.pos + int(arg) 
            return

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

def run(interpreter):
    print("running interpreter on instructions:", interpreter.instructions)
    seen = set()
    valid = True
    while interpreter.pos < len(interpreter.instructions):
        seen.add(interpreter.pos)
        interpreter.do_next_instruction()
        if interpreter.pos in seen:
            valid = False
            break
    return valid

for i in range(len(lines)):
    (op, arg) = lines[i].split(' ')
    if op == 'nop':
        program = lines.copy()
        program[i] = program[i].replace('nop', 'jmp')
        interpreter = Interpreter(program)
        valid = run(interpreter)
        if valid:
            print(interpreter.acc)
            break
        else:
            print("invalid program after changing instruction: ", lines[i])
    elif op == 'jmp':
        program = lines.copy()
        program[i] = program[i].replace('jmp', 'nop')
        interpreter = Interpreter(program)
        valid = run(interpreter)
        if valid:
            print(interpreter.acc)
            break
        else:
            print("invalid program after changing instruction: ", lines[i])
    else:
        print("passed over instruction: ", lines[i])