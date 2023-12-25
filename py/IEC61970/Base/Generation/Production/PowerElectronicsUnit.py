# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:36:32 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower


class PowerElectronicsUnit(Equipment):
    """
    A generating unit or battery or aggregation that connects to the AC network
    using power electronics rather than rotating machines.
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.max_p: ActivePower = ActivePower()
        """Maximum active power limit. This is the maximum (nameplate) limit for the unit."""

        self.min_p: ActivePower = ActivePower()
        """Minimum active power limit. This is the minimum (nameplate) limit for the unit."""
