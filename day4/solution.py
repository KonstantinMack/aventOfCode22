with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
# Question 1: 
solution = 0
for pair in lines:
    elf1, elf2 = pair.split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')

    if ((int(elf1_start) <= int(elf2_start)) and (int(elf1_end) >= int(elf2_end))) or ((int(elf1_start) >= int(elf2_start)) and (int(elf1_end) <= int(elf2_end))):
        solution += 1

print('Question 1: ', solution)

# Question 2:
solution = 0 
for pair in lines:
    elf1, elf2 = pair.split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')

    if (int(elf2_start) <= int(elf1_start) <= int(elf2_end)) or (int(elf1_start) <= int(elf2_start) <= int(elf1_end)):
        solution += 1

print('Question 2: ', solution)
