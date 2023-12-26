package IEC61968.DER;

import IEC61970.Base.Domain.DateTime;
import IEC61968.Metering.EndDeviceGroup;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DERGroupForecast extends IdentifiedObject {

	public DateTime predictionCreationDate;
	public EndDeviceGroup EndDeviceGroup;

	public DERGroupForecast(){

	}
}//end DERGroupForecast