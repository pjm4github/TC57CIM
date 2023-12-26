package IEC62325.Environmental;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Abstract class (with concrete child classes of Observation and Forecast) that
 * groups phenomenon and/or environmental value sets.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class EnvironmentalInformation extends IdentifiedObject {

	/**
	 * The timestamp of when the forecast was created
	 */
	public DateTime created;
	/**
	 * Environmental data provider supplying this environmental information.
	 */
	public EnvironmentalDataProvider EnvironmentalDataProvider;

	public EnvironmentalInformation(){

	}
}//end EnvironmentalInformation