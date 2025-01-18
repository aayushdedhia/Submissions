class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours, minutes = divmod(total_minutes, 60)
        hours = self.hours + other.hours + extra_hours
        return Time(hours, minutes)

    def display_time(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def display_minutes(self):
        print(f"Total minutes: {self.hours * 60 + self.minutes}")

time1 = Time(2, 50)
time2 = Time(1, 20)
result = time1.add_time(time2)

result.display_time()
result.display_minutes()
