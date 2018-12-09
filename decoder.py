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
        parity_bits = np.ma.size(parity,0)
        parity_total = 0
        for i in range(parity_bits):
            index = self.c_prime.size - ((-1*parity_bits - 1) + i)
            parity_total += 2**index + self.c_prime[index]
     if parity_total == 0:
         return self.c_prime[0:(self.c_prime.size-parity_bits)]
    else:
        error_message = self.c_prime[0:(self.c_prime.size-parity_bits)]
        if error_message[parity_total] == 1:
            error_message[parity_total] = 0
            return error_message
        elif error_message[parity_total] == 0:
            error_message[parity_total] = 1
            return error_message
        else:
            print("This code is broken")



        pass  # remove parity bits and return

    def is_correct(self):
        return self.correct
