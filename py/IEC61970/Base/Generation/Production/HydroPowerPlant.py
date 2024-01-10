# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.VolumeFlowRate import VolumeFlowRate
from IEC61970.Base.Domain.WaterLevel import WaterLevel
from IEC61970.Base.Generation.Production.HydroGeneratingUnit import HydroGeneratingUnit
from IEC61970.Base.Generation.Production.HydroPlantStorageKind import HydroPlantStorageKind
from IEC61970.Base.Generation.Production.HydroPump import HydroPump
from IEC61970.Base.Generation.Production.Reservoir import Reservoir


class HydroPowerPlant(PowerSystemResource):
    # A hydro power station which can generate or pump. When generating, the generator turbines receive water from an
    # upper reservoir. When pumping, the pumps receive their water from a lower reservoir.
    # @created 02-Jan-2024 10:55:30 PM

    def __init__(self):
        super().__init__()
        # Water travel delay from tailbay to next downstream hydro power station.
        self.discharge_travel_delay = Seconds()  # Assuming Seconds as a class with typical values
        # The hydro plant's generating rating active power for rated head conditions.
        self.gen_rated_p = ActivePower()  # Assuming ActivePower as a class with typical values
        # The type of hydro power plant water storage.
        self.hydro_plant_storage_type = HydroPlantStorageKind.PUMPED_STORAGE  # Assuming HydroPlantStorageKind as a
        # class with typical values
        # Type and configuration of hydro plant penstock(s).
        self.penstock_type = ""  # Default value is an empty string
        # Total plant discharge capacity.
        self.plant_discharge_capacity = VolumeFlowRate()  # Assuming VolumeFlowRate as a class with typical values
        # The plant's rated gross head.
        self.plant_rated_head = Length()  # Assuming Length as a class with typical values
        # The hydro plant's pumping rating active power for rated head conditions.
        self.pump_rated_p = ActivePower()  # Assuming ActivePower as a class with typical values
        # A code1 describing the type (or absence) of surge tank that is associated with the hydro power plant.
        self.surge_tank_code = str()  # Default value is an empty string
        # The level at which the surge tank spills.
        self.surge_tank_crest_level = WaterLevel()  # Assuming WaterLevel as a class with typical values
        # The hydro pump may be a member of a pumped storage plant or a pump for distributing water.
        self.hydro_pumps = HydroPump()  # Assuming HydroPump as a class with typical values
        # Generators discharge water to or pumps are supplied water from a downstream reservoir.
        self.reservoir = Reservoir()  # Assuming Reservoir as a class with typical values
        # Generators are supplied water from or pumps discharge water to an upstream reservoir.
        self.gen_source_pump_discharge_reservoir = Reservoir()  # Assuming Reservoir as a class with typical values
        # The hydro generating unit belongs to a hydro power plant.
        self.hydro_generating_units = HydroGeneratingUnit()  # Assuming HydroGeneratingUnit as a class with typical
        # values
