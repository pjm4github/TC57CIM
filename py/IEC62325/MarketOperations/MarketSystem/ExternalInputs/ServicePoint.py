# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionPath import TransmissionPath
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionReservation import TransmissionReservation


class ServicePoint(IdentifiedObject):
    """
    The defined termination points of a transmission path. Service points are
    defined from the viewpoint of the transmission service. Each service point is
    contained within (or on the boundary of) an interchange area. A service point
    is source or destination of a transaction.
    @created 27-Dec-2023 3:32:07 PM
    """

    def __init__(self) -> None:
        super().__init__()
        # * A transmission path has a "point-of-receipt" service point
        self.POR_transmission_path: TransmissionPath = TransmissionPath()
        #  * A transmission path has a "point-of-delivery" service point
        self.POD_transmission_path: TransmissionPath = TransmissionPath()
        self.source_reservation: TransmissionReservation = TransmissionReservation()
        self.sink_reservation: TransmissionReservation = TransmissionReservation()
