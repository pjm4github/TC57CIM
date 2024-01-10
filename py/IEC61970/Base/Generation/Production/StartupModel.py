# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.CostPerEnergyUnit import CostPerEnergyUnit
from IEC61970.Base.Domain.CostRate import CostRate
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Hours import Hours
from IEC61970.Base.Domain.Money import Money
from IEC61970.Base.Generation.Production.HeatRate import HeatRate
from IEC61970.Base.Generation.Production.StartIgnFuelCurve import StartIgnFuelCurve
from IEC61970.Base.Generation.Production.StartMainFuelCurve import StartMainFuelCurve
from IEC61970.Base.Generation.Production.StartRampCurve import StartRampCurve


class StartupModel(IdentifiedObject):
    """
    Unit start up characteristics depending on how long the unit has been off line.
    @created 02-Jan-2024 10:58:43 PM
    """

    def __init__(self):
        super().__init__()
        self.fixed_maint_cost = CostRate()  # Fixed maintenance cost.
        self.hot_standby_heat = HeatRate()  # The amount of heat input per time unit required for hot standby operation.
        self.incremental_maint_cost = CostPerEnergyUnit()  # Incremental maintenance cost.
        self.minimum_down_time = Hours()  # The minimum number of hours the unit must be down before restart.
        self.minimum_run_time = Hours()  # The minimum number of hours the unit must be operating before being
        # allowed to shut down.
        self.risk_factor_cost = Money()  # The opportunity cost associated with the return in monetary unit. This
        # represents the restart's "share" of the unit depreciation and risk of an event which would damage the unit.
        self.startup_cost = Money()  # Total miscellaneous start up costs.
        self.startup_date = DateTime()  # The date and time of the most recent generating unit startup.
        self.startup_priority = 0  # Startup priority within control area where lower numbers indicate higher
        # priorities. More than one unit in an area may be assigned the same priority.
        self.stby_aux_p = ActivePower()  # The unit's auxiliary active power consumption to maintain standby mode.
        self.start_ramp_curve = StartRampCurve()  # The unit's startup model may have a startup ramp curve.
        self.start_ign_fuel_curve = StartIgnFuelCurve()  # The unit's startup model may have a startup ignition fuel
        # curve.
        self.start_main_fuel_curve = StartMainFuelCurve()  # The unit's startup model may have a startup main fuel
        # curve.
