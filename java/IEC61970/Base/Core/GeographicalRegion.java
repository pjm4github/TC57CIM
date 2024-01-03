package IEC61970.Base.Core;


/**
 * A geographical region of a power system network model.
 * @created 02-Jan-2024 10:34:18 PM
 */
public class GeographicalRegion extends IdentifiedObject {

	/**
	 * All sub-geograhpical regions within this geographical region.
	 */
	public SubGeographicalRegion Regions;

	public GeographicalRegion(){

	}
}//end GeographicalRegion