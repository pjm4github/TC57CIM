package TC57CIM.IEC61970.Base.Domain;


/**
 * Cost per unit volume.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class CostPerVolume {

	public static final UnitMultiplier denominatorMultiplier = none;
	public static final UnitSymbol denominatorUnit = m3;
	public UnitMultiplier multiplier;
	public Currency unit;
	public Float value;

	public CostPerVolume(){

	}

	public void finalize() throws Throwable {

	}

}