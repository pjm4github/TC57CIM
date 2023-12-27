# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.Environmental.Cyclone import Cyclone


class Hurricane(Cyclone):
    """
    A hurricane, a subtype of cyclone occurring in the North Atlantic Ocean or
    North-eastern Pacific Ocean whose intensity is measured using the Saffir-
    Simpson Hurricane Scale.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        """
        The hurricane's category during the time interval, using Saffir-Simpson
        Hurricane Wind Scale, a 1 to 5 rating based on a hurricane's sustained
        wind speed.
        """
        self.category = 0
