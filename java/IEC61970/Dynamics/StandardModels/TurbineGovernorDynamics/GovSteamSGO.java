package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Simplified Steam turbine governor model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class GovSteamSGO extends TurbineGovernorDynamics {

	/**
	 * One/per unit regulation (K1). 
	 */
	public PU k1;
	/**
	 * Fraction (K2). 
	 */
	public PU k2;
	/**
	 * Fraction (K3).
	 */
	public PU k3;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Upper power limit (Pmax). 
	 */
	public PU pmax;
	/**
	 * Lower power limit (Pmin).
	 */
	public Seconds pmin;
	/**
	 * Controller lag (T1).
	 */
	public Seconds t1;
	/**
	 * Controller lead compensation (T2).
	 */
	public Seconds t2;
	/**
	 * Governor lag (T3) (>0). 
	 */
	public Seconds t3;
	/**
	 * Delay due to steam inlet volumes associated with steam chest and inlet piping
	 * (T4). 
	 */
	public Seconds t4;
	/**
	 * Reheater delay including hot and cold leads (T5). 
	 */
	public Seconds t5;
	/**
	 * Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6). 
	 */
	public Seconds t6;

	public GovSteamSGO(){

	}
}//end GovSteamSGO