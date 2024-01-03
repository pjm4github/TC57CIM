package IEC62325.MarketOperations.MarketQualitySystem;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;

/**
 * Model Expected Energy from Market Clearing, interval based.
 * @created 03-Jan-2024 2:07:09 PM
 */
public class ExpectedEnergy {

	public DateTime intervalStartTime;
	public DateTime updateTimeStamp;
	public String updateUser;
	public ExpectedEnergyValues ExpectedEnergyValues;

	public ExpectedEnergy(){

	}
}//end ExpectedEnergy