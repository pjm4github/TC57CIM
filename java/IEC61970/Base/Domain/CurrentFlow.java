package IEC61970.Base.Domain;


/**
 * Electrical current with sign convention: positive flow is out of the conducting
 * equipment into the connectivity node. Can be both AC and DC.
 * @created 30-Dec-2023 4:19:37 PM
 */
public class CurrentFlow {

	public UnitMultiplier multiplier;
	public UncefactUnitCode uncefactUnitCode;
	public static final UnitSymbol unit = A;
	public Float value;

	public CurrentFlow(){

	}
}//end CurrentFlow