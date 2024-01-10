# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Generation.Production.EmissionType import EmissionType
from IEC61970.Base.Generation.Production.EmissionValueSource import EmissionValueSource


class EmissionAccount(Curve):
    """
    Accounts for tracking emissions usage and credits for thermal generating units.
    A unit may have zero or more emission accounts, and will typically have one for
    tracking usage and one for tracking credits.
    @created 02-Jan-2024 10:52:49 PM
    """

    def __init__(self):
        super().__init__()
        # The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the
        # curve contains the unit of measure (e.g. kg) and the emissionType is the type
        # of emission (e.g. sulfer dioxide).
        self.emission_type = EmissionType.CHLORINE  # type: EmissionType
        # The source of the emission value.
        self.emission_value_source = EmissionValueSource.MEASURED  # type: EmissionValueSource
