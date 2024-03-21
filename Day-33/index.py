dic = {
    344:"Kajal",
    56:"Shubham",
    678:"Zakir",
    547:"Neha"
}
print(dic[547])


info = {'name':'Kajal', 'age':22, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")


print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")