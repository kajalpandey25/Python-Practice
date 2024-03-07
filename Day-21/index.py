# def average(a, b, c=1):
#     print("The average is ", (a+b+c)/2)


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum / len(numbers))
    return sum / len(numbers)
# average(4,6) 
# average(b=9)  

c = average(5,6, 7,1)
print(c)


# default argument
# def name(fname, mname = "Kumari", lname = "Pandey"):
#     print("Hello,", fname, mname, lname)

# name("Kajal")


# keyword argument
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Kumari", lname = "Pandey", fname = "Kajal")


# Required argument
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Kajal", "Sonam")



# Variable-length arguments
# def name(*name):
#     # print(type(name))
#     print("Hello,", name[0], name[1], name[2])

# name("Abhi", "Khushi", "Sona")


# Keyword Arbitrary Arguments
# def name(**name):
#     # print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Kumari", lname = "Pandey", fname = "Komal")



# return Statement
# def name(fname, mname, lname):
#     return "Hello, " + fname + " " + mname + " " + lname

# print(name("James", "Buchanan", "Barnes"))