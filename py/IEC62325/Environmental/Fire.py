# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Importing from local package
from IEC62325.Environmental.GeosphericPhenomenon import GeosphericPhenomenon


# Fire class representing a fire phenomenon
class Fire(GeosphericPhenomenon):
    """
    A fire, often uncontrolled, covering an area of land which typically contains
    combustible vegetation. Associated location information is assumed to describe
    the total area burned as of a specified time.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """
    # Constructor for Fire class
    def __init__(self):
        super().__init__()
