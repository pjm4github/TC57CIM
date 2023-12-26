package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Temperature;

/**
 * A point on a table of limit verses temperature.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TemperatureDependentLimitPoint {

	/**
	 * The scaling of the operational limit in percent.
	 */
	public PerCent limitPercent;
	/**
	 * The temperature of the table point.
	 */
	public Temperature temperature;

	public TemperatureDependentLimitPoint(){

	}
}//end TemperatureDependentLimitPoint