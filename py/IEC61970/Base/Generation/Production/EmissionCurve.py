# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Generation.Production.Emission import Emission
from IEC61970.Base.Generation.Production.EmissionType import EmissionType


class EmissionCurve(Curve):
    """
    Relationship between the unit's emission rate in units of mass per hour (Y-axis)
    and output active power (X-axis) for a given type of emission. This curve
    applies when only one type of fuel is being burned.
    @created 02-Jan-2024 10:53:01 PM
    """

    def __init__(self):
        super().__init__()
        # The emission content per quantity of fuel burned.
        self.emission_content = Emission()  # Typical value as an argument (e.g. 0.0)
        
        # The type of emission, which also gives the production rate measurement unit.
        # The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the
        # emissionType is the type of emission (e.g. sulfur dioxide).
        self.emission_type = EmissionType.CARBON_DIOXIDE  # Typical value as an argument (e.g. EmissionType.SULFUR_DIOXIDE)
        
        # Flag is set to true when output is expressed in net active power.
        self.is_net_gross_p = False  # Typical value as an argument (e.g. True)
