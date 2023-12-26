package IEC61970.InfIEC61970.SCADA_EMS.Meas;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MeasValueConfiguration extends IdentifiedObject {

	public Seconds keepAliveTime;
	public Boolean readAllValues;
	public DateTime sampleTime;
	public Seconds sampleTimeDeviation;

	public MeasValueConfiguration(){

	}
}//end MeasValueConfiguration