package IEC61968.Common;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Group of people with specific skills, tools, and vehicles.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class Crew extends IdentifiedObject {

	/**
	 * Status of this crew.
	 */
	public Status status;
	/**
	 * Type of this crew.
	 */
	public CrewType CrewType;
	/**
	 * All members of this crew.
	 */
	public CrewMember CrewMembers;

	public Crew(){

	}
}//end Crew