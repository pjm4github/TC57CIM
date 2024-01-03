package IEC61970.Base.Domain;


/**
 * Percentage on a defined base.   For example, specify as 100 to indicate at the
 * defined base.
 * @created 30-Dec-2023 4:19:38 PM
 */
public class PerCent {

	public static final UnitMultiplier multiplier = none;
	public static final UnitSymbol unit = none;
	/**
	 * Normally 0 - 100 on a defined base
	 */
	public Float value;

	public PerCent(){

	}
}//end PerCent