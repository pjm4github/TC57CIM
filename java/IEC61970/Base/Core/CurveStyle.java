package IEC61970.Base.Core;


/**
 * Style or shape of curve.
 * @created 02-Jan-2024 10:39:24 PM
 */
public enum CurveStyle {
	/**
	 * The Y-axis values are assumed constant until the next curve point and prior to
	 * the first curve point.
	 */
	constantYValue,
	/**
	 * The Y-axis values are assumed to be a straight line between values.  Also known
	 * as linear interpolation.
	 */
	straightLineYValues
}