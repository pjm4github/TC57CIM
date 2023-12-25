package TC57CIM.IEC61970.Base.DC;


/**
 * Active power control modes for HVDC line operating as Current Source Converter.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public enum CsPpccControlKind {
	/**
	 * Active power control at AC side.
	 */
	activePower,
	/**
	 * DC voltage control.
	 */
	dcVoltage,
	/**
	 * DC current control
	 */
	dcCurrent
}