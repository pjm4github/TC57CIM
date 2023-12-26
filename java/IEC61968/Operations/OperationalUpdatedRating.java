package IEC61968.Operations;

import IEC61970.Base.Domain.String;

/**
 * Lowered capability because of deterioration or inadequacy (sometimes referred
 * to as derating or partial outage) or other kind of operational rating change.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OperationalUpdatedRating extends OperationalRestriction {

	/**
	 * Type of operational updated rating, e.g. a derate, a rerate or a return to
	 * normal.
	 */
	public String changeType;
	/**
	 * Planned equipment outage with this updated rating.
	 */
	public PlannedOutage PlannedOutage;

	public OperationalUpdatedRating(){

	}
}//end OperationalUpdatedRating