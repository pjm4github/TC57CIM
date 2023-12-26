package IEC62325.Environmental;

import IEC61970.Base.Domain.DateTimeInterval;

/**
 * A forecast group of value sets and/or phenomena characteristics.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class Forecast extends EnvironmentalInformation {

	/**
	 * The interval for which the forecast is valid.  For example, a forecast issued
	 * now for tomorrow might be valid for the next 2 hours.
	 */
	public DateTimeInterval validFor;

	public Forecast(){

	}
}//end Forecast