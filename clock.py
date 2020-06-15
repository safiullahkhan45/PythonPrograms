import time, os


class Clock:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def sethours(self, hours):
        if hours > 23:
            hours = int(input("Invalid input. enter a valid value between 0 and 23."))
        self.hours = hours

    def setminutes(self, minutes):
        if minutes > 59:
            minutes = int(input("Invalid input. enter a valid value between 0 and 59."))
        self.minutes = minutes

    def setseconds(self, seconds):
        if seconds > 59:
            seconds = int(input("Invalid input. enter a valid value between 0 and 59."))
        self.seconds = seconds

    def gethours(self):
        return self.hours

    def getminutes(self):
        return self.minutes

    def getseconds(self):
        return self.seconds

    def increment_time(self):
        self.seconds += 1
        if self.seconds > 59:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > 59:
            self.minutes = 0
            self.hours += 1
        if self.hours > 23:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0

    def display_time(self):
        for i in range(123455):
            self.increment_time()
            print("{}:{}:{}".format(self.hours, self.minutes, self.seconds))
            os.system('clear')
            time.sleep(1)


obj = Clock(12, 15, 16)

obj.display_time()
