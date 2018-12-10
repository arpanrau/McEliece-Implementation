import numpy as np


class hamming_keygen:
    "Generates a public key for a message of size 2^kgen-1. Returns G^, the public key, as well as S G and P (Private Key Components)"
    def __init__(self, kgen):
        self.kgen = kgen
        self.k = 2**self.kgen - self.kgen -1
        self.n = 2**self.kgen -1
        self.G = self.genHammingMatrix()
        self.S = self.genInvertibleMatrix()
        self.P = self.genPermuteMatrix()
        self.Gcarat = np.matmul(np.matmul(self.S, self.G), self.P) % 2

    def genHammingMatrix(self):
        """Generates Hamming Matrix given k and n"""
        identity = np.identity(self.kgen)
        identityk = np.identity(self.k)
        left = np.zeros((self.kgen, 2**self.kgen - 1 - self.kgen)).T
        rowcount = 0
        for i in range(2**self.kgen):
            if i + 1 != 1:
                if (i + 1) & i != 0:
                    binarystring = np.binary_repr(i+1)
                    column = np.zeros((len(binarystring), 1))
                    for i in range(len(binarystring)):
                        column[-i - 1] = binarystring[i]
                    column = np.pad(column, (0, self.kgen - len(binarystring)), 'constant')
                    left[rowcount] = column.T[0]
                    rowcount += 1
        left = left.T
        self.paritycheck = np.block([left, identity])
        self.generator = np.block([identityk, np.transpose(left)])
        return self.generator

    def genInvertibleMatrix(self):
        "Generates S ,an invertible matrix of size K*l"
        S = np.random.randint(0,2,(self.k, self.k), dtype=np.uint)
        while np.linalg.det(S) == 0:
            S = np.random.randint(0,2,(self.k, self.k), dtype=np.uint)
        return S

    def genPermuteMatrix(self):
        "Generates P, a random perumutation of the identity matrix"
        P = np.identity(self.n, dtype=np.uint)
        return P[np.random.permutation(self.n)]
