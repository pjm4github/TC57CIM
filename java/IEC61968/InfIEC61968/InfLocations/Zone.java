package IEC61968.InfIEC61968.InfLocations;

import IEC61968.Common.Location;

/**
 * Area divided off from other areas. It may be part of the electrical network, a
 * land area where special restrictions apply, weather areas, etc. For weather, it
 * is an area where a set of relatively homogenous weather measurements apply.
 * @created 29-Dec-2023 6:07:34 PM
 */
public class Zone extends Location {

	/**
	 * Kind of this zone.
	 */
	public ZoneKind kind;

	public Zone(){

	}
}//end Zone