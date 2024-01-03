# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:37:42 2023
from typing import Optional

from IEC61968.Common.Agreement import Agreement
from IEC61968.InfIEC61968.InfLocations.LandProperty import LandProperty


class RightOfWay(Agreement):


    def __init__(self) -> None:
        # Property related information that describes the ROW's land parcel. For example,
        # it may be a deed book number, deed book page number, and parcel number.
        super().__init__()
        self.property_data = ""

        # All land properties this right of way applies to.
        self.land_properties = [LandProperty()]

