package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.StringQuantity;

/**
 * Name-value pair, specific to end device events.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:21 PM
 */
public class EndDeviceEventDetail {

	/**
	 * Name.
	 */
	public String name;
	/**
	 * Value, including unit information.
	 */
	public StringQuantity value;

	public EndDeviceEventDetail(){

	}
}//end EndDeviceEventDetail