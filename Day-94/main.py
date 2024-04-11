import time
from plyer import notification

def drink_water_reminder():
    while True:
        notification_title = "Drink Water Now!"
        notification_message = "It's time to drink water. Stay hydrated!"
        notification_timeout = 10  # Display time for the notification in seconds
        
        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=notification_timeout
        )
        
        # Wait for an hour before sending the next reminder
        time.sleep(60 * 60)  # 60 seconds * 60 minutes = 1 hour

if __name__ == "__main__":
    drink_water_reminder()
