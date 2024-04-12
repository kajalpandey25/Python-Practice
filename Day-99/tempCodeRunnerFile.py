from win10toast import ToastNotifier
import time

REPEAT_INTERVAL = 3600  # Repeat frequency in seconds

toaster = ToastNotifier()

while True:
    toaster.show_toast("Hey Kajal, Drink water", "Hey Kajal, Drink water")
    time.sleep(REPEAT_INTERVAL)
