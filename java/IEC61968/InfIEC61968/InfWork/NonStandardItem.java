package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Money;

/**
 * This document provides information for non-standard items like customer
 * contributions (e.g., customer digs trench), vouchers (e.g., credit), and
 * contractor bids.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class NonStandardItem extends WorkDocument {

	/**
	 * The projected cost for this item.
	 */
	public Money amount;

	public NonStandardItem(){

	}
}//end NonStandardItem