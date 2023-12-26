package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;

/**
 * General model for any prime mover with a PID governor, used primarily for
 * combustion turbine and combined cycle units.
 * This model can be used to represent a variety of prime movers controlled by PID
 * governors.  It is suitable, for example, for representation of
 * <ul>
 * 	<li>gas turbine and single shaft combined cycle turbines </li>
 * </ul>
 * <ul>
 * 	<li>diesel engines with modern electronic or digital governors  </li>
 * </ul>
 * <ul>
 * 	<li>steam turbines where steam is supplied from a large boiler drum or a large
 * header whose pressure is substantially constant over the period under study
 * </li>
 * 	<li>simple hydro turbines in dam configurations where the water column length
 * is short and water inertia effects are minimal. </li>
 * </ul>
 * Additional information on this model is available in the 2012 IEEE report,
 * <i><u>Dynamic Models for Turbine-Governors in Power System Studies</u></i>,
 * section 3.1.2.3 page 3-4 (GGOV1).
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovCT1 extends TurbineGovernorDynamics {

	/**
	 * Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 0.01.
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
	 * Acceleration limiter gain (Ka).  Typical Value = 10.
	 */
	public PU ka;
	/**
	 * Governor derivative gain (Kdgov).  Typical Value = 0.
	 */
	public PU kdgov;
	/**
	 * Governor integral gain (Kigov).  Typical Value = 2.
	 */
	public PU kigov;
	/**
	 * Load limiter integral gain for PI controller (Kiload).  Typical Value = 0.67.
	 */
	public PU kiload;
	/**
	 * Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to
	 * a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow
	 * acting load controller.  Typical Value = 0.01.
	 */
	public PU kimw;
	/**
	 * Governor proportional gain (Kpgov).  Typical Value = 10.
	 */
	public PU kpgov;
	/**
	 * Load limiter proportional gain for PI controller (Kpload).  Typical Value = 2.
	 */
	public PU kpload;
	/**
	 * Turbine gain (Kturb) (>0).  Typical Value = 1.5.
	 */
	public PU kturb;
	/**
	 * Load limiter reference value (Ldref).  Typical Value = 1.
	 */
	public PU ldref;
	/**
	 * Maximum value for speed error signal (maxerr).  Typical Value = 0.05.
	 */
	public PU maxerr;
	/**
	 * Minimum value for speed error signal (minerr).  Typical Value = -0.05.
	 */
	public PU minerr;
	/**
	 * Base for power values (MWbase) (> 0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Permanent droop (R).  Typical Value = 0.04.
	 */
	public PU r;
	/**
	 * Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -0.1.
	 */
	public Float rclose;
	/**
	 * Maximum rate of load limit decrease (Rdown).  Typical Value = -99.
	 */
	public PU rdown;
	/**
	 * Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 0.10.
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
	 * Acceleration limiter time constant (Ta) (>0).  Typical Value = 0.1.
	 */
	public Seconds ta;
	/**
	 * Actuator time constant (Tact).  Typical Value = 0.5.
	 */
	public Seconds tact;
	/**
	 * Turbine lag time constant (Tb) (>0).  Typical Value = 0.5.
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
	 * Load Limiter time constant (Tfload) (>0).  Typical Value = 3.
	 */
	public Seconds tfload;
	/**
	 * Electrical power transducer time constant (Tpelec) (>0).  Typical Value = 1.
	 */
	public Seconds tpelec;
	/**
	 * Temperature detection lead time constant (Tsa).  Typical Value = 4.
	 */
	public Seconds tsa;
	/**
	 * Temperature detection lag time constant (Tsb).  Typical Value = 5.
	 */
	public Seconds tsb;
	/**
	 * Maximum valve position limit (Vmax).  Typical Value = 1.
	 */
	public PU vmax;
	/**
	 * Minimum valve position limit (Vmin).  Typical Value = 0.15.
	 */
	public PU vmin;
	/**
	 * No load fuel flow (Wfnl).  Typical Value = 0.2.
	 */
	public PU wfnl;
	/**
	 * Switch for fuel source characteristic to recognize that fuel flow, for a given
	 * fuel valve stroke, can be proportional to engine speed (Wfspd).
	 * true = fuel flow proportional to speed (for some gas turbines and diesel
	 * engines with positive displacement fuel injectors)
	 * false = fuel control system keeps fuel flow independent of engine speed.
	 * Typical Value = true.
	 */
	public Boolean wfspd;

	public GovCT1(){

	}
}//end GovCT1