with open('input.txt', 'r') as f:
    lines = f.readlines()

grid = [[int(num) for num in x.strip()] for x in lines]

#  Question 1:

transformed_grid = [[x[i] for x in grid] for i in range(len(grid))]

visible = 0
for i in range(len(grid)):
    for j_idx, height in enumerate(grid[i]):
        if i == 0 or i == len(grid) - 1 or j_idx == 0 or j_idx == len(grid[i]) - 1:
            visible += 1
            continue
        if height > min(max(grid[i][:j_idx]), max(grid[i][j_idx+1:])):
            visible += 1
            continue
        if height > min(max(transformed_grid[j_idx][:i]), max(transformed_grid[j_idx][i+1:])):
            visible += 1
            continue

print("Question 1: ", visible)


# Question 2:

max_product = 0
for i_idx in range(1, len(grid)-1):
    for j_idx, height in enumerate(grid[i_idx]):
        if j_idx == 0 or j_idx == len(grid[i_idx]) - 1:
            continue

        left = reversed(grid[i_idx][:j_idx])
        right = grid[i_idx][j_idx+1:]
        top = reversed(transformed_grid[j_idx][:i_idx])
        bottom = transformed_grid[j_idx][i_idx+1:]

        
        product = 1
        for lst in [left, right, top, bottom]:
            trees = 0
            for x in lst:
                if height > x:
                    trees += 1
                else:
                    trees += 1
                    break
            product *= trees

        if product > max_product:
            max_product = product

print("Question 2: ", max_product)