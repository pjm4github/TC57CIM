package IEC61970.Base.Domain;


/**
 * Cost, in units of currency, per quantity of electrical energy generated.
 * @created 25-Dec-2023 8:31:55 PM
 */
public class CostPerEnergyUnit {

	public static final UnitMultiplier denominatorMultiplier = none;
	public static final UnitSymbol denominatorUnit = Wh;
	public UnitMultiplier multiplier;
	public Currency unit;
	public Float value;

	public CostPerEnergyUnit(){

	}
}//end CostPerEnergyUnit