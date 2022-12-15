with open('input.txt', 'r') as f:
    lines = f.readlines()


lines = [x.strip() for x in lines]
lines = [[(int(y.split(',')[0]), int(y.split(',')[1])) for y in x.split(' -> ')] for x in lines]

min_x = min(point[0] for line in lines for point in line)
max_x = max(point[0] for line in lines for point in line)
max_y = max(point[1] for line in lines for point in line)

start = 500 - min_x

new_lines = [[(point[1], point[0]-min_x) for point in line] for line in lines]

area = [['.' for _ in range(max_x - min_x + 1)] for __ in range(max_y + 1)]

def draw_rocks(area):
    for line in new_lines:
        for idx, point in enumerate(line):
            if idx != 0:
                start_y, start_x = line[idx-1]
                end_y, end_x = point
                if start_y == end_y:
                    for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                        area[start_y][i] = '#'
                else:
                    for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
                        area[i][start_x] = '#'
    return area

area = draw_rocks(area)

DIR = [(1, 0), (1, -1), (1, 1)]

def move(start):
    y, x = 0, start
    while not (area[y+1][x] != '.' and area[y+1][x-1] != '.' and area[y+1][x+1] != '.'):

        for dir in DIR:
            yy = y + dir[0]
            xx = x + dir[1]
            if area[yy][xx] == '.':
                y = yy
                x = xx
                break
    return (y, x)

for i in range(10000):
    try:
        sand_y, sand_x = move(start)
        area[sand_y][sand_x] = 'O'
    except:
        print("Question 1: ", i)
        break


# Question 2:

start = 500

max_y = max(point[1] for line in lines for point in line)
new_lines = [[(point[1], point[0]) for point in line] for line in lines]

area = [['.' for _ in range(1000)] for __ in range(max_y + 2)]
area.append(['#' for _ in range(1000)])
area = draw_rocks(area)

i = 0
while area[0][start] == '.':
    i += 1
    sand_y, sand_x = move(start)
    area[sand_y][sand_x] = 'O'

print("Question 2: ",  i)
