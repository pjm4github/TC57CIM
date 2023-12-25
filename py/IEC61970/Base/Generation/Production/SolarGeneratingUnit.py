# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:36:32 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.GeneratingUnit import GeneratingUnit


class SolarGeneratingUnit(GeneratingUnit):
    """
    A solar thermal generating unit, connected to the grid by means of a rotating
    machine. This class does not represent photovoltaic (PV) generation.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:29 PM
    """

    def __init__(self) -> None:
        super().__init__()

