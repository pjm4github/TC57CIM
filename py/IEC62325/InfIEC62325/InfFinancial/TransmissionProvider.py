# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:12:35 2023
from IEC61968.Common.Organisation import Organisation


class TransmissionProvider(Organisation):
    """
    Provider of  the transmission capacity (interconnecting wires between
    Generation and Consumption) required  to fulfill and Energy Transaction's
    energy exchange. Posts information for transmission paths and
    AvailableTransmissionCapacities  on a reservation node.  Buys and sells its
    products and services on the same reservation node.
    @created 27-Dec-2023 3:11:39 PM
    """
    def __init__(self) -> None:
        super().__init__()
