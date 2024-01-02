# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC62325.InfIEC62325.InfEnergyScheduling.TransmissionCorridor import TransmissionCorridor
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionReservation import TransmissionReservation


class TransmissionPath(IdentifiedObject):

    """An electrical connection, link, or line consisting of one or more parallel
       transmission elements between two areas of the interconnected electric systems,
       or portions thereof. TransmissionCorridor and TransmissionRightOfWay refer to
       legal aspects. The TransmissionPath refers to the segments between a
       TransmissionProvider's ServicePoints.
       @created 27-Dec-2023 3:33:47 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.avail_transfer_capabilityOptional[ActivePower] = ActivePower()  # The available transmission capability of a transmission path for the reference direction
        self.parallel_path_flagbool = False  # Flag which indicates if the transmission path is also a designated interconnection "parallel path"
        self.total_transfer_capabilityOptional[ActivePower] = ActivePower()  # The total transmission capability of a transmission path in the reference direction
        self.for_Optional[TransmissionCorridor] = TransmissionCorridor()  # A TransmissionPath is contained in a TransmissionCorridor
        self.transmission_reservationOptional[TransmissionReservation] = TransmissionReservation()
