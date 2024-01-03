package IEC61968.InfIEC61968.InfLocations;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Agreement;

/**
 * A grant provides a right, as defined by type, for a parcel of land. Note that
 * the association to Location, Asset, Organisation, etc. for the Grant is
 * inherited from Agreement, a type of Document.
 * @created 29-Dec-2023 6:06:41 PM
 */
public class LocationGrant extends Agreement {

	/**
	 * Property related information that describes the Grant's land parcel. For
	 * example, it may be a deed book number, deed book page number, and parcel number.
	 */
	public String propertyData;

	public LocationGrant(){

	}
}//end LocationGrant