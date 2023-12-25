package TC57CIM.IEC61970.Base.Domain;


/**
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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

	public void finalize() throws Throwable {

	}

}