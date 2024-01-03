package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.RealEnergy;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.DateTime;

/**
 * Data for profile.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class ProfileData {

	/**
	 * Bid price associated with contract
	 */
	public Float bidPrice;
	/**
	 * Capacity level for the profile, in MW.
	 */
	public ActivePower capacityLevel;
	/**
	 * Energy level for the profile, in MWH.
	 */
	public RealEnergy energyLevel;
	/**
	 * Minimum MW value of contract
	 */
	public Float minimumLevel;
	/**
	 * Sequence to provide item numbering for the profile. { greater than or equal to
	 * 1 }
	 */
	public Integer sequenceNumber;
	/**
	 * Start date/time for this profile.
	 */
	public DateTime startDateTime;
	/**
	 * Stop date/time for this profile.
	 */
	public DateTime stopDateTime;

	public ProfileData(){

	}
}//end ProfileData