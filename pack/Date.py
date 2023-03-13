from .Error import DateTimeError

class Date1:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.validate_date1()

    def display_date(self):
        print(f"{self.year:04}/{self.month:02}/{self.day:02}")

    def validate_date1(self):
        if not isinstance(self.year, int) or not 0 <= self.year <= 9999:
            raise DateTimeError("year", self.year, "Type between 0 to 9999")
        if not isinstance(self.month, int) or not 1 <= self.month <= 12:
            raise DateTimeError("month", self.month, "Type between 1 to 12")
        if not isinstance(self.day, int) or not 1 <= self.day <= 31:
            raise DateTimeError("day", self.day, "Type between 1 to 31")

class DateTime1(Date1):
    def __init__(self, year, month, day, hours, minutes, seconds):
        super().__init__(year, month, day)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.validate_DateTime1()

    def validate_DateTime1(self):
        super().validate_date1()
        if not isinstance(self.hours, int) or not 0 <= self.hours <= 23:
            raise DateTimeError("hours", self.hours, "Type between 0 to 23")
        if not isinstance(self.minutes, int) or not 0 <= self.minutes <= 59:
            raise DateTimeError("minutes", self.minutes, "Type between 0 to 59")
        if not isinstance(self.seconds, int) or not 0 <= self.seconds <= 59:
            raise DateTimeError("seconds", self.seconds, "Type between 0 to 59")

    def display_date(self):
        super().display_date()
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")



