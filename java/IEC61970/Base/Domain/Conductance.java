package IEC61970.Base.Domain;


/**
 * Factor by which voltage must be multiplied to give corresponding power lost
 * from a circuit. Real part of admittance.
 * @created 30-Dec-2023 4:19:37 PM
 */
public class Conductance {

	public UnitMultiplier multiplier;
	public static final UnitSymbol unit = S;
	public Float value;

	public Conductance(){

	}
}//end Conductance