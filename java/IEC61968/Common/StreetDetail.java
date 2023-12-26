package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Boolean;

/**
 * Street details, in the context of address.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class StreetDetail {

	/**
	 * First line of a free form address or some additional address information (for
	 * example a mail stop).
	 */
	public String addressGeneral;
	/**
	 * (if applicable) Second line of a free form address.
	 */
	public String addressGeneral2;
	/**
	 * (if applicable) Third line of a free form address.
	 */
	public String addressGeneral3;
	/**
	 * (if applicable) In certain cases the physical location of the place of interest
	 * does not have a direct point of entry from the street, but may be located
	 * inside a larger structure such as a building, complex, office block, apartment,
	 * etc.
	 */
	public String buildingName;
	/**
	 * (if applicable) Utilities often make use of external reference systems, such as
	 * those of the town-planner's department or surveyor general's mapping system,
	 * that allocate global reference codes to streets.
	 */
	public String code;
	/**
	 * Name of the street.
	 */
	public String name;
	/**
	 * Designator of the specific location on the street.
	 */
	public String number;
	/**
	 * Prefix to the street name. For example: North, South, East, West.
	 */
	public String prefix;
	/**
	 * Suffix to the street name. For example: North, South, East, West.
	 */
	public String suffix;
	/**
	 * Number of the apartment or suite.
	 */
	public String suiteNumber;
	/**
	 * Type of street. Examples include: street, circle, boulevard, avenue, road,
	 * drive, etc.
	 */
	public String type;
	/**
	 * True if this street is within the legal geographical boundaries of the
	 * specified town (default).
	 */
	public Boolean withinTownLimits;

	public StreetDetail(){

	}
}//end StreetDetail