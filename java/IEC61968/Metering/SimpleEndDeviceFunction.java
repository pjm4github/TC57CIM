package IEC61968.Metering;


/**
 * Simple end device function distinguished by 'kind'. Use this class for
 * instances that cannot be represented by another end device function
 * specialisations.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class SimpleEndDeviceFunction extends EndDeviceFunction {

	/**
	 * Kind of this function.
	 */
	public EndDeviceFunctionKind kind;

	public SimpleEndDeviceFunction(){

	}
}//end SimpleEndDeviceFunction