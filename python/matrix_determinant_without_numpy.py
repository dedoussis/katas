from copy import deepcopy as dc

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    operands = list()
    for idx, num in enumerate(matrix[0]):
        num = num if idx % 2 == 0 else -num
        operands.append(num * determinant(minor(dc(matrix), idx)))
    return sum(operands)
   
def minor(matrix, n):
    del matrix[0]
    for i in range(len(matrix)):
        del matrix[i][n]
    return matrix