# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from datetime import timedelta

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ProtectedSwitch import ProtectedSwitch


class Breaker(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking
    currents under normal circuit conditions and also making, carrying for a
    specified time, and breaking currents under specified abnormal circuit
    conditions e.g. those of short circuit.
    @author pmora
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.in_transit_time:timedelta = timedelta(0)

    def get_in_transit_time(self) -> timedelta:
        return self.in_transit_time

    def set_in_transit_time(self, new_val: timedelta) -> None:
        self.in_transit_time = new_val

