package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Steam turbine governor with reheat time constants and modeling of the effects
 * of fast valve closing to reduce mechanical power.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class GovSteamFV2 extends TurbineGovernorDynamics {

	/**
	 * (Dt).
	 */
	public PU dt;
	/**
	 * Fraction of the turbine power developed by turbine sections not involved in
	 * fast valving (K).
	 */
	public PU k;
	/**
	 * Alternate Base used instead of Machine base in equipment model if necessary
	 * (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * (R).
	 */
	public PU r;
	/**
	 * Governor time constant (T1).
	 */
	public Seconds t1;
	/**
	 * Reheater time constant (T3).
	 */
	public Seconds t3;
	/**
	 * Time after initial time for valve to close (Ta).
	 */
	public Seconds ta;
	/**
	 * Time after initial time for valve to begin opening (Tb).
	 */
	public Seconds tb;
	/**
	 * Time after initial time for valve to become fully open (Tc).
	 */
	public Seconds tc;
	/**
	 * Initial time to begin fast valving (Ti).
	 */
	public Seconds ti;
	/**
	 * Time constant with which power falls off after intercept valve closure (Tt).
	 */
	public Seconds tt;
	/**
	 * (Vmax).
	 */
	public PU vmax;
	/**
	 * (Vmin).
	 */
	public PU vmin;

	public GovSteamFV2(){

	}
}//end GovSteamFV2