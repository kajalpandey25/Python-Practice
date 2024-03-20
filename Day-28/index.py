letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Kajal"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.0999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())

print(type(f"{2*30}"))

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Kajal'  
age = 22 
print(f"Hello, My name is {name} and I'm {age} years old.")