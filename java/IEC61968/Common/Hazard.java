package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An object or a condition that is a danger for causing loss or perils to an
 * asset and/or people.
 * @created 03-Jan-2024 12:12:18 PM
 */
public class Hazard extends IdentifiedObject {

	/**
	 * Status of this hazard.
	 */
	public Status status;
	/**
	 * Type of this hazard.
	 */
	public String type;

	public Hazard(){

	}
}//end Hazard