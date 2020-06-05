#
# Select a value of e from 3,5,17,257,65537 (easy operations)
# while p mod e = 1
#   p = genprime(k/2)
#
# while q mode e = 1:
#   q = genprime(k - k/2)
#
# n = p*q
# L = (p-1)(q-1)
# d = modinv(e, L)
# return (n,e,d)

from random import randrange, getrandbits


class rsa:
    def __init__(self, e=4, k=5):
        self.e = [3, 5, 17, 257, 65537][e]
        self.k = [128, 256, 1024, 2048, 3072, 4096][k]

    def is_prime(self, n, tests=128):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        for _ in range(tests):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    def genprime(self, length=1024):
        p = 1
        while len(bin(p)) - 2 != length:
            p = list(bin(getrandbits(length)))
            p = int(''.join(p[0:2] + ['1', '1'] + p[4:]), 2)
        p += 1 if p % 2 == 0 else 0

        ip = self.is_prime(p)
        while not ip:
            p += 2
            ip = self.is_prime(p)
        return p

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - b // a * y, y

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def get_creds(self, e, k):
        n = 0
        while len(bin(int(n))) - 2 != k:
            p = self.genprime(int(k / 2))
            while pow(p, 1, e) == 1:
                p = self.genprime(int(k / 2))
            q = self.genprime(k - int(k / 2))
            while pow(q, 1, e) == 1 and q == p:
                q = self.genprime(k - int(k / 2))
            n = p * q
            l = (p - 1) * (q - 1)
            d = self.modinv(e, l)
        return p, q, (d, e, n)

    def get_keys(self):
        p, q, creds = self.get_creds(self.e, self.k)
        return creds

    def save_keys(self, filename="keys.k"):
        keys = self.get_keys()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(keys[0]) + "\n" + str(keys[1]) + "\n" + str(keys[2]))

    def load_keys(self, filename="keys.k"):
        with open(filename, "r", encoding="utf-8") as file:
            f = file.read().split("\n")
            d = int(f[0])
            e = int(f[1])
            n = int(f[2])
        return d, e, n

    def encrypt(self, ke, i):
        e, n = ke
        cipher = pow(i, e, n)
        return cipher

    def decrypt(self, kd, cipher):
        d, n = kd
        plain = pow(cipher, d, n)
        return plain
