package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.Profile;

/**
 * A type of profile for financial charges.
 * @created 28-Dec-2023 8:18:35 PM
 */
public class ChargeProfile extends Profile {

	/**
	 * The calculation frequency, daily or monthly. 
	 */
	public String frequency;
	/**
	 * The number of intervals in the profile data.
	 */
	public Integer numberInterval;
	/**
	 * The type of profile.  It could be amount, price, or quantity.
	 */
	public String type;
	/**
	 * The unit of measure applied to the value attribute of the profile data.
	 */
	public String unitOfMeasure;
	public BillDeterminant BillDeterminant;
	public ChargeProfileData ChargeProfileData;
	public PassThroughBill PassTroughBill;

	public ChargeProfile(){

	}
}//end ChargeProfile