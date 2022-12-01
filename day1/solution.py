with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

# Question 1: Elf carrying most calories
current_cals = 0
elf_cals = []

for cal in lines:
    if cal:
        current_cals += int(cal)
    else:
        elf_cals.append(current_cals)
        current_cals = 0
        
print("Question 1: ", max(elf_cals))

# Question 2: Top 3 elf calories combined

print("Question 2: ", sum(sorted(elf_cals)[-3:]))