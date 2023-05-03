import numpy as np

def freys_matrix(n):
    """
    Computes Frey's matrix for an n x n Reversi board.
    """
    center = n // 2
    matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            distance = max(abs(i - center), abs(j - center))
            if distance == center:
                matrix[i, j] = -50
            elif distance == center - 1:
                matrix[i, j] = 20
            elif i in [1, n - 2] and j in [1, n - 2]:
                matrix[i, j] = 10
            elif i in [0, n - 1] and j in [0, n - 1]:
                matrix[i, j] = 100
            else:
                matrix[i, j] = -1
                
    return matrix

frey_8x8 = freys_matrix(8)
print(frey_8x8)