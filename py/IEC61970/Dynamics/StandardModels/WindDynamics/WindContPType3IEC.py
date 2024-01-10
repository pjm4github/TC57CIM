# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3IEC import WindTurbineType3IEC


class WindContPType3IEC(IdentifiedObject):
    """
    P control model Type 3.
    Reference: IEC Standard 61400-27-1 Section 5.6.5.4.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """
    def __init__(self):
        super().__init__()
        self.dpmax = PU()  # Maximum wind turbine power ramp rate (dp_max). It is type dependent parameter.
        self.dprefmax = PU()  # Maximum ramp rate of wind turbine reference power (dp_refmax). It is project dependent parameter.
        self.dprefmin = PU()  # Minimum ramp rate of wind turbine reference power (dp_refmin). It is project dependent parameter.
        self.dthetamax = PU()  # Ramp limitation of torque, required in some grid codes (d_theta_max). It is project dependent parameter.
        self.dthetamaxuvrt = PU()  # Limitation of torque rise rate during UVRT (d_theta_maxUVRT). It is project dependent parameter.
        self.kdtd = PU()  # Gain for active drive train damping (K_DTD). It is type dependent parameter.
        self.kip = PU()  # PI controller integration parameter (K_Ip). It is type dependent parameter.
        self.kpp = PU()  # PI controller proportional gain (K_Pp). It is type dependent parameter.
        self.mpuvrt = False  # Enable UVRT power control mode (M_pUVRT). true = 1: voltage control, false = 0: reactive power control. It is project dependent parameter.
        self.omegaoffset = PU()  # Offset to reference value that limits controller action during rotor speed changes (omega_offset). It is case dependent parameter.
        self.pdtdmax = PU()  # Maximum active drive train damping power (p_DTDmax). It is type dependent parameter.
        self.tdvs = Seconds()  # Time delay after deep voltage sags (T_DVS). It is project dependent parameter.
        self.thetaemin = PU()  # Minimum electrical generator torque (t_emin). It is type dependent parameter.
        self.thetauscale = PU()  # Voltage scaling factor of reset-torque (t_uscale). It is project dependent parameter.
        self.tomegafiltp3 = Seconds()  # Filter time constant for generator speed measurement (T_omegafiltp3). It is type dependent parameter.
        self.tpfiltp3 = Seconds()  # Filter time constant for power measurement (T_pfiltp3). It is type dependent parameter.
        self.tpord = PU()  # Time constant in power order lag (T_pord). It is type dependent parameter.
        self.tufiltp3 = Seconds()  # Filter time constant for voltage measurement (T_ufiltp3). It is type dependent parameter.
        self.twref = Seconds()  # Time constant in speed reference filter (T_omega,ref). It is type dependent parameter.
        self.udvs = PU()  # Voltage limit for hold UVRT status after deep voltage sags (u_DVS). It is project dependent parameter.
        self.updip = PU()  # Voltage dip threshold for P-control (u_Pdip). Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter.
        self.wdtd = PU()  # Active drive train damping frequency (omega_DTD). It can be calculated from two mass model parameters. It is type dependent parameter.
        self.zeta = 0.0  # Coefficient for active drive train damping (zeta). It is type dependent parameter.
        self.wind_turbine_type_3iec = WindTurbineType3IEC()  # Wind turbine type 3 model with which this Wind control P type 3 model is associated.
