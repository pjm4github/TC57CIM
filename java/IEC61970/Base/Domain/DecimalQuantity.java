package IEC61970.Base.Domain;


/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DecimalQuantity {

	/**
	 * Quantity with decimal value and associated unit or currency information.
	 */
	public Currency currency;
	public UnitMultiplier multiplier;
	public UnitSymbol unit;
	public Decimal value;

	public DecimalQuantity(){

	}
}//end DecimalQuantity