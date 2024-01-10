from IEC61970.Base.AuxiliaryEquipment.AuxiliaryEquipment import AuxiliaryEquipment


class FaultIndicator(AuxiliaryEquipment):
    """
    A FaultIndicator is typically only an indicator (which may or may not be
    remotely monitored), and not a piece of equipment that actually initiates a
    protection event. It is used for FLISR (Fault Location, Isolation and
    Restoration) purposes.
    Created: 07-Jan-2024 9:57:42 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
