# List data type

marks = [95, 98, 97, "Maths"]
# print(marks)
# print(marks[0])
# print(marks[-1])
# print(marks[0:2])
# print(marks[1:3])

# using for loop
# for score in marks:
#     print(score)

# Append operation
marks.append (99)
print(marks)

# Insert operation
marks.insert(0, (100))
print(marks)

# Find operation
print(100 in marks)
print(93 in marks)

# Find length
print(len(marks))

# using while loop

i = 0
while i < len(marks):
    print(marks[i])
    i = i+1


# marks.clear() operation
    
marks.clear()
print(marks)

