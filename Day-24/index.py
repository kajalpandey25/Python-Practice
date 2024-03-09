tup = (1,2,76,362,34, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])
print(tup[-2])


if 362 in tup:
    print("Yes 362 is present in this tuple")
else:
    print("No 362 is absent in this tuple")


tup2 = tup[1:4]
print(tup2)