from random import randint

def genrnd():
    x = [randint(0,100) for i in range(50)]
    return x
print(genrnd())