package IEC61968.InfIEC61968.InfAssets;


/**
 * Kind of FACTS device.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum FACTSDeviceKind {
	/**
	 * Static VAr compensator.
	 */
	svc,
	/**
	 * Static synchronous compensator.
	 */
	statcom,
	/**
	 * Thyristor-controlled phase-angle regulator.
	 */
	tcpar,
	/**
	 * Thyristor-controlled series capacitor.
	 */
	tcsc,
	/**
	 * Thyristor-controlled voltage limiter.
	 */
	tcvl,
	/**
	 * Thyristor-switched braking resistor.
	 */
	tsbr,
	/**
	 * Thyristor-switched series capacitor.
	 */
	tssc,
	/**
	 * Unified power flow controller.
	 */
	upfc
}