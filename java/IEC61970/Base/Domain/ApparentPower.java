package IEC61970.Base.Domain;


/**
 * Product of the RMS value of the voltage and the RMS value of the current.
 * @created 30-Dec-2023 4:19:37 PM
 */
public class ApparentPower {

	public UnitMultiplier multiplier;
	public UncefactUnitCode uncfactUnitCode;
	public static final UnitSymbol unit = VA;
	public Float value;

	public ApparentPower(){

	}
}//end ApparentPower