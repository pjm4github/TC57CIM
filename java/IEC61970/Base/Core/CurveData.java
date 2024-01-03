package IEC61970.Base.Core;

import IEC61970.Base.Domain.Float;

/**
 * Multi-purpose data points for defining a curve.  The use of this generic class
 * is discouraged if a more specific class  can be used to specify the x and y
 * axis values along with their specific data types.
 * @updated 02-Jan-2024 10:22:25 PM
 */
public class CurveData {

	/**
	 * The data value of the X-axis variable,  depending on the X-axis units.
	 */
	public Float xvalue;
	/**
	 * The data value of the  first Y-axis variable, depending on the Y-axis units.
	 */
	public Float y1value;
	/**
	 * The data value of the second Y-axis variable (if present), depending on the Y-
	 * axis units.
	 */
	public Float y2value;
	/**
	 * The data value of the third Y-axis variable (if present), depending on the Y-
	 * axis units.
	 */
	public Float y3value;

	public CurveData(){

	}
}//end CurveData