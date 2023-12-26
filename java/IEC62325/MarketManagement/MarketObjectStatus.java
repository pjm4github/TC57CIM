package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * The condition or position of an object with regard to its standing.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MarketObjectStatus {

	/**
	 * The coded condition or position of an object with regard to its standing.
	 */
	public String status;
	public TimeSeries TimeSeries;
	public RegisteredResource RegisteredResource;

	public MarketObjectStatus(){

	}
}//end MarketObjectStatus