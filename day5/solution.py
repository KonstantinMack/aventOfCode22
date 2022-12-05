import copy

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
instructions = lines[10:]
instructions = [instruction.split(' ')[1::2] for instruction in instructions if instruction]

stacks = {
    '1': ['R', 'H', 'M', 'P', 'Z'],
    '2': ['B', 'J', 'C', 'P'],
    '3': ['D', 'C', 'L', 'G', 'H', 'N', 'S'],
    '4': ['L', 'R', 'S', 'Q', 'D', 'M', 'T', 'F'],
    '5': ['M', 'Z', 'T', 'B', 'Q', 'P', 'S', 'F'],
    '6': ['G', 'B', 'Z', 'S', 'F', 'T'],
    '7': ['V', 'R', 'N'],
    '8': ['M', 'C', 'V', 'D', 'T', 'L', 'G', 'P'],
    '9': ['L', 'M', 'F', 'J', 'N', 'Q', 'W']
}

stacks = {key: [x for x in reversed(value)] for key, value in stacks.items()}

# Question 1
stacks_q1 = copy.deepcopy(stacks)
for number, from_stack, to_stack in instructions:
    for _ in range(int(number)):
        crate = stacks_q1[from_stack].pop()
        stacks_q1[to_stack].append(crate)
    
solution1 = "".join(i[-1] for i in stacks_q1.values())

print("Question 1: ", solution1)

# Question 2:
stacks_q2 = copy.deepcopy(stacks)

for number, from_stack, to_stack in instructions:    
    crates = stacks_q2[from_stack][-int(number):]
    stacks_q2[from_stack] = stacks_q2[from_stack][:-int(number)]
    stacks_q2[to_stack].extend(crates)
    
solution2 = "".join(i[-1] for i in stacks_q2.values())

print("Question 2: ", solution2)