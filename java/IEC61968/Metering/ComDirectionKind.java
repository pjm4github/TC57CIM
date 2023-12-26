package IEC61968.Metering;


/**
 * Kind of communication direction.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum ComDirectionKind {
	/**
	 * Communication is from device.
	 */
	fromDevice,
	/**
	 * Communication is to device.
	 */
	toDevice,
	/**
	 * Communication with the device is bi-directional.
	 */
	biDirectional
}