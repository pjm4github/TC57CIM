from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Generation.GenerationTrainingSimulation.SteamSupply import SteamSupply


class BWRSteamSupply(SteamSupply):
    """
    Boiling water reactor used as a steam supply to a steam turbine.
    Created: 02-Jan-2024 11:04:03 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.high_power_limit = PU()  # High power limit
        self.in_core_thermal_tc = Seconds()  # In-core thermal time constant
        self.integral_gain = 0.0  # Integral gain
        self.lower_limit = PU()  # Initial lower limit
        self.low_power_limit = PU()  # Low power limit
        self.pressure_limit = PU()  # Pressure limit
        self.pressure_setpoint_ga = 0.0  # Pressure setpoint gain adjuster
        self.pressure_setpoint_tc1 = Seconds()  # Pressure setpoint time constant
        self.pressure_setpoint_tc2 = Seconds()  # Pressure setpoint time constant
        self.proportional_gain = 0.0  # Proportional gain
        self.rf_aux1 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rf_aux2 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rf_aux3 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rf_aux4 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rf_aux5 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rf_aux6 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rf_aux7 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rf_aux8 = PU()  # Coefficient for modeling the effect of off-nominal frequency and voltage
        self.rod_pattern = PU()  # Rod pattern
        self.rod_pattern_constant = 0.0  # Constant associated with rod pattern
        self.upper_limit = PU()  # Initial upper limit
        # Assuming SteamSupply, PU, Seconds, and Float are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
