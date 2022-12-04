with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

# Question 1:
compartments = [(x[:int(len(x)/2)], x[int(len(x)/2):]) for x in lines]

prios = 0

for items in compartments:
    a, b = items
    common = ''.join(set(a).intersection(set(b)))

    if common.isupper():
        prios += ord(common) - 38
    else:
        prios += ord(common) - 96

print("Question 1: ", prios)

# Question 2: 

groups = [[lines[x], lines[x+1], lines[x+2]] for x in range(len(lines)) if x % 3 == 0]

prios = 0
for group in groups:
    common = ''.join(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))

    if common.isupper():
        prios += ord(common) - 38
    else:
        prios += ord(common) - 96

print('Question 2: ', prios)