package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Basic Hydro turbine governor model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class GovHydro1 extends TurbineGovernorDynamics {

	/**
	 * Turbine gain (At) (>0).  Typical Value = 1.2.
	 */
	public PU at;
	/**
	 * Turbine damping factor (Dturb) (>=0).  Typical Value = 0.5.
	 */
	public PU dturb;
	/**
	 * Maximum gate opening (Gmax) (>0).  Typical Value = 1.
	 */
	public PU gmax;
	/**
	 * Minimum gate opening (Gmin) (>=0).  Typical Value = 0.
	 */
	public PU gmin;
	/**
	 * Turbine nominal head (hdam).  Typical Value = 1.
	 */
	public PU hdam;
	/**
	 * Base for power values (MWbase) (> 0).  Unit = MW.
	 */
	public ActivePower mwbase;
	/**
	 * No-load flow at nominal head (qnl) (>=0).  Typical Value = 0.08.
	 */
	public PU qnl;
	/**
	 * Permanent droop (R) (>0).  Typical Value = 0.04.
	 */
	public PU rperm;
	/**
	 * Temporary droop (r) (>R).  Typical Value = 0.3.
	 */
	public PU rtemp;
	/**
	 * Filter time constant (<i>Tf</i>) (>0).  Typical Value = 0.05.
	 */
	public Seconds tf;
	/**
	 * Gate servo time constant (Tg) (>0).  Typical Value = 0.5.
	 */
	public Seconds tg;
	/**
	 * Washout time constant (Tr) (>0).  Typical Value = 5.
	 */
	public Seconds tr;
	/**
	 * Water inertia time constant (Tw) (>0).  Typical Value = 1.
	 */
	public Seconds tw;
	/**
	 * Maximum gate velocity (Vlem) (>0).  Typical Value = 0.2.
	 */
	public Float velm;

	public GovHydro1(){

	}
}//end GovHydro1