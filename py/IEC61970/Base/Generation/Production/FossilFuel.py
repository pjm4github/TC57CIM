# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Generation.Production.CostPerHeatUnit import CostPerHeatUnit
from IEC61970.Base.Generation.Production.FuelAllocationSchedule import FuelAllocationSchedule
from IEC61970.Base.Generation.Production.FuelType import FuelType
from IEC61970.Base.Generation.Production.ThermalGeneratingUnit import ThermalGeneratingUnit


class FossilFuel(IdentifiedObject):
    """
    The fossil fuel consumed by the non-nuclear thermal generating unit. For
    example, coal, oil, gas, etc. This is a specific fuel that the generating
    unit can consume.
    @created 02-Jan-2024 10:53:13 PM
    """

    def __init__(self):
        super().__init__()
        # The type of fossil fuel, such as coal, oil, or gas.
        self.fossil_fuel_type = FuelType.GAS
        # The cost in terms of heat value for the given type of fuel.
        self.fuel_cost = CostPerHeatUnit()
        # The cost of fuel used for economic dispatching which includes: fuel cost, 
        # transportation cost, and incremental maintenance cost.
        self.fuel_dispatch_cost = CostPerHeatUnit()
        # The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed.
        self.fuel_eff_factor = PU()
        # Handling and processing cost associated with this fuel.
        self.fuel_handling_cost = CostPerHeatUnit()
        # The amount of heat per weight (or volume) of the given type of fuel.
        self.fuel_heat_content = 0.0
        # Relative amount of the given type of fuel, when multiple fuels are being consumed.
        self.fuel_mixture = PerCent()
        # The fuel's fraction of pollution credit per unit of heat content.
        self.fuel_sulfur = PU()
        # The active power output level of the unit at which the given type of fuel is switched on.
        # This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high 
        # active power output levels.
        self.high_breakpoint_p = ActivePower()
        # The active power output level of the unit at which the given type of fuel is switched off.
        # This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low 
        # active power output levels.
        self.low_breakpoint_p = ActivePower()
        # A fuel allocation schedule must have a fossil fuel.
        self.fuel_allocation_schedules = FuelAllocationSchedule()
        # A thermal generating unit may have one or more fossil fuels.
        self.thermal_generating_unit = ThermalGeneratingUnit()
