package IEC61970.Base.DC;


/**
 * The operating mode of an HVDC bipole.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public enum DCConverterOperatingModeKind {
	/**
	 * Bipolar operation.
	 */
	bipolar,
	/**
	 * Monopolar operation with metallic return
	 */
	monopolarMetallicReturn,
	/**
	 * Monopolar operation with ground return
	 */
	monopolarGroundReturn
}