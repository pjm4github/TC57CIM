# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class ControlAreaDesignation:
    """
    Indicates Control Area associated with self-schedule.
    @created 28-Dec-2023 1:03:56 PM
    """

    def __init__(self) -> None:
        self.attained: YesNo.NO
        self.native: YesNo.NO
        self.sub_control_area: SubControlArea = SubControlArea()
        self.registered_resource: RegisteredResource = RegisteredResource()
