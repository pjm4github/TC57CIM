package IEC61970.Base.Domain;


/**
 * Product of RMS value of the voltage and the RMS value of the in-phase component
 * of the current.
 * @created 30-Dec-2023 4:19:37 PM
 */
public class ActivePower {

	public UnitMultiplier multiplier;
	public UncefactUnitCode uncefactUnitCode;
	public static final UnitSymbol unit = W;
	public Float value;

	public ActivePower(){

	}
}//end ActivePower