package IEC61970.Base.Core;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;

/**
 * A multi-purpose curve or functional relationship between an independent
 * variable (X-axis) and dependent (Y-axis) variables.
 * @created 02-Jan-2024 10:18:27 PM
 */
public class Curve extends IdentifiedObject {

	/**
	 * The style or shape of the curve.
	 */
	public CurveStyle curveStyle;
	/**
	 * Multiplier for X-axis.
	 */
	public UnitMultiplier xMultiplier;
	/**
	 * The X-axis units of measure.
	 */
	public UnitSymbol xUnit;
	/**
	 * Multiplier for Y1-axis.
	 */
	public UnitMultiplier y1Multiplier;
	/**
	 * The Y1-axis units of measure.
	 */
	public UnitSymbol y1Unit;
	/**
	 * Multiplier for Y2-axis.
	 */
	public UnitMultiplier y2Multiplier;
	/**
	 * The Y2-axis units of measure.
	 */
	public UnitSymbol y2Unit;
	/**
	 * Multiplier for Y3-axis.
	 */
	public UnitMultiplier y3Multiplier;
	/**
	 * The Y3-axis units of measure.
	 */
	public UnitSymbol y3Unit;
	/**
	 * The point data values that define this curve.
	 */
	public CurveData CurveDatas;

	public Curve(){

	}
}//end Curve