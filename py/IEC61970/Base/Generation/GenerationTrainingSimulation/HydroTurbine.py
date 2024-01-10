from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.RotationSpeed import RotationSpeed
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Generation.GenerationTrainingSimulation.PrimeMover import PrimeMover
from IEC61970.Base.Generation.GenerationTrainingSimulation.TurbineType import TurbineType


class HydroTurbine(PrimeMover):
    """
    A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    Created: 02-Jan-2024 11:05:55 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.gate_rate_limit = 0.0  # Gate rate limit
        self.gate_upper_limit = PU()  # Gate upper limit
        self.max_head_max_p = ActivePower()  # Maximum efficiency active power at maximum head conditions
        self.min_head_max_p = ActivePower()  # Maximum efficiency active power at minimum head conditions
        self.speed_rating = RotationSpeed()  # Rated speed in number of revolutions
        self.speed_regulation = PU()  # Speed regulation
        self.transient_droop_time = Seconds()  # Transient droop time constant
        self.transient_regulation = PU()  # Transient regulation
        self.turbine_rating = ActivePower()  # Rated turbine active power
        self.turbine_type = TurbineType()  # Type of turbine
        self.water_starting_time = Seconds()  # Water starting time
        # Assuming PrimeMover, Float, PU, ActivePower, RotationSpeed, Seconds, and TurbineType are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
