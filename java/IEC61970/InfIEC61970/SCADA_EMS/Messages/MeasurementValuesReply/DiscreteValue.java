package IEC61970.InfIEC61970.SCADA_EMS.Messages.MeasurementValuesReply;

import IEC61970.Base.Domain.Integer;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiscreteValue extends MeasurementValue {

	/**
	 * The value to supervise.
	 */
	public Integer value;

	public DiscreteValue(){

	}
}//end DiscreteValue