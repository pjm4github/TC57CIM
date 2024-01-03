package IEC61968.InfIEC61968.InfLocations;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Agreement;

/**
 * A right-of-way (ROW) is for land where it is lawful to use for a public road,
 * an electric power line, etc. Note that the association to Location, Asset,
 * Organisation, etc. for the Grant is inherited from Agreement, a type of
 * Document.
 * @created 29-Dec-2023 6:07:05 PM
 */
public class RightOfWay extends Agreement {

	/**
	 * Property related information that describes the ROW's land parcel. For example,
	 * it may be a deed book number, deed book page number, and parcel number.
	 */
	public String propertyData;
	/**
	 * All land properties this right of way applies to.
	 */
	public LandProperty LandProperties;

	public RightOfWay(){

	}
}//end RightOfWay