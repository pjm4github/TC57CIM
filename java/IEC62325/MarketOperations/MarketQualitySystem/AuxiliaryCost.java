package IEC62325.MarketOperations.MarketQualitySystem;

import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC61970.Base.Domain.String;

/**
 * Models Market clearing results for Auxiliary costs.
 * @created 03-Jan-2024 2:07:09 PM
 */
public class AuxiliaryCost {

	public DateTime intervalStartTime;
	public MarketType marketType;
	public DateTime updateTimeStamp;
	public String updateUser;
	public AuxiliaryValues AuxillaryValues;

	public AuxiliaryCost(){

	}
}//end AuxiliaryCost