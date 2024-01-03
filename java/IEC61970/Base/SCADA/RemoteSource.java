package IEC61970.Base.SCADA;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Remote sources are state variables that are telemetered or calculated within
 * the remote unit.
 * @created 02-Jan-2024 11:29:44 PM
 */
public class RemoteSource extends RemotePoint {

	/**
	 * The smallest change in value to be reported.
	 */
	public Float deadband;
	/**
	 * The time interval between scans.
	 */
	public Seconds scanInterval;
	/**
	 * The maximum value the telemetry item can return.
	 */
	public Float sensorMaximum;
	/**
	 * The minimum value the telemetry item can return.
	 */
	public Float sensorMinimum;

	public RemoteSource(){

	}
}//end RemoteSource