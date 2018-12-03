import numpy as np


class hamming_keygen:
    def __init__(self, k,n,kgen,S,P,m):
        self.kgen = kgen
        self.k = 2**self.kgen - self.kgen -1
        self.n = 2**self.kgen -1
        self.G = self.genhammingMatrix()
        self.S = self.genInvertibleMatrix()
        self.P = self.genPermuteMatrix()
        self.Gcarat = np.matmul(np.matmul(self.S,self.G),self.P)
        self.m = m

    def genHammingMatrix(self):
        """Generates Hamming Matrix given k and n"""
        self.identity = numpy.identity(self.kgen)
        self.identityk = numpy.identity(self.k)
        self.left = np.zeroes(self.kgen,2**self.kgen - 1 - self.kgen)
        self.rowcount = 0
        for i in range(2**self.kgen):
            if i+1 != 1:
                if (1+1)%2 != 0:
                    self.binarystring = np.binary_repr(i+1)
                    self.column = np.zeros((length(self.binarystring),1))
                    for i in binarystring:
                        self.column[0][i] = int(i)
                    self.column = np.pad(self.column, (1,self.kgen), 'constant')
                    self.left[:][count] =  self.column
        self.paritycheck = np.concatenate(self.left,self.identity)
        self.generator = np.concatenate(self.identityk,np.transpose(self.left))
        return self.generator

    def genInvertibleMatrix(self):
        self.S = np.random.randint(0,2,(self.k,self.k), dtype=np.uint)
        while np.linalg.det(S) == 0:
            self.S = np.random.randint(0,2,(self.k,self.k), dtype=np.uint)
        return self.S


    def genPermuteMatrix(self):
        self.P = np.identity(n, dtype=np.uint)
        return self.P[np.random.permutation(self.n)]
