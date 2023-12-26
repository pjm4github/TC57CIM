package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;

/**
 * General governor model with frequency-dependent fuel flow limit.  This model is
 * a modification of the GovCT1<b> </b>model in order to represent the frequency-
 * dependent fuel flow limit of a specific gas turbine manufacturer.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovCT2 extends TurbineGovernorDynamics {

	/**
	 * Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10.
	 */
	public Float aset;
	/**
	 * Speed governor dead band in per unit speed (db).  In the majority of
	 * applications, it is recommended that this value be set to zero.  Typical Value
	 * = 0.
	 */
	public PU db;
	/**
	 * Speed sensitivity coefficient (Dm).  Dm can represent either the variation of
	 * the engine power with the shaft speed or the variation of maximum power
	 * capability with shaft speed.  If it is positive it describes the falling slope
	 * of the engine speed verses power characteristic as speed increases. A slightly
	 * falling characteristic is typical for reciprocating engines and some aero-
	 * derivative turbines.  If it is negative the engine power is assumed to be
	 * unaffected by the shaft speed, but the maximum permissible fuel flow is taken
	 * to fall with falling shaft speed. This is characteristic of single-shaft
	 * industrial turbines due to exhaust temperature limits.  Typical Value = 0.
	 */
	public PU dm;
	/**
	 * Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59.
	 */
	public Frequency flim1;
	/**
	 * Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim10;
	/**
	 * Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim2;
	/**
	 * Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim3;
	/**
	 * Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim4;
	/**
	 * Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim5;
	/**
	 * Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim6;
	/**
	 * Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim7;
	/**
	 * Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim8;
	/**
	 * Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0.
	 */
	public Frequency flim9;
	/**
	 * Acceleration limiter Gain (Ka).  Typical Value = 10.
	 */
	public PU ka;
	/**
	 * Governor derivative gain (Kdgov).  Typical Value = 0.
	 */
	public PU kdgov;
	/**
	 * Governor integral gain (Kigov).  Typical Value = 0.45.
	 */
	public PU kigov;
	/**
	 * Load limiter integral gain for PI controller (Kiload).  Typical Value = 1.
	 */
	public PU kiload;
	/**
	 * Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to
	 * a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow
	 * acting load controller.  Typical Value = 0.
	 */
	public PU kimw;
	/**
	 * Governor proportional gain (Kpgov).  Typical Value = 4.
	 */
	public PU kpgov;
	/**
	 * Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1.
	 */
	public PU kpload;
	/**
	 * Turbine gain (Kturb).  Typical Value = 1.9168.
	 */
	public PU kturb;
	/**
	 * Load limiter reference value (Ldref).  Typical Value = 1.
	 */
	public PU ldref;
	/**
	 * Maximum value for speed error signal (Maxerr).  Typical Value = 1.
	 */
	public PU maxerr;
	/**
	 * Minimum value for speed error signal (Minerr).  Typical Value = -1.
	 */
	public PU minerr;
	/**
	 * Base for power values (MWbase) (> 0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Power limit 1 (Plim1).  Typical Value = 0.8325.
	 */
	public PU plim1;
	/**
	 * Power limit 10 (Plim10).  Typical Value = 0.
	 */
	public PU plim10;
	/**
	 * Power limit 2 (Plim2).  Typical Value = 0.
	 */
	public PU plim2;
	/**
	 * Power limit 3 (Plim3).  Typical Value = 0.
	 */
	public PU plim3;
	/**
	 * Power limit 4 (Plim4).  Typical Value = 0.
	 */
	public PU plim4;
	/**
	 * Power limit 5 (Plim5).  Typical Value = 0.
	 */
	public PU plim5;
	/**
	 * Power limit 6 (Plim6).  Typical Value = 0.
	 */
	public PU plim6;
	/**
	 * Power limit 7 (Plim7).  Typical Value = 0.
	 */
	public PU plim7;
	/**
	 * Power limit 8 (Plim8).  Typical Value = 0.
	 */
	public PU plim8;
	/**
	 * Power Limit 9 (Plim9).  Typical Value = 0.
	 */
	public PU plim9;
	/**
	 * Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017.
	 */
	public PU prate;
	/**
	 * Permanent droop (R).  Typical Value = 0.05.
	 */
	public PU r;
	/**
	 * Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99.
	 */
	public Float rclose;
	/**
	 * Maximum rate of load limit decrease (Rdown).  Typical Value = -99.
	 */
	public PU rdown;
	/**
	 * Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99.
	 */
	public Float ropen;
	/**
	 * Feedback signal for droop (Rselect).  Typical Value = electricalPower.
	 */
	public DroopSignalFeedbackKind rselect;
	/**
	 * Maximum rate of load limit increase (Rup).  Typical Value = 99.
	 */
	public PU rup;
	/**
	 * Acceleration limiter time constant (Ta).  Typical Value = 1.
	 */
	public Seconds ta;
	/**
	 * Actuator time constant (Tact).  Typical Value = 0.4.
	 */
	public Seconds tact;
	/**
	 * Turbine lag time constant (Tb).  Typical Value = 0.1.
	 */
	public Seconds tb;
	/**
	 * Turbine lead time constant (Tc).  Typical Value = 0.
	 */
	public Seconds tc;
	/**
	 * Governor derivative controller time constant (Tdgov).  Typical Value = 1.
	 */
	public Seconds tdgov;
	/**
	 * Transport time delay for diesel engine used in representing diesel engines
	 * where there is a small but measurable transport delay between a change in fuel
	 * flow setting and the development of torque (Teng).  Teng should be zero in all
	 * but special cases where this transport delay is of particular concern.  Typical
	 * Value = 0.
	 */
	public Seconds teng;
	/**
	 * Load Limiter time constant (Tfload).  Typical Value = 3.
	 */
	public Seconds tfload;
	/**
	 * Electrical power transducer time constant (Tpelec).  Typical Value = 2.5.
	 */
	public Seconds tpelec;
	/**
	 * Temperature detection lead time constant (Tsa).  Typical Value = 0.
	 */
	public Seconds tsa;
	/**
	 * Temperature detection lag time constant (Tsb).  Typical Value = 50.
	 */
	public Seconds tsb;
	/**
	 * Maximum valve position limit (Vmax).  Typical Value = 1.
	 */
	public PU vmax;
	/**
	 * Minimum valve position limit (Vmin).  Typical Value = 0.175.
	 */
	public PU vmin;
	/**
	 * No load fuel flow (Wfnl).  Typical Value = 0.187.
	 */
	public PU wfnl;
	/**
	 * Switch for fuel source characteristic to recognize that fuel flow, for a given
	 * fuel valve stroke, can be proportional to engine speed (Wfspd).
	 * true = fuel flow proportional to speed (for some gas turbines and diesel
	 * engines with positive displacement fuel injectors)
	 * false = fuel control system keeps fuel flow independent of engine speed.
	 * Typical Value = false.
	 */
	public Boolean wfspd;

	public GovCT2(){

	}
}//end GovCT2