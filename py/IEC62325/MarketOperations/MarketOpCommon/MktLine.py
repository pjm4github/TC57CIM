# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from IEC62325.InfIEC62325.InfEnergyScheduling.TransmissionRightOfWay import TransmissionRightOfWay
from IEC61970.Base.Wires.Line import Line


class MktLine(Line):
    # Subclass for IEC61970:Wires:Line.
    # @author mspivbe2
    # @version 1.0
    # @created 25-Dec-2023 9:21:23 PM
    def __init__(self):
        super().__init__()
        self.transmission_right_of_way = TransmissionRightOfWay()

