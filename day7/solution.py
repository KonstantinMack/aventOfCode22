import copy

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

# Question 1:

cwd = []

file_sizes = {}

for i in lines:
    if i.startswith('$ cd'):
        slug = i.split(' ')[-1]
        if slug == "/":
            cwd = ["/"]
        elif slug == "..":
            cwd.pop()
        else:
            cwd.append(slug)

    elif i.startswith('dir ') or i.startswith('$'):
        continue
    else:
        size = int(i.split(' ')[0])
        for i in range(len(cwd)):
            path = '/'.join(cwd[:i+1])
            if not path:
                path = '/'
            if path in file_sizes:
                file_sizes[path].append(size)
            else:
                file_sizes[path] = [size]


print("Question 1: ", sum(sum(v) for v in file_sizes.values() if sum(v) < 100000))


# Question 2:
needed_space = 30000000 - (70000000 - sum(file_sizes['/']))

for i in sorted([sum(v) for v in file_sizes.values()]):
    if i >= needed_space:
        print("Question 2: ", i)
        break
