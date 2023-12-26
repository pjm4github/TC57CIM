package IEC61970.Dynamics.StandardModels.TurbineLoadControllerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Turbine Load Controller model developed in the WECC.  This model represents a
 * supervisory turbine load controller that acts to maintain turbine power at a
 * set value by continuous adjustment of the turbine governor speed-load reference.
 * This model is intended to represent slow reset 'outer loop' controllers
 * managing the action of the turbine governor.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TurbLCFB1 extends TurbineLoadControllerDynamics {

	/**
	 * Controller dead band (db).  Typical Value = 0.
	 */
	public PU db;
	/**
	 * Maximum control error (Emax) (note 4).  Typical Value = 0.02.
	 */
	public PU emax;
	/**
	 * Frequency bias gain (Fb).  Typical Value = 0.
	 */
	public PU fb;
	/**
	 * Frequency bias flag (Fbf).
	 * true = enable frequency bias
	 * false = disable frequency bias.
	 * Typical Value = false.
	 */
	public Boolean fbf;
	/**
	 * Maximum turbine speed/load reference bias (Irmax) (note 3).  Typical Value = 0.
	 */
	public PU irmax;
	/**
	 * Integral gain (Ki).  Typical Value = 0.
	 */
	public PU ki;
	/**
	 * Proportional gain (Kp).  Typical Value = 0.
	 */
	public PU kp;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Power controller flag (Pbf).
	 * true = enable load controller
	 * false = disable load controller.
	 * Typical Value = false.
	 */
	public Boolean pbf;
	/**
	 * Power controller setpoint (Pmwset) (note 1).  Unit = MW. Typical Value = 0.
	 */
	public ActivePower pmwset;
	/**
	 * Type of turbine governor reference (Type).
	 * true = speed reference governor
	 * false = load reference governor.
	 * Typical Value = true.
	 */
	public Boolean speedReferenceGovernor;
	/**
	 * Power transducer time constant (Tpelec).  Typical Value = 0.
	 */
	public Seconds tpelec;

	public TurbLCFB1(){

	}
}//end TurbLCFB1