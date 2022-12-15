with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

lines = [x.split(" ") for x in lines]

coords = []

for line in lines:
    sensor_x = int(line[2].split('=')[1].split(',')[0])
    sensor_y = int(line[3].split('=')[1].split(':')[0])
    beacon_x = int(line[8].split('=')[1].split(',')[0])
    beacon_y = int(line[9].split('=')[1])
    coords.append(((sensor_y, sensor_x), (beacon_y, beacon_x)))


def calc_manhatten(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])

target_line = 2000000
target_line_x_vals = set()
sensors_target_line = len({1 for x in coords if x[1][0] == target_line})

for sensor, beacon in coords:
    dist = calc_manhatten(sensor, beacon)
    i=0
    while True:
        target = (target_line, sensor[1]+i)
        if calc_manhatten(sensor, target) <= dist:
            target_line_x_vals.add(sensor[1]+i)
            target_line_x_vals.add(sensor[1]-i)
            i+=1
        else:
            break

print("Question 1: ", len(target_line_x_vals) - sensors_target_line)

#  Question 2:

coords = [(sensor, beacon, calc_manhatten(sensor, beacon)) for sensor, beacon in coords]

limit = 4000000

DIR = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def find():
    for idx, (sensor, beacon, dist) in enumerate(coords):
        print(f"Checking sensor number {idx+1}")
        for dx in range(dist+2):
            dy = dist + 1 - dx
            for dir in DIR:
                y = sensor[0] + (dy * dir[0])
                x = sensor[1] + (dx * dir[1])
                if not(0 < x < limit and 0 < y < limit):
                    continue
                else:
                    is_solution = True
                    for s, b, d in coords:
                        if calc_manhatten(s, (y, x)) <= d:
                            is_solution = False
                            break
                    
                    if is_solution:
                        return x * 4000000 + y

print("Question 2: ", find())
                

                






