with open('input.txt', 'r') as f:
    lines = f.readlines()


lines = [x.strip() for x in lines]

# (x, y)
H = (0, 0)
T = (0, 0)

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}

visited = [(0, 0)]

for line in lines:
    direction, steps = line.split(' ')
    for _ in range(int(steps)):
        x, y = H
        xx, yy = directions[direction]
        xh = x + xx
        yh = y + yy
        H = (xh, yh)

        xt, yt = T
        if abs(xh-xt) > 1:
                if xh > xt:
                    xt += 1
                else:
                    xt -= 1
                if yh != yt:
                    yt = yh

        if abs(yh-yt) > 1:
            if yh > yt:
                yt += 1
            else:
                yt -= 1
            if xh != xt:
                xt = xh

        T = (xt, yt)

        visited.append(T)

print("Question 1: ", len(set(visited)))

# Question 2:

K = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

def adjust_tail(H, T):
    xh, yh = H
    xt, yt = T

    if abs(xh-xt) >= 2 and abs(yh-yt) >= 2:
        xt = xt + 1 if xh > xt else xt - 1
        yt = yt + 1 if yh > yt else yt - 1
        return (xt, yt)

    if abs(xh-xt) >= 2:
        xt = xt + 1 if xh > xt else xt - 1
        return (xt, yh)        

    if abs(yh-yt) >= 2:
        yt = yt + 1 if yh > yt else yt - 1
        return (xh, yt)    
    
    return (xt, yt)


visited = [(0, 0)]

for line in lines:
    direction, steps = line.split(' ')
    for _ in range(int(steps)):
        for idx, knot in enumerate(K):
            if idx == 0:
                x, y = knot
                xx, yy = directions[direction]
                xh = x + xx
                yh = y + yy
                K[idx] = (xh, yh)
                continue
            
            K[idx] = adjust_tail(K[idx-1], K[idx])
        visited.append(K[-1])

print("Question 2: ", len(set(visited)))
