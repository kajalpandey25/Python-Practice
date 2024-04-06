import time

def usingWhile():
    i = 0
    while i<50000:
        i = i + 1
        print(i)

def usingFor():
        for i in range(50000):
             print(i)  

init = time.time()
usingFor()
print(time.time() - init)
init = time.time()
usingWhile()
print(time.time() - init)               
