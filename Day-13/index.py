# Strings are immutable
a = "Kajal"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("Kajal", "Komal"))
print(a.split(" "))

name = "Abhi!!!!!"
print(name.rstrip("!"))

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"
print(len(str1))
print((str1.center(50)))
print(len(str1.center(50)))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4,10))

a1 = "!!!1Kajal!! !!!! Kajal"
print(a1.count("Kajal"))

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is"))
print(str2.find("ishh"))

str3 = "WelcomeToTheConsole"
print(str3.isalnum())

str4 = "hello world"
print(str4.islower())

str5 = "We wish you a Merry Christmas\n"
print(str5)
print(str5.isprintable())

d = "            "
print(d.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())