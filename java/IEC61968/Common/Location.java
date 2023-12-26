package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Meas.Measurement;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Base.Core.PowerSystemResource;
import IEC61968.Operations.SwitchingOrder;

/**
 * The place, scene, or point of something where someone or something has been, is,
 * and/or will be at a given moment in time. It can be defined with one or more
 * postition points (coordinates) in a given coordinate system.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class Location extends IdentifiedObject {

	/**
	 * (if applicable) Direction that allows field crews to quickly find a given asset.
	 * For a given location, such as a street address, this is the relative direction
	 * in which to find the asset. For example, a streetlight may be located at the
	 * 'NW' (northwest) corner of the customer's site, or a usage point may be located
	 * on the second floor of an apartment building.
	 */
	public String direction;
	/**
	 * Electronic address.
	 */
	public ElectronicAddress electronicAddress;
	/**
	 * (if applicable) Reference to geographical information source, often external to
	 * the utility.
	 */
	public String geoInfoReference;
	/**
	 * Main address of the location.
	 */
	public StreetAddress mainAddress;
	/**
	 * Phone number.
	 */
	public TelephoneNumber phone1;
	/**
	 * Additional phone number.
	 */
	public TelephoneNumber phone2;
	/**
	 * Secondary address of the location. For example, PO Box address may have
	 * different ZIP code than that in the 'mainAddress'.
	 */
	public StreetAddress secondaryAddress;
	/**
	 * Status of this location.
	 */
	public Status status;
	/**
	 * Classification by utility's corporate standards and practices, relative to the
	 * location itself (e.g., geographical, functional accounting, etc., not a given
	 * property that happens to exist at that location).
	 */
	public String type;
	public Measurement Measurements;
	/**
	 * Coordinate system used to describe position points of this location.
	 */
	public CoordinateSystem CoordinateSystem;
	/**
	 * All power system resources at this location.
	 */
	public PowerSystemResource PowerSystemResources;
	/**
	 * All configuration events created for this location.
	 */
	public ConfigurationEvent ConfigurationEvents;
	public Crew Crew;
	public SwitchingOrder SwitchingOrder;
	/**
	 * Sequence of position points describing this location, expressed in coordinate
	 * system 'Location.CoordinateSystem'.
	 */
	public PositionPoint PositionPoints;

	public Location(){

	}
}//end Location