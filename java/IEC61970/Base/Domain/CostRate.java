package IEC61970.Base.Domain;


/**
 * Cost, in units of currency, per elapsed time.
 * @created 25-Dec-2023 8:31:55 PM
 */
public class CostRate {

	public static final UnitMultiplier denominatorMultiplier = none;
	public static final UnitSymbol denominatorUnit = s;
	public UnitMultiplier multiplier;
	public Currency unit;
	public Float value;

	public CostRate(){

	}
}//end CostRate