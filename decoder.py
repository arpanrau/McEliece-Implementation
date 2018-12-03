import numpy as np


class decoder:
    def __init__(self, c, S, P, H, m):
        self.c = c
        self.S = S
        self.P = P
        self.H = H
        self.m = m
        self.decrypted = self.decrypt()
        self.correct = (self.m == self.decrypted)

    def decrypt(self):
        P_inv = np.linalg.inv(self.P)
        S_inv = np.linalg.inv(self.S)
        c_prime = np.matmul(self.c, P_inv)
        m_prime = self.error_corection(c_prime)
        decrypted = np.matmul(m_prime, S_inv)
        return decrypted

    def error_corection(self, c_prime):
        parity = np.matmul(c_prime, np.transpose(self.H))
        if not np.all(parity == 0):
            error_loc = 0
            for i in range(self.n):
                if ((i+1) & i) == 0:
                    error_loc += 2**i
            c_prime[error_loc] = !c_prime[error_loc]
        pass  # remove parity bits and return

    def is_correct(self):
        return self.correct