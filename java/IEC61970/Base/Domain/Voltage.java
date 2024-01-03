package IEC61970.Base.Domain;


/**
 * Electrical voltage, can be both AC and DC.
 * @created 30-Dec-2023 4:19:38 PM
 */
public class Voltage {

	public UnitMultiplier multiplier;
	public UncefactUnitCode uncefactUnitCode;
	public static final UnitSymbol unit = V;
	public Float value;

	public Voltage(){

	}
}//end Voltage