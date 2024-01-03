package IEC61970.Base.Generation.Production;

import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Domain.Currency;
import IEC61970.Base.Domain.Float;

/**
 * Cost, in units of currency, per quantity of heat generated.
 * @created 02-Jan-2024 10:52:23 PM
 */
public class CostPerHeatUnit {

	public static final UnitMultiplier denominatorMultiplier = none;
	public static final UnitSymbol denominatorUnit = J;
	public UnitMultiplier multiplier;
	public Currency unit;
	public Float value;

	public CostPerHeatUnit(){

	}
}//end CostPerHeatUnit