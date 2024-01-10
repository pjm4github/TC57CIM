# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Domain.CostPerVolume import CostPerVolume
from IEC61970.Base.Generation.Production.GeneratingUnit import GeneratingUnit
from IEC61970.Base.Generation.Production.HydroEnergyConversionKind import HydroEnergyConversionKind
from IEC61970.Base.Generation.Production.HydroGeneratingEfficiencyCurve import HydroGeneratingEfficiencyCurve
from IEC61970.Base.Generation.Production.PenstockLossCurve import PenstockLossCurve
from IEC61970.Base.Generation.Production.TailbayLossCurve import TailbayLossCurve


class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).
    @created 02-Jan-2024 10:55:18 PM
    """

    def __init__(self):
        super().__init__()
        # Energy conversion capability for generating.
        self.energy_conversion_capability = HydroEnergyConversionKind.GENERATOR  # Typical value used
        # The equivalent cost of water that drives the hydro turbine.
        self.hydro_unit_water_cost = CostPerVolume()  # Typical value used
        # A hydro generating unit has a tailbay loss curve.
        self.TailbayLossCurve = TailbayLossCurve()  # Typical value used
        # A hydro generating unit has an efficiency curve.
        self.HydroGeneratingEfficiencyCurves = HydroGeneratingEfficiencyCurve()  # Typical value used
        # A hydro generating unit has a penstock loss curve.
        self.PenstockLossCurve = PenstockLossCurve()  # Typical value used
