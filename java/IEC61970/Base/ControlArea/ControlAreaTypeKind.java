package IEC61970.Base.ControlArea;


/**
 * The type of control area.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
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