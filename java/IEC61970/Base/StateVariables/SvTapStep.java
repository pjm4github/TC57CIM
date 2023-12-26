package IEC61970.Base.StateVariables;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Wires.TapChanger;

/**
 * State variable for transformer tap step.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class SvTapStep extends StateVariable {

	/**
	 * The floating point tap position.   This is not the tap ratio, but rather the
	 * tap step position as defined by the related tap changer model and normally is
	 * constrained to be within the range of minimum and maximum tap positions.
	 */
	public Float position;
	/**
	 * The tap changer associated with the tap step state.
	 */
	public TapChanger TapChanger;

	public SvTapStep(){

	}
}//end SvTapStep