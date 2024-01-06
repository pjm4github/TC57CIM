# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:30:57 2024
from IEC61970.Base.LoadModel.EnergyArea import EnergyArea
from IEC61970.Base.LoadModel.SubLoadArea import SubLoadArea


class LoadArea(EnergyArea):
    """
    The class is the root or first level in a hierarchical structure for grouping
    of loads for the purpose of load flow load scaling.
    @created 03-Jan-2024 10:44:40 PM
    """

    def __init__(self):
        super().__init__()
        # The SubLoadAreas in the LoadArea.
        self.sub_load_areas = SubLoadArea()
