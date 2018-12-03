import numpy as np
import scipy as sp

class hamming_keygen:
    def __init__(self, k,n, S, P, m):
        self.k = k
        self.wN = -2**(-k-1)*np.log10(2)
        self.kgen = -1*((scipy.lambertw(self.wN)+k*np.log10(2)+log10(2))/np.log10(2)
        self.n = genN(self)
        self.G = self.genhammingMatrix()
        self.S = self.genInvertibleMatrix()
        self.P = self.genPermuteMatrix()
        self.Gcarat = SGP
        self.m = m

    def genN(self):
        self.n = 2**self.kgen - 1

    def genHammingMatrix(self):
        """Generates Hamming Matrix given k and n"""
        self.klength = self.k - self.n
        self.identity = numpy.identity(self.klength)
        

    def genInvertibleMatrix(self):
        self.S = np.random.randint(0,2,(self.k,self.k), dtype=np.uint)
        while np.linalg.det(S) == 0:
            self.S = np.random.randint(0,2,(self.k,self.k), dtype=np.uint)
        return self.S


    def genPermuteMatrix(self):
        self.P = np.identity(n, dtype=np.uint)
        return self.P[np.random.permutation(self.n)]
