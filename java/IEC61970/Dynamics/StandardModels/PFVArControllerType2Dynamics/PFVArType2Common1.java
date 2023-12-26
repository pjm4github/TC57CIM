package IEC61970.Dynamics.StandardModels.PFVArControllerType2Dynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;

/**
 * Power factor / Reactive power regulator. This model represents the power factor
 * or reactive power controller such as the Basler SCP-250. The controller
 * measures power factor or reactive power (PU on generator rated power) and
 * compares it with the operator's set point.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PFVArType2Common1 extends PFVArControllerType2Dynamics {

	/**
	 * Selector (J).
	 * true = control mode for reactive power
	 * false = control mode for power factor.
	 */
	public Boolean j;
	/**
	 * Reset gain (Ki).
	 */
	public PU ki;
	/**
	 * Proportional gain (Kp).
	 */
	public PU kp;
	/**
	 * Output limit (max).
	 */
	public PU max;
	/**
	 * Reference value of reactive power or power factor (Ref).
	 * The reference value is initialised by this model. This initialisation may
	 * override the value exchanged by this attribute to represent a plant operator's
	 * change of the reference setting.
	 */
	public PU ref;

	public PFVArType2Common1(){

	}
}//end PFVArType2Common1