# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# environmental.py
from IEC62325.Environmental.EnvironmentalInformation import EnvironmentalInformation


# Observed (actual non-forecast) values sets and/or phenomena characteristics.
# @author mcmorran
# @version 1.0
# @created 25-Dec-2023 9:21:23 PM

class Observation(EnvironmentalInformation):
    def __init__(self):
        super().__init__()
