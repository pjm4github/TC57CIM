package IEC61968.Assets;

import IEC61970.Base.Domain.Date;

/**
 * Dates associated with asset 'in use' status. May have multiple in use dates for
 * this device and a compound type allows a query to return multiple dates.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class InUseDate {

	/**
	 * Date asset was most recently put in use.
	 */
	public Date inUseDate;
	/**
	 * Date of most recent asset transition to not ready for use state.
	 */
	public Date notReadyForUseDate;
	/**
	 * Date of most recent asset transition to ready for use state.
	 */
	public Date readyForUseDate;

	public InUseDate(){

	}
}//end InUseDate