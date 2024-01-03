package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61968.Assets.AssetFunction;

/**
 * Function performed by an end device such as a meter, communication equipment,
 * controllers, etc.
 * @created 03-Jan-2024 1:07:44 PM
 */
public class EndDeviceFunction extends AssetFunction {

	/**
	 * True if the function is enabled.
	 */
	public Boolean enabled;

	public EndDeviceFunction(){

	}
}//end EndDeviceFunction