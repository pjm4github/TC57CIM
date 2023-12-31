# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Document import Document
from IEC61968.PaymentMetering.ConsumptionTariffInterval import ConsumptionTariffInterval
from IEC61968.PaymentMetering.TimeTariffInterval import TimeTariffInterval


class TariffProfile(Document):
    
    def __init__(self):
        super().__init__()
        self.tariff_cycle = ""
        self.consumption_tariff_intervals = ConsumptionTariffInterval()
        self.time_tariff_intervals = TimeTariffInterval()
