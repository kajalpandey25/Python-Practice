What are strings?

In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

example =>
name = "Harry"
print("Hello, " + name) 

Multiline Strings =>

If our string has multiple lines, we can create them like this:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

Accessing Characters of a String =>

In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.

print(name[0])
print(name[1])

Looping through the string
We can loop through strings using a for loop like this:

for character in name:
    print(character)

Above code prints all the characters in the string name one by one!