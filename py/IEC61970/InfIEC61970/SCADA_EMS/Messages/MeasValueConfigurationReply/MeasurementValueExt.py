# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:18:27 2024
# Class to represent MeasurementValueExt
from IEC61970.InfIEC61970.SCADA_EMS.Meas.TimeAccuracy import TimeAccuracy


class MeasurementValueExt:
    """
    @author SELAOST1
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """

    def __init__(self):
        super().__init__()
        self.time_accuracy = TimeAccuracy.T1SEC  # typical value as argument for the TimeAccuracy class method call
