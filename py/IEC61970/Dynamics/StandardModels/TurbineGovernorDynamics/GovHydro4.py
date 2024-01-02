# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydro4(TurbineGovernorDynamics):
    """Hydro turbine and governor. Represents plants with straight-forward penstock
    configurations and hydraulic governors of traditional 'dashpot' type.  This
    model can be used to represent simple, Francis, Pelton or Kaplan turbines."""

    def __init__(self):
        super().__init__()
        self.at = PU(1.2)  # Turbine gain (At).  Typical Value = 1.2.
        self.bgv0 = PU(0)  # Kaplan blade servo point 0 (Bgv0).  Typical Value = 0.
        self.bgv1 = PU(0)  # Kaplan blade servo point 1 (Bgv1).  Typical Value = 0.
        self.bgv2 = PU(0)  # Kaplan blade servo point 2 (Bgv2).
        # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1.
        self.bgv3 = PU(0)  # Kaplan blade servo point 3 (Bgv3).
        # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667.
        self.bgv4 = PU(0)  # Kaplan blade servo point 4 (Bgv4).
        # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9.
        self.bgv5 = PU(0)  # Kaplan blade servo point 5 (Bgv5).
        # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.
        self.bmax: float = 0  # Maximum blade adjustment factor (Bmax).
        # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276.
        self.db1 = Frequency(0)  # Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
        self.db2 = ActivePower(0)  # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
        self.dturb = PU(.5)  # Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed
        # (PU).
        # Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1.
        self.eps = Frequency(0)  # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
        self.gmax = PU(1)  # Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1.
        self.gmin = PU(0)  # Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0.
        self.gv0 = PU(0)  # Nonlinear gain point 0, PU gv (Gv0).
        # Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1.
        self.gv1 = PU(0)  # Nonlinear gain point 1, PU gv (Gv1).
        # Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4.
        self.gv2 = PU(0)  # Nonlinear gain point 2, PU gv (Gv2).
        # Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5.
        self.gv3 = PU(0)  # Nonlinear gain point 3, PU gv (Gv3).
        # Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7.
        self.gv4 = PU(0)  # Nonlinear gain point 4, PU gv (Gv4).
        # Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8.
        self.gv5 = PU(0)  # Nonlinear gain point 5, PU gv (Gv5).
        # Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9.
        self.hdam = PU(1)  # Head available at dam (hdam).  Typical Value = 1.
        self.mwbase = ActivePower(.1)  # Base for power values (MWbase) (>0).  Unit = MW.
        self.pgv0 = PU(0)  # Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0.
        self.pgv1 = PU(0)  # Nonlinear gain point 1, PU power (Pgv1).
        # Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35.
        self.pgv2 = PU(0)  # Nonlinear gain point 2, PU power (Pgv2).
        self.pgv3 = PU(0)  # Nonlinear gain point 3, PU power (Pgv3).
        # Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796.
        self.pgv4 = PU(0)  # Nonlinear gain point 4, PU power (Pgv4).
        # Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917.
        self.pgv5 = PU(0)  # Nonlinear gain point 5, PU power (Pgv5).
        # Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99.
        self.qn1 = PU(.08)  # No-load flow at nominal head (Qnl).
        # Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0.
        self.rperm = Seconds(.05)  # Permanent droop (Rperm).  Typical Value = 0.05.
        self.rtemp = Seconds(.3)  # Temporary droop (Rtemp).  Typical Value = 0.3.
        self.tblade = Seconds(100)  # Blade servo time constant (Tblade).  Typical Value = 100.
        self.tg = Seconds(.5)  # Gate servo time constant (Tg) (>0).  Typical Value = 0.5.
        self.tp = Seconds(.1)  # Pilot servo time constant (Tp).  Typical Value = 0.1.
        self.tr = Seconds(5)  # Dashpot time constant (Tr) (>0).  Typical Value = 5.
        self.tw = Seconds(1)  # Water inertia time constant (Tw) (>0).  Typical Value = 1.
        self.uc : float = .2  # Max gate closing velocity (Uc).  Typical Value = 0.2.
        self.uo : float = .2  # Max gate opening velocity (Uo).  Typical Value = 0.2.
