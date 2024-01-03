package IEC61968.InfIEC61968.InfCommon;

import IEC61970.Base.Domain.String;
import IEC61968.InfIEC61968.InfLocations.Route;
import IEC61968.InfIEC61968.InfWork.Assignment;
import IEC61968.InfIEC61968.InfWork.ShiftPattern;
import IEC61968.Common.Crew;
import IEC61968.Common.Location;

/**
 * A crew is a group of people with specific skills, tools, and vehicles.
 * @created 29-Dec-2023 6:01:39 PM
 */
public class OldCrew extends Crew {

	/**
	 * Classification by utility's work management standards and practices.
	 */
	public String type;
	public Route Route;
	/**
	 * All Assignments for this Crew.
	 */
	public Assignment Assignments;
	public ShiftPattern ShiftPatterns;
	public Location Locations;

	public OldCrew(){

	}
}//end OldCrew