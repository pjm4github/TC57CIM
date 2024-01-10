from IEC61970.Base.Wires.RegulatingControl import RegulatingControl
from IEC61970.InfIEC61970.InfSIPS.ProtectiveAction import ProtectiveAction


class ProtectiveActionRegulation(ProtectiveAction):
    """
    Protective action to change regulation to Equipment.
    @author sveinols
    @version 1.0
    @created 02-Jan-2024 9:34:17 PM
    """

    def __init__(self):
        super().__init__()
        self.is_regulating = True  # If true the regulator is put in-service, otherwise out-of-service (no regulation).

        self.target_value = 0.0  # The target value specified the new case input for the regulator.  The value has
        # the units appropriate to the mode attribute. The protective action does not
        # change the mode attribute.
        self.regulating_control = RegulatingControl()
