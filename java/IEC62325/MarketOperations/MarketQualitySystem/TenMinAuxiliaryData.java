package IEC62325.MarketOperations.MarketQualitySystem;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;

/**
 * Models 10-Minutes Auxiliary Data.
 * @created 03-Jan-2024 2:07:09 PM
 */
public class TenMinAuxiliaryData {

	public DateTime intervalStartTime;
	public DateTime updateTimeStamp;
	public String updateUser;
	public AuxiliaryValues AuxillaryData;

	public TenMinAuxiliaryData(){

	}
}//end TenMinAuxiliaryData