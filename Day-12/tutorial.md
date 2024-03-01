String Slicing & Operations on String: -

Length of a String =>
We can find the length of a string using len() function.

example => 
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

String as an array =>
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

example => 
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index

Slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

output =>
Apple
Pie
pleP
ApplePie

Loop through a String:
Strings are arrays and arrays are iterable. Thus we can loop through strings.

example =>
alphabets = "ABCDE"
for i in alphabets:
    print(i)

output =>
A
B
C
D
E