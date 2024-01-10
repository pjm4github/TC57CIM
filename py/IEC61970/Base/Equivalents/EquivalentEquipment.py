from IEC61970.Base.Core.ConductingEquipment import ConductingEquipment


class EquivalentEquipment(ConductingEquipment):
    """
    The class represents equivalent objects that are the result of a network
    reduction. The class is the base for equivalent objects of different types.
    @created 07-Jan-2024 9:59:33 PM
    """
    def __init__(self):
        ConductingEquipment.__init__(self)
