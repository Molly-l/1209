import hashlib
hash = hashlib.md5()
hash.update('1*1*1*1'.encode())
print(hash.hexdigest())
