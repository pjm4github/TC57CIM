package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Indication of region for fuel inventory purposes.
 * @updated 28-Dec-2023 12:14:44 PM
 */
public class FuelRegion extends IdentifiedObject {

	/**
	 * The type of fuel region
	 */
	public String fuelRegionType;
	/**
	 * Time of last update
	 */
	public DateTime lastModified;
	public RegisteredGenerator RegisteredGenerator;

	public FuelRegion(){

	}
}//end FuelRegion