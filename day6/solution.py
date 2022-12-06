with open('input.txt', 'r') as f:
    lines = f.readlines()

signal = lines[0].strip()

# Question 1:
for i in range(len(signal)):
    if len(set(signal[i: i+4])) == 4:
        print("Question 1: ", i+4)
        break

# Question 2:
for i in range(len(signal)):
    if len(set(signal[i: i+14])) == 14:
        print("Question 2: ", i+14)
        break

