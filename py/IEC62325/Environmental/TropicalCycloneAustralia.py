# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.Environmental.Cyclone import Cyclone


class TropicalCycloneAustralia(Cyclone):
    """
    A tropical cyclone, a subtype of cyclone that forms to the east of 90 E in the
    Southern Hemisphere whose intensity is measured by the Australian tropical
    cyclone intensity scale.
    @author ppbr003
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        """
        Strength of tropical cyclone during the time interval, based on Australian
        Bureau of Meteorology Category System where:
        1 - tropical cyclone, with typical gusts over flat land 90-125 km/h
        2 - tropical cyclone, with typical gusts over flat land 125-164 km/h
        3 - severe tropical cyclone, with typical gusts over flat land 165-224 km/h
        4 - severe tropical cyclone, with typical gusts over flat land 225-279 km/h
        5 - severe tropical cyclone, with typical gusts over flat land greater than
        280 km/h.
        """
        self.category = 1

