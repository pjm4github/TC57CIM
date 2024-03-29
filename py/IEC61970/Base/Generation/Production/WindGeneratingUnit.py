from IEC61970.Base.Generation.Production.GeneratingUnit import GeneratingUnit
from IEC61970.Base.Generation.Production.WindGenUnitKind import WindGenUnitKind


class WindGeneratingUnit(GeneratingUnit):
    """
    A wind driven generating unit, connected to the grid by means of a rotating
    machine. May be used to represent a single turbine or an aggregation.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self):
        super().__init__()
        self.wind_gen_unit_type: WindGenUnitKind = WindGenUnitKind.ONSHORE
