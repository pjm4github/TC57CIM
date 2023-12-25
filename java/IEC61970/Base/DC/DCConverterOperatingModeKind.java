package TC57CIM.IEC61970.Base.DC;


/**
 * The operating mode of an HVDC bipole.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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