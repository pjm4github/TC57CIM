package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;

/**
 * Cross compound turbine governor model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class GovSteamCC extends TurbineGovernorDynamics {

	/**
	 * HP damping factor (Dhp).  Typical Value = 0.
	 */
	public PU dhp;
	/**
	 * LP damping factor (Dlp).  Typical Value = 0.
	 */
	public PU dlp;
	/**
	 * Fraction of HP power ahead of reheater (Fhp).  Typical Value = 0.3.
	 */
	public PU fhp;
	/**
	 * Fraction of LP power ahead of reheater (Flp).  Typical Value = 0.7.
	 */
	public PU flp;
	/**
	 * Base for power values (MWbase) (>0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * Maximum HP value position (Pmaxhp).  Typical Value = 1.
	 */
	public PU pmaxhp;
	/**
	 * Maximum LP value position (Pmaxlp).  Typical Value = 1.
	 */
	public PU pmaxlp;
	/**
	 * HP governor droop (Rhp).  Typical Value = 0.05.
	 */
	public PU rhp;
	/**
	 * LP governor droop (Rlp).  Typical Value = 0.05.
	 */
	public PU rlp;
	/**
	 * HP governor time constant (T1hp).  Typical Value = 0.1.
	 */
	public Seconds t1hp;
	/**
	 * LP governor time constant (T1lp).  Typical Value = 0.1.
	 */
	public Seconds t1lp;
	/**
	 * HP turbine time constant (T3hp).  Typical Value = 0.1.
	 */
	public Seconds t3hp;
	/**
	 * LP turbine time constant (T3lp).  Typical Value = 0.1.
	 */
	public Seconds t3lp;
	/**
	 * HP turbine time constant (T4hp).  Typical Value = 0.1.
	 */
	public Seconds t4hp;
	/**
	 * LP turbine time constant (T4lp).  Typical Value = 0.1.
	 */
	public Seconds t4lp;
	/**
	 * HP reheater time constant (T5hp).  Typical Value = 10.
	 */
	public Seconds t5hp;
	/**
	 * LP reheater time constant (T5lp).  Typical Value = 10.
	 */
	public Seconds t5lp;

	public GovSteamCC(){

	}
}//end GovSteamCC