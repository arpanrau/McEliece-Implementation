import numpy as np

def genPermuteMatrix(n):
    P = np.identity(n, dtype=np.uint)
    return P[np.random.permutation(n)]

def genInvertibleMatrix(k):
    S = np.random.randint(0,2,(k,k), dtype=np.uint)
    while np.linalg.det(S) == 0:
        S = np.random.randint(0,2,(k,k), dtype=np.uint)
    return S
