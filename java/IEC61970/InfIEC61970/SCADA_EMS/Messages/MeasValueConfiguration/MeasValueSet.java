package IEC61970.InfIEC61970.SCADA_EMS.Messages.MeasValueConfiguration;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Boolean;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MeasValueSet extends IdentifiedObject {

	public PerCent anaogValueDeadband;
	public Boolean reportDiscreteOnChange;
	public MeasurementValue m_MeasurementValue;

	public MeasValueSet(){

	}
}//end MeasValueSet