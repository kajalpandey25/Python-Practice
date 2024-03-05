import time

def greet_user():
    current_hour = int(time.strftime('%H'))
    
    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    print(f"{greeting}, Sir!")

if __name__ == "__main__":
    greet_user()
