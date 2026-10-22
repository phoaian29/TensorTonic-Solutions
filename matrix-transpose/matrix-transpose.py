import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    A = np.asarray(A)
    rows, cols = A.shape
    B = np.empty((cols, rows), dtype=A.dtype)

    for i in range(rows):
        for j in range(cols):
            B[j, i] = A[i, j]

    return B
