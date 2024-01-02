# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.DroopSignalFeedbackKind import DroopSignalFeedbackKind
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovCT2(TurbineGovernorDynamics):
    """
    General governor model with frequency-dependent fuel flow limit. This model is a modification of the GovCT1
    model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self):
        super().__init__()
        # Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10.
        self.aset = 10.0

        # Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that
        # this value be set to zero.  Typical Value = 0.
        self.db: PU = PU(0)

        # Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the
        # shaft speed or the variation of maximum power capability with shaft speed.
        # If it is positive it describes the falling slope of the engine speed verses power characteristic as
        # speed increases. A slightly falling characteristic is typical for reciprocating engines and some
        # aero-derivative turbines.
        # If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum
        # permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft
        # industrial turbines due to exhaust temperature limits.
        # Typical Value = 0.
        self.dm: PU = PU(0)

        # Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59.
        self.flim1: Frequency = Frequency(59)

        # Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0.
        self.flim10: Frequency = Frequency(0)

        # Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0.
        self.flim2: Frequency = Frequency(0)

        # Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0.
        self.flim3: Frequency = Frequency(0)

        # Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0.
        self.flim4: Frequency = Frequency(0)

        # Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0.
        self.flim5: Frequency = Frequency(0)

        # Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0.
        self.flim6: Frequency = Frequency(0)

        # Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0.
        self.flim7: Frequency = Frequency(0)

        # Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0.
        self.flim8: Frequency = Frequency(0)

        # Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0.
        self.flim9: Frequency = Frequency(0)

        # Acceleration limiter Gain (Ka).  Typical Value = 10.
        self.ka: PU = PU(10)

        # Governor derivative gain (Kdgov).  Typical Value = 0.
        self.kdgov: PU = PU(0)

        # Governor integral gain (Kigov).  Typical Value = 0.45.
        self.kigov: PU = PU(0.45)

        # Load limiter integral gain for PI controller (Kiload).  Typical Value = 1.
        self.kiload: PU = PU(1)

        # Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.
        # A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0.
        self.kimw: PU = PU(0)

        # Governor proportional gain (Kpgov).  Typical Value = 4.
        self.kpgov: PU = PU(4)

        # Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1.
        self.kpload: PU = PU(1)

        # Turbine gain (Kturb).  Typical Value = 1.9168.
        self.kturb: PU = PU(1.9168)

        # Load limiter reference value (Ldref).  Typical Value = 1.
        self.ldref: PU = PU(1)

        # Maximum value for speed error signal (Maxerr).  Typical Value = 1.
        self.maxerr: PU = PU(1)

        # Minimum value for speed error signal (Minerr).  Typical Value = -1.
        self.minerr: PU = PU(-1)

        # Base for power values (MWbase) (> 0).  Unit = MW.
        self.mwbase = ActivePower(.1)

        # Power limit 1 (Plim1).

        # Power limit 1 (Plim1).  Typical Value = 0.8325.
        self.plim1: PU = PU()

        # Power limit 10 (Plim10).  Typical Value = 0.
        self.plim10: PU = PU()

        # Power limit 2 (Plim2).  Typical Value = 0.
        self.plim2: PU = PU()

        # Power limit 3 (Plim3).  Typical Value = 0.
        self.plim3: PU = PU()

        # Power limit 4 (Plim4).  Typical Value = 0.
        self.plim4: PU = PU()

        # Power limit 5 (Plim5).  Typical Value = 0.
        self.plim5: PU = PU()

        # Power limit 6 (Plim6).  Typical Value = 0.
        self.plim6: PU = PU()

        # Power limit 7 (Plim7).  Typical Value = 0.
        self.plim7: PU = PU()

        # Power limit 8 (Plim8).  Typical Value = 0.
        self.plim8: PU = PU()

        # Power Limit 9 (Plim9).  Typical Value = 0.
        self.plim9: PU = PU()

        # Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017.
        self.prate: PU = PU()

        # Permanent droop (R).  Typical Value = 0.05.
        self.r: PU = PU()

        # Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99.
        self.rclose: float = -99

        # Maximum rate of load limit decrease (Rdown).  Typical Value = -99.
        self.rdown: PU = PU()

        # Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99.
        self.ropen: float = 99

        # Feedback signal for droop (Rselect).  Typical Value = electricalPower.
        self.rselect: DroopSignalFeedbackKind = DroopSignalFeedbackKind.ELECTRICAL_POWER
        self.rup: PU = PU(99)  # Maximum rate of load limit increase (Rup).  Typical Value = 99.

        self.ta: Seconds = Seconds(1)  # Acceleration limiter time constant (Ta).  Typical Value = 1.
        self.tact: Seconds = Seconds(.4)  # Actuator time constant (Tact).  Typical Value = 0.4.
        self.tb: Seconds = Seconds(.1)  # Turbine lag time constant (Tb).  Typical Value = 0.1.
        self.tc: Seconds = Seconds(0)  # Turbine lead time constant (Tc).  Typical Value = 0.
        self.tdgov: Seconds = Seconds(1)  # Governor derivative controller time constant (Tdgov).  Typical Value = 1.
        # Transport time delay for diesel engine used in representing diesel engines where there is a small but
        # measurable transport delay between a change in fuel flow setting and the development of torque (Teng).
        # Teng should be zero in all but special cases where this transport delay is of particular concern.
        # Typical Value = 0.
        self.teng: Seconds = Seconds(0)
        self.tfload: Seconds = Seconds(3)  # Load Limiter time constant (Tfload).  Typical Value = 3.
        self.tpelec: Seconds = Seconds(2.5)  # Electrical power transducer time constant (Tpelec).  Typical Value = 2.5.
        self.tsa: Seconds = Seconds(0)  # Temperature detection lead time constant (Tsa).  Typical Value = 0.
        self.tsb: Seconds = Seconds(50)  # Temperature detection lag time constant (Tsb).  Typical Value = 50.
        self.vmax: PU = PU(1) # Maximum valve position limit (Vmax).  Typical Value = 1.
        self.vmin: PU = PU(.175)  # Minimum valve position limit (Vmin).  Typical Value = 0.175.
        self.wfnl: PU = PU(.187)  # No load fuel flow (Wfnl).  Typical Value = 0.187.
        # Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be
        # proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and
        # diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow
        # independent of engine speed. Typical Value = false.
        self.wfspd: bool = False
