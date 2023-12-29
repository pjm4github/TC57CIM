# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class TieLine(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.side_a_sub_control_area: SubControlArea = SubControlArea()
        self.side_b_sub_control_area: SubControlArea = SubControlArea()
