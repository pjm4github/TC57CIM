package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast
 * valving.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class GovSteamFV3 extends TurbineGovernorDynamics {

	/**
	 * Governor gain, (reciprocal of droop) (K).  Typical Value = 20.
	 */
	public PU k;
	/**
	 * Fraction of turbine power developed after first boiler pass (K1).  Typical
	 * Value = 0.2.
	 */
	public PU k1;
	/**
	 * Fraction of turbine power developed after second boiler pass (K2).  Typical
	 * Value = 0.2.
	 */
	public PU k2;
	/**
	 * Fraction of hp turbine power developed after crossover or third boiler pass
	 * (K3). Typical Value = 0.6.
	 */
	public PU k3;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Maximum valve opening, PU of MWbase (Pmax).  Typical Value = 1.
	 */
	public PU pmax;
	/**
	 * Minimum valve opening, PU of MWbase (Pmin).  Typical Value = 0.
	 */
	public PU pmin;
	/**
	 * Max. pressure in reheater (Prmax).  Typical Value = 1.
	 */
	public PU prmax;
	/**
	 * Governor lead time constant (T1).  Typical Value = 0.
	 */
	public Seconds t1;
	/**
	 * Governor lag time constant (T2).  Typical Value = 0.
	 */
	public Seconds t2;
	/**
	 * Valve positioner time constant (T3).  Typical Value = 0.
	 */
	public Seconds t3;
	/**
	 * Inlet piping/steam bowl time constant (T4).  Typical Value = 0.2.
	 */
	public Seconds t4;
	/**
	 * Time constant of second boiler pass (i.e. reheater) (T5).  Typical Value = 0.5.
	 */
	public Seconds t5;
	/**
	 * Time constant of crossover or third boiler pass (T6).  Typical Value = 10.
	 */
	public Seconds t6;
	/**
	 * Time to close intercept valve (IV) (Ta).  Typical Value = 0.97.
	 */
	public Seconds ta;
	/**
	 * Time until IV starts to reopen (Tb).  Typical Value = 0.98.
	 */
	public Seconds tb;
	/**
	 * Time until IV is fully open (Tc).  Typical Value = 0.99.
	 */
	public Seconds tc;
	/**
	 * Maximum valve closing velocity (Uc).  Unit = PU/sec.  Typical Value = -1.
	 */
	public Float uc;
	/**
	 * Maximum valve opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1.
	 */
	public Float uo;

	public GovSteamFV3(){

	}
}//end GovSteamFV3