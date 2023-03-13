class DateTimeError(Exception):
    def __init__(self, date_time, value, message):
        self.date_time = date_time
        self.value = value
        self.message = message

    def __str__(self):
        return f"Invalid value {self.value} for {self.date_time}. {self.message}"


