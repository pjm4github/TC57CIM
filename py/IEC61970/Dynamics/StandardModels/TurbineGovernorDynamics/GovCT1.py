# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from typing import Optional, Union

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.DroopSignalFeedbackKind import DroopSignalFeedbackKind
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovCt1(TurbineGovernorDynamics):
    """
        General model for any prime mover with a PID governor, used primarily for
        combustion turbine and combined cycle units.
        This model can be used to represent a variety of prime movers controlled by PID
        governors.  It is suitable, for example, for representation of
        <ul>
            <li>gas turbine and single shaft combined cycle turbines </li>
        </ul>
        <ul>
            <li>diesel engines with modern electronic or digital governors  </li>
        </ul>
        <ul>
            <li>steam turbines where steam is supplied from a large boiler drum or a large
        header whose pressure is substantially constant over the period under study
        </li>
            <li>simple hydro turbines in dam configurations where the water column length
        is short and water inertia effects are minimal. </li>
        </ul>
        Additional information on this model is available in the 2012 IEEE report,
        <i><u>Dynamic Models for Turbine-Governors in Power System Studies</u></i>,
        section 3.1.2.3 page 3-4 (GGOV1).
        @author tsaxton
        @version 1.0
        @created 29-Dec-2023 11:24:18 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.aset: float = 0.01  # Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 0.01.
        self.db: PU = PU(0.0)  # Speed governor dead band in per unit speed (db).  In the majority of applications,
        # it is recommended that this value be set to zero.  Typical Value = 0.
        self.dm: PU = PU(0.0)  # Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the
        # engine power with the shaft speed or the variation of maximum power capability with shaft speed.
        # If it is positive it describes the falling slope of the engine speed verses power characteristic as
        # speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-
        # derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed,
        # but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of
        # single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0.
        self.ka: PU = PU(10.0)  # Acceleration limiter gain (Ka).  Typical Value = 10.
        self.kdgov: PU = PU(0.0)  # Governor derivative gain (Kdgov).  Typical Value = 0.
        self.kigov: PU = PU(2.0)  # Governor integral gain (Kigov).  Typical Value = 2.
        self.kiload: PU = PU(0.67)  # Load limiter integral gain for PI controller (Kiload).  Typical Value = 0.67.
        self.kimw: PU = PU(0.01)  # Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a
        # reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.
        # Typical Value = 0.01.
        self.kpgov: PU = PU(10.0)  # Governor proportional gain (Kpgov).  Typical Value = 10.
        self.kpload: PU = PU(2.0)  # Load limiter proportional gain for PI controller (Kpload).  Typical Value = 2.
        self.kturb: PU = PU(1.5)  # Turbine gain (Kturb) (>0).  Typical Value = 1.5.
        self.ldref: PU = PU(1.0)  # Load limiter reference value (Ldref).  Typical Value = 1.
        self.maxerr: PU = PU(0.05)  # Maximum value for speed error signal (maxerr).  Typical Value = 0.05.
        self.minerr: PU = PU(-0.05)  # Minimum value for speed error signal (minerr).  Typical Value = -0.05.
        self.mwbase: ActivePower = ActivePower(0.1)  # Base for power values (MWbase) (> 0).  Unit = MW.
        self.r: PU = PU(0.04)  # Permanent droop (R).  Typical Value = 0.04.
        self.rclose: float = -0.1  # Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -0.1.
        self.rdown: PU = PU(-99.)  # Maximum rate of load limit decrease (Rdown).  Typical Value = -99.
        self.ropen: float = 0.1  # Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 0.10.
        self.rselect: DroopSignalFeedbackKind = DroopSignalFeedbackKind.ELECTRICAL_POWER  # Feedback signal for droop (Rselect).  Typical Value = electricalPower.
        self.rup: PU = PU(99.0)  # Maximum rate of load limit increase (Rup).  Typical Value = 99.
        self.ta: Seconds = Seconds(0.1)  # Acceleration limiter time constant (Ta) (>0).  Typical Value = 0.1.
        self.tact: Seconds = Seconds(0.5)  # Actuator time constant (Tact).  Typical Value = 0.5.
        self.tb: Seconds = Seconds(0.5)  # Turbine lag time constant (Tb) (>0).  Typical Value = 0.5.
        self.tc: Seconds = Seconds(0.0)  # Turbine lead time constant (Tc).  Typical Value = 0.
        self.tdgov: Seconds = Seconds(1.0)  # Governor derivative controller time constant (Tdgov).  Typical Value = 1.
        self.teng: Seconds = Seconds(0.0)  # Transport time delay for diesel engine used in representing diesel engines
        # where there is a small but measurable transport delay between a change in fuel flow setting and the
        # development of torque (Teng).  Teng should be zero in all but special cases where this transport
        # delay is of particular concern.  Typical Value = 0.
        self.tfload: Seconds = Seconds(3.0)  # Load Limiter time constant (Tfload) (>0).  Typical Value = 3.
        self.tpelec: Seconds = Seconds(1.)  # Electrical power transducer time constant (Tpelec) (>0).
        # Typical Value = 1.
        self.tsa: Seconds = Seconds(4.0)  # Temperature detection lead time constant (Tsa).  Typical Value = 4.
        self.tsb: Seconds = Seconds(5.0)  # Temperature detection lag time constant (Tsb).  Typical Value = 5.
        self.vmax: PU = PU(1.0)  # Maximum valve position limit (Vmax).  Typical Value = 1.
        self.vmin: PU = PU(0.15)  # Minimum valve position limit (Vmin).  Typical Value = 0.15.
        self.wfnl: PU = PU(0.2)  # No load fuel flow (Wfnl).  Typical Value = 0.2.
        self.wfspd: bool = True # Switch for fuel source characteristic to recognize that fuel flow, for a given fuel
        # valve stroke, can be proportional to engine speed (Wfspd).
        # True = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement
        # fuel injectors)
        # False = fuel control system keeps fuel flow independent of engine speed.
        # Typical Value = True.





































