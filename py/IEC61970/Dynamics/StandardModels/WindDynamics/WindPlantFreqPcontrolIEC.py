# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantIEC import WindPlantIEC


class WindPlantFreqPcontrolIEC(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.dprefmax = PU()  # Maximum ramp rate of p_WTref request from the plant controller to the wind turbines (dp_refmax)
        self.dprefmin = PU()  # Minimum (negative) ramp rate of p_WTref request from the plant controller to the wind turbines (dp_refmin)
        self.dpwprefmax = PU()  # Maximum positive ramp rate for wind plant power reference (dp_WPrefmax)
        self.dpwprefmin = PU()  # Maximum negative ramp rate for wind plant power reference (dp_WPrefmin)
        self.kiwpp = 0.0  # Plant P controller integral gain (K_IWPp)
        self.kiwppmax = PU()  # Maximum PI integrator term (K_IWPpmax)
        self.kiwppmin = PU()  # Minimum PI integrator term (K_IWPpmin)
        self.kpwpp = 0.0  # Plant P controller proportional gain (K_PWPp)
        self.kwppref = PU()  # Power reference gain (K_WPpref)
        self.prefmax = PU()  # Maximum p_WTref request from the plant controller to the wind turbines (p_refmax)
        self.prefmin = PU()  # Minimum p_WTref request from the plant controller to the wind turbines (p_refmin)
        self.tpft = Seconds()  # Lead time constant in reference value transfer function (T_pft)
        self.tpfv = Seconds()  # Lag time constant in reference value transfer function (T_pfv)
        self.twpffiltp = Seconds()  # Filter time constant for frequency measurement (T_WPffiltp)
        self.twppfiltp = Seconds()  # Filter time constant for active power measurement (T_WPpfiltp)
        self.wind_plant_iec = WindPlantIEC()  # Wind plant model with which this wind plant frequency and active power control