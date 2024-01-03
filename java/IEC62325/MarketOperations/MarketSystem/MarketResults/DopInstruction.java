package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MQSCHGType;
import IEC61970.Base.Domain.String;

/**
 * Provides the necessary information (on a resource basis) to capture the
 * Dispatch Operating Point (DOP) results on a Dispatch interval. This information
 * is only relevant to the RT interval market.
 * @created 28-Dec-2023 8:19:57 PM
 */
public class DopInstruction {

	/**
	 * Dispatched Operating Point (MW)
	 */
	public ActivePower mwDOP;
	/**
	 * A value used to establish priority of the DOP when plotting.  This is only
	 * applicable when two DOPs exist for the same time, but with different MW values.
	 * E.g. when indicating a step in the curve.  Its used to determine if the curve
	 * steps up or down.
	 */
	public Integer plotPriority;
	/**
	 * Indication of DOP validity.
	 * 
	 * Shows the DOP is calculated from the latest run (YES). A NO indicator shows
	 * that the DOP is copied from a previous execution.
	 * 
	 * Up to 2 intervals can be missed.
	 */
	public YesNo runIndicatorDOP;
	/**
	 * DOP time stamp
	 */
	public DateTime timestampDOP;
	public DateTime updateTimeStamp;
	public MQSCHGType updateType;
	public String updateUser;

	public DopInstruction(){

	}
}//end DopInstruction