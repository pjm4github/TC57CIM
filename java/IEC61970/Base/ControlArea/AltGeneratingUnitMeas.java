package IEC61970.Base.ControlArea;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Meas.AnalogValue;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A prioritized measurement to be used for the generating unit in the control
 * area specificaiton.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AltGeneratingUnitMeas extends IdentifiedObject {

	/**
	 * Priority of a measurement usage.   Lower numbers have first priority.
	 */
	public Integer priority;
	/**
	 * The specific analog value used as a source.
	 */
	public AnalogValue AnalogValue;

	public AltGeneratingUnitMeas(){

	}
}//end AltGeneratingUnitMeas