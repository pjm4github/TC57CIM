package IEC61970.Base.Domain;


/**
 * Product of RMS value of the voltage and the RMS value of the quadrature
 * component of the current.
 * @created 30-Dec-2023 4:19:38 PM
 */
public class ReactivePower {

	public UnitMultiplier multiplier;
	public static final UnitSymbol unit = VAr;
	public Float value;

	public ReactivePower(){

	}
}//end ReactivePower