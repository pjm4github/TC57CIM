# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from IEC61970.Base.Meas.IOPoint import IOPoint
from IEC61970.Base.Meas.MeasurementValueSource import MeasurementValueSource


class IOPointSource(MeasurementValueSource):
    def __init__(self) -> None:
        super().__init__()
        self.io_point: IOPoint = IOPoint()
    
