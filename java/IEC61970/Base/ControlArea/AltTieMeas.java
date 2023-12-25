package TC57CIM.IEC61970.Base.ControlArea;

import TC57CIM.IEC61970.Base.Domain.Integer;
import TC57CIM.IEC61970.Base.Meas.AnalogValue;
import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * A prioritized measurement to be used for the tie flow as part of the control
 * area specification.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class AltTieMeas extends IdentifiedObject {

	/**
	 * Priority of a measurement usage.   Lower numbers have first priority.
	 */
	public Integer priority;
	/**
	 * The specific analog value used as a source.
	 */
	public AnalogValue AnalogValue;

	public AltTieMeas(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}