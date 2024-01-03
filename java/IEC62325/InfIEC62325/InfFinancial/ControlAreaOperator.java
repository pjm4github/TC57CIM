package IEC62325.InfIEC62325.InfFinancial;

import IEC61968.Common.Organisation;
import IEC62325.InfIEC62325.InfEnergyScheduling.TieLine;

/**
 * Operates the Control Area. Approves and implements energy transactions.
 * Verifies both Inter-Control Area and Intra-Control Area transactions for the
 * power system  before granting approval (and implementing) the transactions.
 * @created 03-Jan-2024 1:52:02 PM
 */
public class ControlAreaOperator extends Organisation {

	/**
	 * A ControlAreaOperator has a collection of tie points that ring the ControlArea,
	 * called a TieLine.
	 */
	public TieLine CAChildOf;

	public ControlAreaOperator(){

	}
}//end ControlAreaOperator