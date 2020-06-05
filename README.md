# PyRSA
RSA implemention in Python that just uses random module.

## Methods
The module has the following methods:

```python
encryption = rsa(e, k)
```

being ```e``` the encryption/public key and being ```k``` the final ```n``` bit length.
These values are defined in ```python __init__``` to be used by the automated generation methods.

```python
encryption.get_creds(e, k)
```

being ```e``` the encryption/public key and being ```k``` the final ```n``` bit length.
Returns ```p, q``` (2 prime numbers of k/2 and k - k/2 length used to generate n (p*q)), ```(d, e, n)``` as a single argument, being ```d``` the decryption/private key, ```e``` the encryption/public and ```n``` the module being used in the encryption/decryption.


```python
encryption.get_keys()
```

Returns  ```(d, e, n)``` as a single argument, being ```d``` the decryption/private key, ```e``` the encryption/public and ```n``` the modulus being used in the encryption/decryption.


```python
encryption.save_keys(filename="keys.k")
```

Saves decryption/private key, encryption/public key, and the operation modulus split by line in ```filename```.

```python
encryption.load_keys(filename="keys.k")
```

Loads decryption/private key, encryption/public key, and the operation modulus in ```filename```.
Returns  ```(d, e, n)``` as a single argument, being ```d``` the decryption/private key, ```e``` the encryption/public and ```n``` the modulus being used in the encryption/decryption.

```python
encryption.encrypt(ke, i)
```

Being ```ke``` equivalent to ```(e, n)``` and ```i``` the integer to be encrypted.
Returns the RSA encrypted i.

```python
encryption.decrypt(kd, cipher)
```

Being ```kd``` equivalent to ```(d, n)``` and ```cipher``` the RSA encrypted integer to be decrypted.
Returns the RSA decrypted cipher.
