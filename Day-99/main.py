from plyer import notification
import time

REPEAT_INTERVAL = 3600 # Repeat frequency in seconds (1 hour)

while True:
    notification.notify(
        title="Drink Water Reminder",
        message="Hey there! Remember to drink some water.",
        timeout=10  # Notification will disappear after 10 seconds
    )
    time.sleep(REPEAT_INTERVAL)
