# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Volume import Volume
from IEC61970.Base.Domain.WaterLevel import WaterLevel
from IEC61970.Base.Generation.Production.InflowForecast import InflowForecast
from IEC61970.Base.Generation.Production.LevelVsVolumeCurve import LevelVsVolumeCurve
from IEC61970.Base.Generation.Production.TargetLevelSchedule import TargetLevelSchedule


class Reservoir(PowerSystemResource):
    """
    A water storage facility within a hydro system, including ponds, lakes, lagoons, and rivers.
    The storage is usually behind some type of dam.
    @created 02-Jan-2024 10:57:32 PM
    """

    def __init__(self):
        super().__init__()
    
        # Storage volume between the full supply level and the normal minimum operating level.
        self.active_storage_capacity = Volume()  # assume Volume as the class method call

        # The reservoir's energy storage rating in energy for given head conditions.
        self.energy_storage_rating = 0.0  # assume Float as the class method call

        # Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.
        self.full_supply_level = WaterLevel()  # assume WaterLevel as the class method call

        # Total capacity of reservoir.
        self.gross_capacity = Volume()  # assume Volume as the class method call

        # Normal minimum operating level below which the penstocks will draw air.
        self.normal_min_operate_level = WaterLevel()  # assume WaterLevel as the class method call

        # River outlet works for riparian right releases or other purposes.
        self.river_outlet_works = str()

        # The spillway water travel delay to the next downstream reservoir.
        self.spill_travel_delay = Seconds()  # assume Seconds as the class method call

        # The flow capacity of the spillway in cubic meters per second.
        self.spillway_capacity = 0.0  # assume Float as the class method call

        # The length of the spillway crest.
        self.spillway_crest_length = Length()  # assume Length as the class method call

        # Spillway crest level above which water will spill.
        self.spillway_crest_level = WaterLevel()  # assume WaterLevel as the class method call

        # Type of spillway gate, including parameters.
        self.spillway_gate_type = str()

        # A reservoir may spill into a downstream reservoir.
        self.spills_into_reservoirs = Reservoir()

        # A reservoir may have a level versus volume relationship.
        self.level_vs_volume_curves = LevelVsVolumeCurve()

        # A reservoir may have a "natural" inflow forecast.
        self.inflow_forecasts = InflowForecast()

        # A reservoir may have a water level target schedule.
        self.target_level_schedule = TargetLevelSchedule()

