# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.ReserveDemandCurve import ReserveDemandCurve


class ASRequirements:
    """
    Models Ancillary Service Requirements.  Describes interval for which the
    requirement is applicable.
    @created 27-Dec-2023 3:24:11 PM
    """


    def __init__(self) -> None:
        self.interval_start_time: DateTime = DateTime()
        self.reserve_demand_curve: ReserveDemandCurve = ReserveDemandCurve()
