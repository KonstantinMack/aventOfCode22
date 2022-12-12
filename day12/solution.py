with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
char_map = {"S": 1, "E": 26}
HEIGHTS = [[char_map.get(char, ord(char) - ord('a') + 1) for char in x] for x in lines]

# Question 1:
start = [
         (idx, line.find('S'), 0) 
         for idx, line in enumerate(lines) 
         if 'S' in line
        ]

def find_shortest_path(nodes):
    seen = set()
    while nodes:
        y, x, d = nodes.pop(0)

        if (y, x) in seen:
            continue

        seen.add((y, x))
        if lines[y][x] == 'E':
            return d

        for dir in DIR:
            yy = y + dir[0]
            xx = x + dir[1]

            if 0 <= yy < len(lines) and 0 <= xx < len(lines[0]) and HEIGHTS[yy][xx] <= 1 + HEIGHTS[y][x]:
                nodes.append((yy, xx, d+1))

print("Question 1: ", find_shortest_path(start))

# Question 2:
start = [
         (idx_y, idx_x, 0) 
         for idx_y, line in enumerate(lines) 
         for idx_x, char in enumerate(line) 
         if char == "a"
        ]


print("Question 2: ", find_shortest_path(start))