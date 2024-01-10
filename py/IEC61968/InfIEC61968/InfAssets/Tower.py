# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61968.Assets.Structure import Structure
from IEC61968.InfIEC61968.InfAssets.TowerConstructionKind import TowerConstructionKind


class Tower(Structure):
    """
    Tower asset. Dimensions of the Tower are specified in associated DimensionsInfo class.
    When used for planning purposes, a transmission tower carrying two 3-phase
    circuits will have 2 instances of Connection, each of which will have 3
    MountingPoint instances, one for each phase all with coordinates relative to a
    common origin on the tower. (It may also have a 3rd Connection with a single
    MountingPoint for the Neutral line).
    """

    def __init__(self) -> None:
        super().__init__()
        """
        Construction structure on the tower.
        """
        self.construction_kind = TowerConstructionKind.SUSPENSION
