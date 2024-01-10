from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Generation.GenerationTrainingSimulation.BoilerControlMode import BoilerControlMode
from IEC61970.Base.Generation.GenerationTrainingSimulation.SteamSupply import SteamSupply


class FossilSteamSupply(SteamSupply):
    """
    Fossil fueled boiler (e.g., coal, oil, gas).
    Created: 02-Jan-2024 11:05:29 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.aux_power_versus_frequency = PU()  # Off nominal frequency effect on auxiliary real power
        self.aux_power_versus_voltage = PU()  # Off nominal voltage effect on auxiliary real power
        self.boiler_control_mode = BoilerControlMode()  # The control mode of the boiler
        self.control_error_bias_p = 0.0  # Active power error bias ratio
        self.control_ic = 0.0  # Integral constant
        self.control_pc = 0.0  # Proportional constant
        self.control_peb = 0.0  # Pressure error bias ratio
        self.control_ped = PU()  # Pressure error deadband
        self.control_tc = 0.0  # Time constant
        self.feed_water_ig = 0.0  # Feedwater integral gain ratio
        self.feed_water_pg = 0.0  # Feedwater proportional gain ratio
        self.feed_water_tc = Seconds()  # Feedwater time constant ratio
        self.fuel_demand_limit = PU()  # Fuel demand limit
        self.fuel_supply_delay = Seconds()  # Fuel delay
        self.fuel_supply_tc = Seconds()  # Fuel supply time constant
        self.max_error_rate_p = 0.0  # Active power maximum error rate limit
        self.mech_power_sensor_lag = Seconds()  # Mechanical power sensor lag
        self.min_error_rate_p = 0.0  # Active power minimum error rate limit
        self.pressure_ctrl_dg = 0.0  # Pressure control derivative gain ratio
        self.pressure_ctrl_ig = 0.0  # Pressure control integral gain ratio
        self.pressure_ctrl_pg = 0.0  # Pressure control proportional gain ratio
        self.pressure_feedback = 0  # Pressure feedback indicator
        self.super_heater1_capacity = 0.0  # Drum/primary superheater capacity
        self.super_heater2_capacity = 0.0  # Secondary superheater capacity
        self.super_heater_pipe_pd = 0.0  # Superheater pipe pressure drop constant
        self.throttle_pressure_sp = PU()  # Throttle pressure setpoint
        # Assuming SteamSupply, PU, Float, Seconds, Integer, and BoilerControlMode are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
