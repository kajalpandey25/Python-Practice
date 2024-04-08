import pyttsx3

names = ["Kajal", "Monika", "Alia"]

engine = pyttsx3.init()

for name in names:
    engine.say(f"Shoutout to {name}")

engine.runAndWait()
