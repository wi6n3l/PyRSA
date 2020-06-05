from rsa import rsa

encryption = rsa(k=5)
encryption.save_keys()
keys = encryption.load_keys()
#keys = encryption.get_keys()
d = keys[0]
e = keys[1]
n = keys[2]
n_length = len(bin(int(n)))
a = encryption.encrypt((e, n), 1337)
print(a)
print(encryption.decrypt((d, n), a))
