package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.Float;

/**
 * Quantity of emission per fuel heat content.
 * @created 02-Jan-2024 10:52:37 PM
 */
public class Emission {

	public static final UnitMultiplier multiplier = none;
	public static final UnitSymbol unit = kgPerJ;
	public Float value;

	public Emission(){

	}
}//end Emission