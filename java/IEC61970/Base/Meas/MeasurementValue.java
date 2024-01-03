package IEC61970.Base.Meas;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.SCADA.RemoteSource;
import IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasurementValueExt;

/**
 * The current state for a measurement. A state value is an instance of a
 * measurement from a specific source. Measurements can be associated with many
 * state values, each representing a different source for the measurement.
 * @created 02-Jan-2024 11:19:54 PM
 */
public class MeasurementValue extends IOPoint MeasurementValueExt {

	/**
	 * The limit, expressed as a percentage of the sensor maximum, that errors will
	 * not exceed when the sensor is used under  reference conditions.
	 */
	public PerCent sensorAccuracy;
	/**
	 * The time when the value was last updated
	 */
	public DateTime timeStamp;
	/**
	 * Link to the physical telemetered point associated with this measurement.
	 */
	public RemoteSource RemoteSource;
	/**
	 * A MeasurementValue has a MeasurementValueQuality associated with it.
	 */
	public MeasurementValueQuality MeasurementValueQuality;

	public MeasurementValue(){

	}
}//end MeasurementValue