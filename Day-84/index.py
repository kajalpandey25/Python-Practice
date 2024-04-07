import time

# time.time()


def usingWhile():
    i = 0
    while i<5000:
        i = i + 1
        print(i)

def usingFor():
        for i in range(5000):
             print(i)  

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)   
print(t1)            


# time.sleep()

print(4)
time.sleep(3)
print("This is printed after 3 seconds")


# time.strftime()

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time) 