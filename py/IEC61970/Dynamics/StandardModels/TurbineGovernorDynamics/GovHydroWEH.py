# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroWEH(TurbineGovernorDynamics):
    """Woodward Electric Hydro Governor Model.
    
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """
    def __init__(self):
        super().__init__()
        self.db = PU()  # Speed Dead Band (db).
        self.dicn = PU()  # Value to allow the integral controller to advance beyond the gate limits (Dicn).
        self.dpv = PU()  # Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv).
        self.dturb = PU()  # Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU).
        self.feedback_signal = True  # Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0).
        self.fl1 = PU()  # Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow.
        self.fl2 = PU()  # Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow.
        self.fl3 = PU()  # Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow.
        self.fl4 = PU()  # Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow.
        self.fl5 = PU()  # Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow.
        self.fp1 = PU()  # Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp10 = PU()  # Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp2 = PU()  # Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp3 = PU()  # Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp4 = PU()  # Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp5 = PU()  # Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp6 = PU()  # Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp7 = PU()  # Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp8 = PU()  # Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.fp9 = PU()  # Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow.
        self.gmax = PU()  # Maximum Gate Position (Gmax).
        self.gmin = PU()  # Minimum Gate Position (Gmin).
        self.gtmxcl = PU()  # Maximum gate closing rate (Gtmxcl).
        self.gtmxop = PU()  # Maximum gate opening rate (Gtmxop).
        self.gv1 = PU()  # Gate 1 (Gv1).  Gate Position value
        self.gv2 = PU()  # Gate 2 (Gv2).
        self.gv3 = PU()  # Gate 3 (Gv3).
        self.gv4 = PU()  # Gate 4 (Gv4).
        self.gv5 = PU()  # Gate 5 (Gv5).
        self.kd = PU()  # Derivative controller derivative gain (Kd).
        self.ki = PU()  # Derivative controller Integral gain (Ki).
        self.kp = PU()  # Derivative control gain (Kp).
        self.mwbase = ActivePower()  # Base for power values (MWbase) (>0).  Unit = MW.
        self.pmss1 = PU()  # Pmss Flow P1 (Pmss1).
        self.pmss10 = PU()  # Pmss Flow P10 (Pmss10).
        self.pmss2 = PU()  # Pmss Flow P2 (Pmss2).
        self.pmss3 = PU()  # Pmss Flow P3 (Pmss3).
        self.pmss4 = PU()  # Pmss Flow P4 (Pmss4).
        self.pmss5 = PU()  # Pmss Flow P5 (Pmss5).
        self.pmss6 = PU()  # Pmss Flow P6 (Pmss6).
        self.pmss7 = PU()  # Pmss Flow P7 (Pmss7).
        self.pmss8 = PU()  # Pmss Flow P8 (Pmss8).
        self.pmss9 = PU()  # Pmss Flow P9 (Pmss9).
        self.rpg = 0.1  # Permanent droop for governor output feedback (R-Perm-Gate).
        self.rpp = 0.1  # Permanent droop for electrical power feedback (R-Perm-Pe).
        self.td = Seconds()  # Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td).
        self.tdv = Seconds()  # Distributive Valve time lag time constant (Tdv).
        self.tg = Seconds()  # Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg).
        self.tp = Seconds()  # Pilot Valve time lag time constant (Tp).
        self.tpe = Seconds()  # Electrical power droop time constant (Tpe).
        self.tw = Seconds()  # Water inertia time constant (Tw) (>0).
