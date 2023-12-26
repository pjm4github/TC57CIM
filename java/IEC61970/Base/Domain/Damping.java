package IEC61970.Base.Domain;


/**
 * Per-unit active power variation with frequency referenced on the system
 * apparent power base. Typical values are in range 1.0 - 2.0.
 * @created 25-Dec-2023 8:31:55 PM
 */
public class Damping {

	public static final UnitMultiplier multiplier;
	public static final UnitSymbol unit = onePerHz;
	public Float value;

	public Damping(){

	}
}//end Damping