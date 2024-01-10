from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Generation.GenerationTrainingSimulation.SteamSupply import SteamSupply


class PWRSteamSupply(SteamSupply):
    """
    Pressurized water reactor used as a steam supply to a steam turbine.
    Created: 02-Jan-2024 11:06:06 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.cold_leg_fb_lag_tc = PU()  # Cold leg feedback lag time constant
        self.cold_leg_fb_lead_tc1 = PU()  # Cold leg feedback lead time constant
        self.cold_leg_fb_lead_tc2 = PU()  # Cold leg feedback lead time constant
        self.cold_leg_fg1 = PU()  # Cold leg feedback gain 1
        self.cold_leg_fg2 = PU()  # Cold leg feedback gain 2
        self.cold_leg_lag_tc = PU()  # Cold leg lag time constant
        self.core_ht_lag_tc1 = PU()  # Core heat transfer lag time constant
        self.core_ht_lag_tc2 = PU()  # Core heat transfer lag time constant
        self.core_neutronics_eff_tc = PU()  # Core neutronics effective time constant
        self.core_neutronics_ht = PU()  # Core neutronics and heat transfer
        self.feedback_factor = PU()  # Feedback factor
        self.hot_leg_lag_tc = PU()  # Hot leg lag time constant
        self.hot_leg_steam_gain = PU()  # Hot leg steam gain
        self.hot_leg_to_cold_leg_gain = PU()  # Hot leg to cold leg gain
        self.pressure_cg = PU()  # Pressure control gain
        self.steam_flow_fg = PU()  # Steam flow feedback gain
        self.steam_pressure_drop_lag_tc = PU()  # Steam pressure drop lag time constant
        self.steam_pressure_fg = PU()  # Steam pressure feedback gain
        self.throttle_pressure_factor = PU()  # Throttle pressure factor
        self.throttle_pressure_sp = PU()  # Throttle pressure setpoint
        # Assuming SteamSupply and PU are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
