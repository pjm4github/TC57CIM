# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantQcontrolModeKind import WindPlantQControlModeKind


class WindPlantReactiveControlIEC(IdentifiedObject):
    """
    Simplified plant voltage and reactive power control model for use with type 3
    and type 4 wind turbine models.
    
    Reference: IEC Standard 61400-27-1 Annex D.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self):
        super().__init__()
        self.dxrefmax = PU()  # Maximum positive ramp rate for wind turbine reactive power/voltage reference (dx_refmax)
        self.dxrefmin = PU()  # Maximum negative ramp rate for wind turbine reactive power/voltage reference (dx_refmin)
        self.kiwpx = 1.0  # Plant Q controller integral gain (K_IWPx)
        self.kiwpxmax = PU()  # Maximum reactive Power/voltage reference from integration (K_IWPxmax)
        self.kiwpxmin = PU()  # Minimum reactive Power/voltage reference from integration (K_IWPxmin)
        self.kpwpx = 1.0  # Plant Q controller proportional gain (K_PWPx)
        self.kwpqref = PU()  # Reactive power reference gain (K_WPqref)
        self.kwpqu = PU()  # Plant voltage control droop (K_WPqu)
        self.tuqfilt = Seconds()  # Filter time constant for voltage dependent reactive power (T_uqfilt)
        self.twppfiltq = Seconds()  # Filter time constant for active power measurement (T_WPpfiltq)
        self.twpqfiltq = Seconds()  # Filter time constant for reactive power measurement (T_WPqfiltq)
        self.twpufiltq = Seconds()  # Filter time constant for voltage measurement (T_WPufiltq)
        self.txft = Seconds()  # Lead time constant in reference value transfer function (T_xft)
        self.txfv = Seconds()  # Lag time constant in reference value transfer function (T_xfv)
        self.uwpqdip = PU()  # Voltage threshold for UVRT detection in q control (u_WPqdip)
        self.wind_plant_q_control_modes_type = WindPlantQControlModeKind.VOLTAGE_CONTROL  # Reactive power/voltage controller mode (M_WPqmode)
        self.xrefmax = PU()  # Maximum x_WTref (q_WTref or delta u_WTref) request from the plant controller (x_refmax)
        self.xrefmin = PU()  # Minimum x_WTref (q_WTref or delta u_WTref) request from the plant controller (x_refmin)
