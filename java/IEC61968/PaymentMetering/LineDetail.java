package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;

/**
 * Details on an amount line, with rounding, date and note.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class LineDetail {

	/**
	 * Amount for this line item.
	 */
	public Money amount;
	/**
	 * Date and time when this line was created in the application process.
	 */
	public DateTime dateTime;
	/**
	 * Free format note relevant to this line.
	 */
	public String note;
	/**
	 * Totalised monetary value of all errors due to process rounding or truncating
	 * that is not reflected in 'amount'.
	 */
	public Money rounding;

	public LineDetail(){

	}
}//end LineDetail