from IEC61970.Base.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from IEC61970.Base.Equivalents.EquivalentEquipment import EquivalentEquipment


class EquivalentNetwork(ConnectivityNodeContainer):
    """
    A class that represents an external meshed network that has been reduced to an
    electrically equivalent model. The ConnectivityNodes contained in the
    equivalent are intended to reflect internal nodes of the equivalent.
    Created: 07-Jan-2024 10:00:15 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.equivalent_equipments = EquivalentEquipment()  # Placeholder for associated reduced equivalents (EquivalentEquipment)
        # Assuming EquivalentEquipment is a previously defined class
        # If EquivalentEquipment is not defined, this will raise an error and needs to be implemented
