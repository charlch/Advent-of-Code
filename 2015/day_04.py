import hashlib

data = "abcdef"
data = "pqrstuv"
data = "ckczppom"
i = 0

while True:
    i+=1
    has = hashlib.md5((data+str(i)).encode()).hexdigest()
    if has.startswith("000000"):
        print(data+str(i))
        break
              
