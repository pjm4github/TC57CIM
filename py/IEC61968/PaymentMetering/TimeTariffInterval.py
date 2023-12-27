# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.PaymentMetering.Charge import Charge
from IEC61970.Base.Domain.Time import Time


class TimeTariffInterval:
    def __init__(self):
        self.sequence_number =0
        self.start_time = Time()
        self.charges = Charge()
