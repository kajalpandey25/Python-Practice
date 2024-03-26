questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language is known for its use in building scalable and high-performance backend systems?", "JavaScript","PHP","Python","C++","None",3
  ],
  [
    "What language is frequently used for game development, especially with the Unity game engine?", "Python", "C#", "Ruby" "Java", "None", 2
  ],
  [
    "What language is often used for data analysis, machine learning, and scientific computing?", "JavaScript", "C#", "Python", "php", "None", 3
    
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")