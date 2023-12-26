package IEC61970.Dynamics.StandardModels.PFVArControllerType2Dynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;

/**
 * The class represents IEEE PF Controller Type 2 which is a summing point type
 * controller and makes up the outside loop of a two-loop system. This controller
 * is implemented as a slow PI type controller. The voltage regulator forms the
 * inner loop and is implemented as a fast controller.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 11.4.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PFVArType2IEEEPFController extends PFVArControllerType2Dynamics {

	/**
	 * Overexcitation or under excitation flag (<i>EXLON</i>)
	 * true = 1 (not in the overexcitation or underexcitation state, integral action
	 * is active)
	 * false = 0 (in the overexcitation or underexcitation state, so integral action
	 * is disabled to allow the limiter to play its role).
	 */
	public Boolean exlon;
	/**
	 * Integral gain of the pf controller (<i>K</i><i><sub>I</sub></i>).  Typical
	 * Value = 1.
	 */
	public PU ki;
	/**
	 * Proportional gain of the pf controller (<i>K</i><i><sub>P</sub></i>).  Typical
	 * Value = 1.
	 */
	public PU kp;
	/**
	 * Power factor reference (<i>P</i><i><sub>FREF</sub></i>).
	 */
	public PU pfref;
	/**
	 * Maximum output of the pf controller (<i>V</i><i><sub>CLMT</sub></i>).  Typical
	 * Value = 0.1.
	 */
	public PU vclmt;
	/**
	 * Voltage regulator reference (<i>V</i><i><sub>REF</sub></i>).
	 */
	public PU vref;
	/**
	 * Generator sensing voltage (<i>V</i><i><sub>S</sub></i>).
	 */
	public Float vs;

	public PFVArType2IEEEPFController(){

	}
}//end PFVArType2IEEEPFController