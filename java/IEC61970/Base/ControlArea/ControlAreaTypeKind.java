package TC57CIM.IEC61970.Base.ControlArea;


/**
 * The type of control area.
 * @author kdd
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public enum ControlAreaTypeKind {
	/**
	 * Used for automatic generation control.
	 */
	AGC,
	/**
	 * Used for load forecast.
	 */
	Forecast,
	/**
	 * Used for interchange specification or control.
	 */
	Interchange
}