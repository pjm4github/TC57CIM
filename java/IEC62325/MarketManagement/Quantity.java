package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Decimal;

/**
 * Description of quantities needed in the data exchange.
 * The type of the quantity is described either by the role of the association or
 * the type attribute.
 * The quality attribute provides the information about the quality of the
 * quantity (measured, estimated, etc.).
 * @author ENTSO-E
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class Quantity {

	/**
	 * The quality of the information being provided. This quality may be estimated,
	 * not available, as provided, etc. 
	 */
	public String quality;
	/**
	 * The quantity value.
	 * The association role provides the information about what is expressed.
	 */
	public Decimal quantity;
	/**
	 * The description of the type of the quantity.
	 */
	public String type;
	public TimeSeries TimeSeries;
	public Point Point;
	public Domain Domain;

	public Quantity(){

	}
}//end Quantity