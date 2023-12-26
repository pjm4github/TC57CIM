package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * A simplified steam turbine governor model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovSteam0 extends TurbineGovernorDynamics {

	/**
	 * Turbine damping coefficient (Dt).  Unit = delta P / delta speed. Typical Value
	 * = 0.
	 */
	public PU dt;
	/**
	 * Base for power values (MWbase)  (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Permanent droop (R).  Typical Value = 0.05.
	 */
	public PU r;
	/**
	 * Steam bowl time constant (T1).  Typical Value = 0.5.
	 */
	public Seconds t1;
	/**
	 * Numerator time constant of T2/T3 block (T2).  Typical Value = 3.
	 */
	public Seconds t2;
	/**
	 * Reheater time constant (T3).  Typical Value = 10.
	 */
	public Seconds t3;
	/**
	 * Maximum valve position, PU of mwcap (Vmax).  Typical Value = 1.
	 */
	public PU vmax;
	/**
	 * Minimum valve position, PU of mwcap (Vmin).  Typical Value = 0.
	 */
	public PU vmin;

	public GovSteam0(){

	}
}//end GovSteam0