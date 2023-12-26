package IEC61970.InfIEC61970.SCADA_EMS.Messages.MeasValueConfigurationReply;


/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MeasurementValue extends IdentifiedObject MeasurementValueExt {

	public MeasValueSet m_MeasValueSet;
	public MeasurementValueQuality m_MeasurementValueQuality;

	public MeasurementValue(){

	}
}//end MeasurementValue