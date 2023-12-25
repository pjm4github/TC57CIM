# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ReadingType import ReadingType
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.Charge import Charge
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.TimeTariffInterval import TimeTariffInterval


class ConsumptionTariffInterval:
    
    def __init__(self):
        self.sequence_number = 0
        self.start_value = 0.0
        self.tou_tariff_intervals = TimeTariffInterval()
        self.charges = Charge()
        self.reading_type = ReadingType()

