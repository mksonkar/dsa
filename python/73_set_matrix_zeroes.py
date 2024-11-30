from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    zero_indexes = []
    for arr in matrix:
        if 0 in arr:
            zero_indexes.extend([i for i, el in enumerate(arr) if el == 0])
            print(zero_indexes)
            for i in range(len(arr)):
                arr[i] = 0
    print("outside index arry", zero_indexes)
    zero_indexes = set(zero_indexes)
    for arr in matrix:
        for i in range(len(arr)):
            if i in zero_indexes:
                arr[i] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# output = [[1,0,1],[0,0,0],[1,0,1]]

setZeroes(matrix)
print(matrix)
