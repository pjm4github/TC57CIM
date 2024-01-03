package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Status;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61968.InfIEC61968.InfCommon.OldCrew;
import IEC61968.InfIEC61968.InfCommon.Craft;

/**
 * Capabilities of a crew.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class Capability extends WorkIdentifiedObject {

	/**
	 * Capability performance factor.
	 */
	public String performanceFactor;
	public Status status;
	/**
	 * Classification by utility's work management standards and practices.
	 */
	public String type;
	/**
	 * Date and time interval for which this capability is valid (when it became
	 * effective and when it expires).
	 */
	public DateTimeInterval validityInterval;
	public OldWorkTask WorkTasks;
	public OldCrew Crew;
	public Craft Crafts;

	public Capability(){

	}
}//end Capability