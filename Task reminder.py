import time
from plyer import notification # installed plyer by giving the command pip install plyer.
if __name__=="__main__": # it helps in encapsulation
    while True: 
           # running a loop to push notification after a given time.
        Reminder=input("Enter that task you want to get reminded of")
        reminder_interval=int(input("Enter the time (in hrs) of the task you want to get reminded of"))
        notification.notify(title = "**Its time for your task",
         message = "Don't ignore your tasks, kindly do "+Reminder,
          timeout=10 
          # the amount of time the notfication would be displayed
         )
        time.sleep(reminder_interval*3600)