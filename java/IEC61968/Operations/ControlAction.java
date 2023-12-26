package IEC61968.Operations;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Meas.Control;

/**
 * Control executed as a switching step.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class ControlAction extends SwitchingAction {

	/**
	 * The analog value used for the analog control, the raise/lower control and the
	 * set point control
	 */
	public Float analogValue;
	/**
	 * The integer value used for the command or the accumulator reset.
	 */
	public Integer discreteValue;
	public Control Control;

	public ControlAction(){

	}
}//end ControlAction