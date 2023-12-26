package IEC61968.Common;

import IEC61970.Base.Domain.String;

/**
 * the enumerated values for the dispatch status
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum CrewStatusKind {
	/**
	 * Indicates that one or more crews have arrived at the work site
	 */
	arrived,
	/**
	 * Indicates that one or more crews have been assigned to the work
	 */
	assigned,
	/**
	 * Indicates that the work is awaiting one or more crews to be assigned
	 */
	awaitingCrewAssignment,
	/**
	 * Indicates that one or more crews are traveling to the work site(s)
	 */
	enroute,
	/**
	 * Indicates that the work at one or more work sites has been completed
	 */
	fieldComplete
}