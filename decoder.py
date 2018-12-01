import numpy as np


class decoder:
    def __init__(self, c, S, P, m):
        self.c = c
        self.S = S
        self.P = P
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
        pass

    def is_correct(self):
        return self.correct