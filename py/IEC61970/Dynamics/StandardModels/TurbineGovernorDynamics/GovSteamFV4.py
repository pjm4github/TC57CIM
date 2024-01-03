from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics import TurbineGovernorDynamics

class GovSteamFV4(TurbineGovernorDynamics):
    """
    Detailed electro-hydraulic governor for steam unit.
    """
    def __init__(self):
        super().__init__()
        self.cpsmn = PU(-1)  # Minimum value of pressure regulator output (Cpsmn).  Typical Value = -1.
        self.cpsmx = PU(1)  # Maximum value of pressure regulator output (Cpsmx).  Typical Value = 1.
        self.crmn = PU(0)  # Minimum value of regulator set-point (Crmn).  Typical Value = 0.
        self.crmx = PU(1.2)  # Maximum value of regulator set-point (Crmx).  Typical Value = 1.2.
        self.kdc = PU(1)  # Derivative gain of pressure regulator (Kdc).  Typical Value = 1.
        self.kf1 = PU(20)  # Frequency bias (reciprocal of droop) (Kf1).  Typical Value = 20.
        self.kf3 = PU(20)  # Frequency control (reciprocal of droop) (Kf3).  Typical Value = 20.
        self.khp = PU(0.35)  # Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.35.
        self.kic = PU(0.0033)  # Integral gain of pressure regulator (Kic).  Typical Value = 0.0033.
        self.kip = PU(0.5)  # Integral gain of pressure feedback regulator (Kip).  Typical Value = 0.5.
        self.kit = PU(0.04)  # Integral gain of electro-hydraulic regulator (Kit).  Typical Value = 0.04.
        self.kmp1 = PU(0.5)  # First gain coefficient of intercept valves characteristic (Kmp1).  Typical Value = 0.5.
        self.kmp2 = PU(3.5)  # Second gain coefficient of intercept valves characteristic (Kmp2).  Typical Value = 3.5.
        self.kpc = PU(0.5)  # Proportional gain of pressure regulator (Kpc).  Typical Value = 0.5.
        self.kpp = PU(1)  # Proportional gain of pressure feedback regulator (Kpp).  Typical Value = 1.
        self.kpt = PU(0.3)  # Proportional gain of electro-hydraulic regulator (Kpt).  Typical Value = 0.3.
        self.krc = PU(0.05)  # Maximum variation of fuel flow (Krc).  Typical Value = 0.05.
        self.ksh = PU(0.08)  # Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical Value = 0.08.
        self.lpi = PU(-0.15)  # Maximum negative power error (Lpi).  Typical Value = -0.15.
        self.lps = PU(0.03)  # Maximum positive power error (Lps).  Typical Value = 0.03.
        self.mnef = PU(-0.05)  # Lower limit for frequency correction (MN_EF).  Typical Value = -0.05.
        self.mxef = PU(0.05)  # Upper limit for frequency correction (MX_EF).  Typical Value = 0.05.
        self.pr1 = PU(0.2)  # First value of pressure set point static characteristic (Pr1).  Typical Value = 0.2.
        self.pr2 = PU(0.75)  # Second value of pressure set point static characteristic, corresponding to Ps0 = 1.0 PU (Pr2).  Typical Value = 0.75.
        self.psmn = PU(1)  # Minimum value of pressure set point static characteristic (Psmn).  Typical Value = 1.
        self.rsmimn = PU(0)  # Minimum value of integral regulator (Rsmimn).  Typical Value = 0.
        self.rsmimx = PU(1.1)  # Maximum value of integral regulator (Rsmimx).  Typical Value = 1.1.
        self.rvgmn = PU(0)  # Minimum value of integral regulator (Rvgmn).  Typical Value = 0.
        self.rvgmx = PU(1.2)  # Maximum value of integral regulator (Rvgmx).  Typical Value = 1.2.
        self.srmn = PU(0)  # Minimum valve opening (Srmn).  Typical Value = 0.
        self.srmx = PU(1.1)  # Maximum valve opening (Srmx).  Typical Value = 1.1.
        self.srsmp = PU(0.43)  # Intercept valves characteristic discontinuity point (Srsmp).  Typical Value = 0.43.
        self.svmn = -0.0333  # Maximum regulator gate closing velocity (Svmn).  Typical Value = -0.0333.
        self.svmx = 0.0333  # Maximum regulator gate opening velocity (Svmx).  Typical Value = 0.0333.
        self.ta = Seconds(0.8)  # Control valves rate opening time (Ta).  Typical Value = 0.8.
        self.tam = Seconds(0.8)  # Intercept valves rate opening time (Tam).  Typical Value = 0.8.
        self.tc = Seconds(0.5)  # Control valves rate closing time (Tc).  Typical Value = 0.5.
        self.tcm = Seconds(0.5)  # Intercept valves rate closing time (Tcm).  Typical Value = 0.5.
        self.tdc = Seconds(90)  # Derivative time constant of pressure regulator (Tdc).  Typical Value = 90.
        self.tf1 = Seconds(10)  # Time constant of fuel regulation (Tf1).  Typical Value = 10.
        self.tf2 = Seconds(10)  # Time constant of steam chest (Tf2).  Typical Value = 10.
        self.thp = Seconds(0.15)  # High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.15.
        self.tmp = Seconds(0.4)  # Low pressure (LP) time constant of the turbine (Tmp).  Typical Value = 0.4.
        self.trh = Seconds(10)  # Reheater time constant of the turbine (Trh).  Typical Value = 10.
        self.tv = Seconds(60)  # Boiler time constant (Tv).  Typical Value = 60.
        self.ty = Seconds(0.1)  # Control valves servo time constant (Ty).  Typical Value = 0.1.
        self.y = PU(0.13)  # Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical Value = 0.13.
        self.yhpmn = PU(0)  # Minimum control valve position (Yhpmn).  Typical Value = 0.
        self.yhpmx = PU(1.1)  # Maximum control valve position (Yhpmx).  Typical Value = 1.1.
        self.ympmn = PU(0)  # Minimum intercept valve position (Ympmn).  Typical Value = 0.
        self.ympmx = PU(1.1)  # Maximum intercept valve position (Ympmx).  Typical Value = 1.1.