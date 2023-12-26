package IEC62325.Environmental;

import IEC61970.Base.Domain.Pressure;
import IEC61970.Base.Domain.Speed;
import IEC61970.Base.Domain.Integer;

/**
 * A cyclone (or tropical cyclone), a rapidly-rotating storm system characterized
 * by a low-pressure center, strong winds, and a spiral arrangement of
 * thunderstorms that produce heavy rain.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class Cyclone extends AtmosphericPhenomenon {

	/**
	 * The central pressure of the cyclone during the time interval.
	 */
	public Pressure centralPressure;
	/**
	 * The maximum surface wind speed of the cyclone during the time interval.
	 */
	public Speed maxSurfaceWindSpeed;
	/**
	 * Wind Force as classified on the Beaufort Scale (0-12) during the time interval.
	 */
	public Integer windForce;

	public Cyclone(){

	}
}//end Cyclone