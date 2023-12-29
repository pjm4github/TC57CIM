# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.RealEnergy import RealEnergy
from IEC62325.MarketOperations.ReferenceData.RegisteredGenerator import RegisteredGenerator


class UnitInitialConditions(IdentifiedObject):
    """
    Resource status at the end of a given clearing period.
    @created 27-Dec-2023 3:34:08 PM
    """

    def __init__(self) -> None:
        """
        Cumulative energy production over trading period.
        """
        super().__init__()
        self.cum_energy: Optional[RealEnergy] = RealEnergy()

        """
        Cumulative number of status changes of the resource.
        """
        self.cum_status_changes: Optional[int] = 0

        """
        Number of start ups in the operating day until the end of the previous hour.
        """
        self.number_of_startups: Optional[int] = 0

        """
        'true' if the GeneratingUnit is currently On-Line
        """
        self.online_status: Optional[bool] = False

        """
        Resource MW output at the end of previous clearing period.
        """
        self.resource_mw: Optional[ActivePower] = ActivePower()

        """
        Resource status at the end of previous clearing period:
        0 - off-line
        1 - on-line production
        2 - in shutdown process
        3 - in startup process
        """
        self.resource_status: Optional[int] = 0

        """
        Time and date for resourceStatus
        """
        self.status_date: Optional[DateTime] = DateTime()

        """
        Time in market trading intervals the resource is in the state as of the end of
        the previous clearing period.
        """
        self.time_in_status: Optional[float] = 0.0

        """
        Time interval
        """
        self.time_interval: Optional[DateTime] = DateTime()

        self.generating_unit: Optional[RegisteredGenerator] = RegisteredGenerator()
