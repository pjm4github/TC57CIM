package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.String;

/**
 * Describing users of a Scheduling Coordinator.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class SchedulingCoordinatorUser {

	/**
	 * Login ID
	 */
	public String loginID;
	/**
	 * Assigned roles (these are roles with either Read or Read/Write privileges on
	 * different Market Systems)
	 */
	public String loginRole;

	public SchedulingCoordinatorUser(){

	}
}//end SchedulingCoordinatorUser