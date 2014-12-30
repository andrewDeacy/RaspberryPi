__author__ = 'Andrew'
import time
import os
import threading

#Basic alarm class for my raspberry pi program
class Alarm(threading.Thread):
        def __init__(self, hours, minutes, name): #I want to pass in name of user...
            super(Alarm, self).__init__()
            self.hours = int(hours)
            self.minutes = int(minutes)
            self.name = str(name)
            self.keepAlarmOn = True


            def turnAlarmOn(self):
                try:
                    while self.keepAlarmOn:
                        now = time.localtime()
                        if (now.tm_hour == self.hours and now.tm_minutes == self.minutes):
                            print("Time to wake up " + name + "!")
                            os.popen("alarm.mp3") #Need to find alarm sound or text to voice...
                            return
                        time.sleep(60)
                except:
                    return

            def turnAlarmOff(self):
                self.keepAlarmOn = False

#Asking user for name and alarm time...
name = input("Hey there. What's your name?")
print("Nice to meet you " + name + ".")
hour = input("Enter the hour you want to wake up at: ")
minutes = input("Enter the minute you want to wake up at: ")

#Confirming alarm:
print("You want to wake up at: {0:02}:{1:02}").format(hour, minutes)

#Initalizing alarm with user input:
alarm = Alarm(hour, minutes, name)
alarm.start()

#Waiting for alarm to trigger...
try:
    while True:
         text = str(input()) #User must type 'stop' to turn alarm off
         if text == "stop":
            alarm.turnAlarmOff()
            break
except:
    print("Error found...")
    alarm.turnAlarmOff()



