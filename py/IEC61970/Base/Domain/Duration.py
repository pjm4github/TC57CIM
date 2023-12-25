# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
import re
import time
from typing import Any


class Duration:
    """
    Duration as "PnYnMnDTnHnMnS" which conforms to ISO 8601,
    where nY expresses a number of years, nM a number of months,
    nD a number of days. The letter T separates the date expression
    from the time expression and, after it, nH identifies a number of hours, nM a number of minutes and nS a
    number of seconds. The number of seconds could be
    expressed as a decimal number, but all other numbers are integers.
    """
    def __init__(self) -> None:
        self.years = 0
        self.months = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0.0
        self._duration: time.time_ns = 0

    @property
    def duration(self):
        return str(self)

    @duration.setter
    def duration(self, value: [float, str]):
        if type(value, str):
            # convert it this way
            # Regular expression to match the pattern
            pattern = r'(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?(?:(\d+)H)?(?:(\d+)M)?(\d+\.\d+S)?'

            # Use re.search to find the matches
            match = re.search(pattern, value)

            # Extract components
            self.years = int(match.group(1)) if match.group(1) else 0
            self.months = int(match.group(2)) if match.group(2) else 0
            self.days = int(match.group(3)) if match.group(3) else 0
            self.hours = int(match.group(4)) if match.group(4) else 0
            self.minutes = int(match.group(5)) if match.group(5) else 0
            self.seconds = float(match.group(6)) if match.group(6) else 0.0
            total_seconds = (self.years * 365 * 24 * 60 * 60) + \
                            (self.months * 30 * 24 * 60 * 60) + \
                            (self.days * 24 * 60 * 60) + \
                            (self.hours * 60 * 60) + \
                            (self.minutes * 60) + \
                            self.seconds
            leap_years = self.years // 4 - self.years // 100 + self.years // 400
            total_seconds += leap_years * 24 * 60 * 60
            self._duration = int(total_seconds * 1e9)
        else:
            # convert it as a float (in seconds)

            total_seconds = value/1e-9
            self._duration = value

            # Calculate years, months, days, hours, minutes, and seconds
            seconds_in_minute = 60
            seconds_in_hour = 3600
            seconds_in_day = 86400
            seconds_in_month = 30.44 * seconds_in_day  # Approximate average month length

            self.years = total_seconds // (365 * seconds_in_day)
            total_seconds %= (365 * seconds_in_day)

            self.months = total_seconds // seconds_in_month
            total_seconds %= seconds_in_month

            self.days = total_seconds // seconds_in_day
            total_seconds %= seconds_in_day

            self.hours = total_seconds // seconds_in_hour
            total_seconds %= seconds_in_hour

            self.minutes = total_seconds // seconds_in_minute
            total_seconds %= seconds_in_minute

            self.seconds = total_seconds

    def __str__(self):
        return f"P{self.years}Y" \
                f"{self.months}M" \
                f"{self.days}DT" \
                f"{self.hours}H"\
                f"{self.minutes}M" \
                f"{self.seconds}S"
