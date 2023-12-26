package IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;

/**
 * The class represents IEEE VAR Controller Type 1 which operates by moving the
 * voltage reference directly.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 11.3.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PFVArType1IEEEVArController extends PFVArControllerType1Dynamics {

	/**
	 * Var controller time delay (<i>T</i><i><sub>VARC</sub></i>).  Typical Value = 5.
	 */
	public Seconds tvarc;
	/**
	 * Synchronous machine power factor (<i>V</i><i><sub>VAR</sub></i>).
	 */
	public PU vvar;
	/**
	 * Var controller dead band (<i>V</i><i><sub>VARC_BW</sub></i>).  Typical Value =
	 * 0.02.
	 */
	public Float vvarcbw;
	/**
	 * Var controller reference (<i>V</i><i><sub>VARREF</sub></i>).
	 */
	public PU vvarref;
	/**
	 * Maximum machine terminal voltage needed for pf/var controller to be enabled
	 * (<i>V</i><i><sub>VTMAX</sub></i>).
	 */
	public PU vvtmax;
	/**
	 * Minimum machine terminal voltage needed to enable pf/var controller
	 * (<i>V</i><i><sub>VTMIN</sub></i>).
	 */
	public PU vvtmin;

	public PFVArType1IEEEVArController(){

	}
}//end PFVArType1IEEEVArController