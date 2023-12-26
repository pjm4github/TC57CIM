package IEC61970.InfIEC61970.SCADA_EMS.Messages.MeasurementValues;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTime;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MeasValueConfiguration extends IdentifiedObject {

	public Boolean readAllValues;
	public DateTime sampleTime;
	public MeasValueSet m_MeasValueSet;

	public MeasValueConfiguration(){

	}
}//end MeasValueConfiguration