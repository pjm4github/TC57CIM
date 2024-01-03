package IEC61968.Work;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Length;

/**
 * Vehicle asset.
 * @created 02-Jan-2024 10:07:00 PM
 */
public class Vehicle extends WorkAsset {

	/**
	 * Date and time the last odometer reading was recorded.
	 */
	public DateTime odometerReadDateTime;
	/**
	 * Odometer reading of this vehicle as of the 'odometerReadingDateTime'. Refer to
	 * associated ActivityRecords for earlier readings.
	 */
	public Length odometerReading;
	/**
	 * Kind of usage of the vehicle.
	 */
	public VehicleUsageKind usageKind;

	public Vehicle(){

	}
}//end Vehicle