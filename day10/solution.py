with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

# Question 1:

x = 1
cycle = 1
cycle_snapshots = []

for command in lines:
    if cycle in [20, 60, 100, 140, 180, 220]:
        cycle_snapshots.append(x*cycle)
    if command.startswith('noop'):
        cycle += 1
        continue
    else:
        increase = int(command.split(" ")[1])
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            cycle_snapshots.append(x*cycle)
        x += increase
        cycle += 1


print("Question 1: ", sum(cycle_snapshots))


# Question 2:

x = 1
cycle = 1
cycle_snapshot = ''

for command in lines:
    if command.startswith('noop'):
        cycle_snapshot += '#' if abs((cycle % 40)-1-x) <= 1 else '.'
        cycle += 1
        continue
    else:
        increase = int(command.split(" ")[1])
        cycle_snapshot += '#' if abs((cycle % 40)-1-x) <= 1 else '.'
        cycle += 1
        cycle_snapshot += '#' if abs((cycle % 40)-1-x) <= 1 else '.'
        x += increase
        cycle += 1

print("Question 2:")
print(cycle_snapshot[:40])
print(cycle_snapshot[40:80])
print(cycle_snapshot[80:120])
print(cycle_snapshot[120:160])
print(cycle_snapshot[160:200])
print(cycle_snapshot[200:240])