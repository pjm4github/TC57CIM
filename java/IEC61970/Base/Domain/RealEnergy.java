package IEC61970.Base.Domain;


/**
 * Real electrical energy.
 * @created 30-Dec-2023 4:19:38 PM
 */
public class RealEnergy {

	public UnitMultiplier multiplier;
	public UncefactUnitCode uncefactUnitCode;
	public static final UnitSymbol unit = Wh;
	public Float value;

	public RealEnergy(){

	}
}//end RealEnergy