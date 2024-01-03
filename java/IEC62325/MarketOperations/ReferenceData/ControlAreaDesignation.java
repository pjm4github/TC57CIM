package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Indicates Control Area associated with self-schedule.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class ControlAreaDesignation {

	/**
	 * Attained.
	 */
	public YesNo attained;
	/**
	 * Native.
	 */
	public YesNo native;
	public SubControlArea SubControlArea;
	public RegisteredResource RegisteredResource;

	public ControlAreaDesignation(){

	}
}//end ControlAreaDesignation