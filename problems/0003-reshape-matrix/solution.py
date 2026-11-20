import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    if (len(a) * len(a[0])) != (new_shape[0] * new_shape[1] ) : 
        return []
    b = [[0 for j in range(new_shape[1])] for i in range(new_shape[0])]
    k = 0
    for i in range(len(a)) :
        for j in range(len(a[0])) :
            row = k // new_shape[1]
            col = k % new_shape[1]
            b[row][col] = a[i][j]
            k += 1
    return b