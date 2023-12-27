# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC61970.Base.Domain.Minutes import Minutes


class EndDeviceTiming:
    
    def __init__(self):
        self.duration = Minutes()
        self.duration_indefinite = False
        self.interval = DateTimeInterval()
        self.randomisation = None
