package IEC61968.Operations;

import IEC61968.Common.CrewMember;

/**
 * Crew member on work site responsible for all local safety measures for the work
 * crew doing maintenance, construction and repair in a substation or on a power
 * line/cable.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class FieldSafetySupervisor extends CrewMember {

	/**
	 * All safety documents released by this supervisor.
	 */
	public SafetyDocument ReleasedSafetyDocuments;
	/**
	 * All safety documents issued to this supervisor.
	 */
	public SafetyDocument IssuedSafetyDocuments;

	public FieldSafetySupervisor(){

	}
}//end FieldSafetySupervisor