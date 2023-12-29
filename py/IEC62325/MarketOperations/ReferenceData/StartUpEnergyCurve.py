# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.Curve import Curve


class StartUpEnergyCurve(Curve):
    """
    The energy consumption of a generating resource to complete a start-up from the
    StartUpEnergyCurve. Definition of the StartUpEnergyCurve includes, xvalue as
    the cooling time and y1value as the MW value.
    @created 28-Dec-2023 12:23:36 PM
    """

    def __init__(self) -> None:
        super().__init__()
