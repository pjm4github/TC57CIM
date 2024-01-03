package IEC61968.InfIEC61968.InfLocations;

import IEC61968.Common.Status;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Common.Location;

/**
 * Route that is followed, for example by service crews.
 * @created 29-Dec-2023 6:07:16 PM
 */
public class Route extends IdentifiedObject {

	public Status status;
	/**
	 * Classification by utility's work management standards and practices.
	 */
	public String type;
	public Location Locations;

	public Route(){

	}
}//end Route