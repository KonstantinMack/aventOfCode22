import json
from itertools import zip_longest
from functools import cmp_to_key

with open('input.txt', 'r') as f:
    lines = f.read()

lines = [[json.loads(x.split('\n')[0]), json.loads(x.split('\n')[1])] for x in lines.split('\n\n')]

# Question 1:

def run_compare(one, two):
    isValid = None

    def compare(one, two):
        nonlocal isValid
        if one == "out" and isValid == None:
            isValid = True
        if two == "out" and isValid == None:
            isValid = False
        if type(one) == int and type(two) == int:
            if two > one and isValid == None:
                isValid = True 
            elif two < one and isValid == None:
                isValid = False
            else:
                pass

        if type(one) == list and type(two) == int:
            compare(one, [two])

        if type(one) == int and type(two) == list:
            compare([one], two)

        if type(one) == list and type(two) == list:
            for i, j in zip_longest(one, two, fillvalue='out'):
                compare(i, j)

    compare(one, two)

    return isValid

valids = [idx for idx, (one, two) in enumerate(lines, start=1) if run_compare(one, two)]

print("Question 1: ", sum(valids))

# Question 2:

compare_key = cmp_to_key(lambda x,y: run_compare(x,y) * (-1))

all_lines = [item for line in lines for item in line]
all_lines.extend([[[2]], [[6]]])

sorted_lines = sorted(all_lines, key=compare_key)

idxs = [idx for idx, line in enumerate(sorted_lines, start=1) if line in [[[2]], [[6]]]]

print("Question 2: ", idxs[0] * idxs[1])