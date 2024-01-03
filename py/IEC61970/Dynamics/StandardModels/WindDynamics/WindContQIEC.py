# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindQcontrolModeKind import WindQcontrolModeKind
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindUVRTQcontrolModeKind import WindUVRTQcontrolModeKind


class WindContQIEC(IdentifiedObject):
    """
    Q control model.
    
    Reference: IEC Standard 61400-27-1 Section 5.6.5.7.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """
    def __init__(self):
        super().__init__()
        self.iq_h1 = PU()  # Maximum reactive current injection during dip (i_qh1)
        self.iq_max = PU()  # Maximum reactive current injection (i_qmax)
        self.iq_min = PU()  # Minimum reactive current injection (i_qmin)
        self.iq_post = PU()  # Post fault reactive current injection (i_qpost)
        self.kiq = PU()  # Reactive power PI controller integration gain (K_I,q)
        self.kiu = PU()  # Voltage PI controller integration gain (K_I,u)
        self.kpq = PU()  # Reactive power PI controller proportional gain (K_P,q)
        self.kpu = PU()  # Voltage PI controller proportional gain (K_P,u)
        self.kqv = PU()  # Voltage scaling factor for UVRT current (K_qv)
        self.r_droop = PU()  # Resistive component of voltage drop impedance (r_droop)
        self.t_pfiltq = Seconds()  # Power measurement filter time constant (T_pfiltq)
        self.t_post = Seconds()  # Length of time period where post fault reactive power is injected (T_post)
        self.t_qord = Seconds()  # Time constant in reactive power order lag (T_qord)
        self.t_ufiltq = Seconds()  # Voltage measurement filter time constant (T_ufiltq)
        self.u_db1 = PU()  # Voltage dead band lower limit (u_db1)
        self.u_db2 = PU()  # Voltage dead band upper limit (u_db2)
        self.u_max = PU()  # Maximum voltage in voltage PI controller integral term (u_max)
        self.u_min = PU()  # Minimum voltage in voltage PI controller integral term (u_min)
        self.u_qdip = PU()  # Voltage threshold for UVRT detection in q control (u_qdip)
        self.u_ref0 = PU()  # User defined bias in voltage reference (u_ref0)
        self.wind_q_control_modes_type = WindQcontrolModeKind.VOLTAGE  # Types of general wind turbine Q control modes (M_qG)
        self.wind_uvrt_q_control_modes_type = WindUVRTQcontrolModeKind.MODE_0   # Types of UVRT Q control modes (M_qUVRT)
        self.x_droop = PU()  # Inductive component of voltage drop impedance (x_droop)
        self.wind_turbine_type3or4_iec = WindTurbineType3or4IEC()  # Wind turbine type 3 or 4 model with which this reactive
