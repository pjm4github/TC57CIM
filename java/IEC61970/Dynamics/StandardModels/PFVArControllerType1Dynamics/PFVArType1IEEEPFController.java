package IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;

/**
 * The class represents IEEE PF Controller Type 1 which operates by moving the
 * voltage reference directly.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 11.2.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PFVArType1IEEEPFController extends PFVArControllerType1Dynamics {

	/**
	 * Overexcitation Flag (<i>OVEX</i>)
	 * true = overexcited
	 * false = underexcited.
	 */
	public Boolean ovex;
	/**
	 * PF controller time delay (<i>T</i><i><sub>PFC</sub></i>).  Typical Value = 5.
	 */
	public Seconds tpfc;
	/**
	 * Minimum machine terminal current needed to enable pf/var controller
	 * (<i>V</i><i><sub>ITMIN</sub></i>).
	 */
	public PU vitmin;
	/**
	 * Synchronous machine power factor (<i>V</i><i><sub>PF</sub></i>).
	 */
	public PU vpf;
	/**
	 * PF controller dead band (<i>V</i><i><sub>PFC_BW</sub></i>).  Typical Value = 0.
	 * 05.
	 */
	public Float vpfcbw;
	/**
	 * PF controller reference (<i>V</i><i><sub>PFREF</sub></i>).
	 */
	public PU vpfref;
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

	public PFVArType1IEEEPFController(){

	}
}//end PFVArType1IEEEPFController