package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.Float;

/**
 * Heat generated, in energy pertime unit of elapsed time.
 * @created 02-Jan-2024 10:54:40 PM
 */
public class HeatRate {

	public UnitMultiplier multiplier;
	public static final UnitSymbol unit = J;
	public Float value;

	public HeatRate(){

	}
}//end HeatRate