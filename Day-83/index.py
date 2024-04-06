import pyttsx3

def pronounce_names(names):
    engine = pyttsx3.init()

    for name in names:
        engine.say(f"Shoutout to {name}")

    engine.runAndWait()

# Example list of names
l = ["Rahul", "Nishant", "Harry"]

# Pronounce the names
pronounce_names(l)
