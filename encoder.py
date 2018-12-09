import numpy as np

class Encoder:
    def __init__(self, m, g_prime, t=1):
        self.g_prime = g_prime
        self.message = m
        (k, n) = g_prime.shape
        self.k = k
        self.n = n
        self.t = t
        self.z = self.generate_errors()
        self.encoded = self.encode()

    def generate_errors(self):
        z = np.zeros(self.n)
        idx_list = np.random.choice(self.n, self.t, replace=False)
        for idx in idx_list:
            z[idx] = 1
        return z

    def encode(self):
        c_prime = np.matmul(self.message, self.g_prime) % 2
        c = (c_prime + self.z) % 2
        print(c, c_prime)
        return c

    def get_message(self):
        return self.message

    def get_encrypted(self):
        return self.encoded