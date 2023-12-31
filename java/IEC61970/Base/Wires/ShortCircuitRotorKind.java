package IEC61970.Base.Wires;


/**
 * Type of rotor, used by short circuit applications.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public enum ShortCircuitRotorKind {
	/**
	 * Salient pole 1 in the IEC 60909
	 */
	salientPole1,
	/**
	 * Salient pole 2 in IEC 60909
	 */
	salientPole2,
	/**
	 * Turbo Series 1 in the IEC 60909
	 */
	turboSeries1,
	/**
	 * Turbo series 2 in IEC 60909
	 */
	turboSeries2
}