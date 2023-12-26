package IEC61970.InfIEC61970.SCADA_EMS.Messages.MeasurementValuesReply;

import IEC61970.Base.Domain.Float;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AnalogValue extends MeasurementValue {

	/**
	 * The value to supervise.
	 */
	public Float value;

	public AnalogValue(){

	}
}//end AnalogValue