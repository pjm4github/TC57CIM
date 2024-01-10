# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Generation.Production.CostPerHeatUnit import CostPerHeatUnit
from IEC61970.Base.Generation.Production.EmissionAccount import EmissionAccount
from IEC61970.Base.Generation.Production.EmissionCurve import EmissionCurve
from IEC61970.Base.Generation.Production.FuelAllocationSchedule import FuelAllocationSchedule
from IEC61970.Base.Generation.Production.GeneratingUnit import GeneratingUnit
from IEC61970.Base.Generation.Production.HeatInputCurve import HeatInputCurve
from IEC61970.Base.Generation.Production.HeatRateCurve import HeatRateCurve
from IEC61970.Base.Generation.Production.IncrementalHeatRateCurve import IncrementalHeatRateCurve
from IEC61970.Base.Generation.Production.ShutdownCurve import ShutdownCurve
from IEC61970.Base.Generation.Production.StartupModel import StartupModel


class ThermalGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover could be a steam turbine,
    combustion turbine, or diesel engine.
    """
    
    def __init__(self):
        super().__init__()
        # Operating and maintenance cost for the thermal unit.
        self.o_m_cost = CostPerHeatUnit()  # Typical value passed to the CostPerHeatUnit constructor is None
        
        # A thermal generating unit may have a heat rate curve.
        self.heat_rate_curve = HeatRateCurve()  # Typical value passed to the HeatRateCurve constructor is None
        
        # A thermal generating unit may have one or more fuel allocation schedules.
        self.fuel_allocation_schedules = FuelAllocationSchedule()  # Typical value passed to the FuelAllocationSchedule constructor is None
        
        # A thermal generating unit may have a startup model.
        self.startup_model = StartupModel()  # Typical value passed to the StartupModel constructor is None
        
        # A thermal generating unit may have one or more emission curves.
        self.emission_curves = EmissionCurve()  # Typical value passed to the EmissionCurve constructor is None
        
        # A thermal generating unit may have a shutdown curve.
        self.shutdown_curve = ShutdownCurve()  # Typical value passed to the ShutdownCurve constructor is None
        
        # A thermal generating unit may have an incremental heat rate curve.
        self.incremental_heat_rate_curve = IncrementalHeatRateCurve()  # Typical value passed to the IncrementalHeatRateCurve constructor is None
        
        # A thermal generating unit may have one or more emission allowance accounts.
        self.emission_accounts = EmissionAccount()  # Typical value passed to the EmissionAccount constructor is None
        
        # A thermal generating unit may have a heat input curve.
        self.heat_input_curve = HeatInputCurve()  # Typical value passed to the HeatInputCurve constructor is None
