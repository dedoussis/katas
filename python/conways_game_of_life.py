# Conway's Game Of Life - Unlimited Edition
# Solution WITHOUT NumPy
from copy import deepcopy as dc

def get_generation(cells, generations):    
    if generations == 0:
        return cells
    cells = double_transpose(cells, pad)
    next_gen_cells=dc(cells)
    for x, row in enumerate(cells):
        for y, cell in enumerate(row):
            neighbours = get_neighbours(dc(cells), x, y)
            if cell == 1 and neighbours not in range(2,4):
                next_gen_cells[x][y] = 0
            elif cell == 0 and neighbours == 3:
                next_gen_cells[x][y] = 1
    next_gen_cropped = double_transpose(next_gen_cells, unpad)
    return get_generation(next_gen_cropped, generations - 1)

def get_neighbours(cells, x, y):
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            if i not in range(x-1, x+2) or j not in range(y-1, y+2) or (i==x and j==y): 
                cells[i][j] = 0
    return sum(row.count(1) for row in cells)

def double_transpose(cells, func):
    modified = func(cells, 0)
    transpose = list(map(list, zip(*modified))) 
    modified = func(transpose, 0)
    return list(map(list, zip(*modified)))
    
def pad(matrix, n):
    return [[n]*len(matrix[0])] + matrix + [[n]*len(matrix[0])]

def unpad(matrix, n):
    for idx in (0, -1):
        if all(cell == n for cell in matrix[idx]):
            del matrix[idx]
            matrix = unpad(matrix, n)
    return matrix