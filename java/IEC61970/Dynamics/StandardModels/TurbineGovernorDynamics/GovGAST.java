package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Single shaft gas turbine.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovGAST extends TurbineGovernorDynamics {

	/**
	 * Ambient temperature load limit (Load Limit).  Typical Value = 1.
	 */
	public PU at;
	/**
	 * Turbine damping factor (Dturb).  Typical Value = 0.18.
	 */
	public PU dturb;
	/**
	 * Temperature limiter gain (Kt).  Typical Value = 3.
	 */
	public PU kt;
	/**
	 * Base for power values (MWbase) (> 0).
	 */
	public ActivePower mwbase;
	/**
	 * Permanent droop (R).  Typical Value = 0.04.
	 */
	public PU r;
	/**
	 * Governor mechanism time constant (T1).  T1 represents the natural valve
	 * positioning time constant of the governor for small disturbances, as seen when
	 * rate limiting is not in effect.  Typical Value = 0.5.
	 */
	public Seconds t1;
	/**
	 * Turbine power time constant (T2).  T2 represents delay due to internal energy
	 * storage of the gas turbine engine. T2 can be used to give a rough approximation
	 * to the delay associated with acceleration of the compressor spool of a multi-
	 * shaft engine, or with the compressibility of gas in the plenum of a the free
	 * power turbine of an aero-derivative unit, for example.  Typical Value = 0.5.
	 */
	public Seconds t2;
	/**
	 * Turbine exhaust temperature time constant (T3).  Typical Value = 3.
	 */
	public Seconds t3;
	/**
	 * Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1.
	 */
	public PU vmax;
	/**
	 * Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0.
	 */
	public PU vmin;

	public GovGAST(){

	}
}//end GovGAST