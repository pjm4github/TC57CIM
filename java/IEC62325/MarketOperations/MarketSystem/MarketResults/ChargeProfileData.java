package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;

/**
 * Model of various charges associated with an energy profile to support billing
 * and settlement.
 * @created 28-Dec-2023 8:18:48 PM
 */
public class ChargeProfileData {

	/**
	 * The sequence number of the profile.
	 */
	public Integer sequence;
	/**
	 * The date and time of an interval.
	 */
	public DateTime timeStamp;
	/**
	 * The value of an interval given a profile type (amount, price, or quantity),
	 * subject to the UOM. 
	 */
	public Float value;

	public ChargeProfileData(){

	}
}//end ChargeProfileData