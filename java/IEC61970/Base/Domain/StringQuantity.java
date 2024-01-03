package IEC61970.Base.Domain;


/**
 * Quantity with string value (when it is not important whether it is an integral
 * or a floating point number) and associated unit information.
 * @created 30-Dec-2023 4:19:38 PM
 */
public class StringQuantity {

	public UnitMultiplier multiplier;
	public UnitSymbol unit;
	public String value;

	public StringQuantity(){

	}
}//end StringQuantity