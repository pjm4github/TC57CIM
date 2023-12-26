package IEC61968.Assets;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;

/**
 * Acceptance test for assets.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:18 PM
 */
public class AcceptanceTest {

	/**
	 * Date and time the asset was last tested using the 'type' of test and yielding
	 * the current status in 'success' attribute.
	 */
	public DateTime dateTime;
	/**
	 * True if asset has passed acceptance test and may be placed in or is in service.
	 * It is set to false if asset is removed from service and is required to be
	 * tested again before being placed back in service, possibly in a new location.
	 * Since asset may go through multiple tests during its lifecycle, the date of
	 * each acceptance test may be recorded in 'Asset.ActivityRecord.status.dateTime'.
	 */
	public Boolean success;
	/**
	 * Type of test or group of tests that was conducted on 'dateTime'.
	 */
	public String type;

	public AcceptanceTest(){

	}
}//end AcceptanceTest