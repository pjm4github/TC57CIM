package IEC61968.Metering;


/**
 * Transmission mode for end device display controls, applicable to premises area
 * network (PAN) devices.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum TransmissionModeKind {
	/**
	 * Message transmission mode whereby messages or commands are sent to specific
	 * devices.
	 */
	normal,
	/**
	 * Message transmission mode whereby messages or commands are broadcast to
	 * unspecified devices listening for such communications.
	 */
	anonymous,
	/**
	 * Message transmission mode whereby messages or commands are sent by both
	 * 'normal' and 'anonymous' methods.
	 */
	both
}