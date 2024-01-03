package IEC62325.InfIEC62325.InfFinancial;

import IEC61968.Common.Organisation;
import IEC62325.InfIEC62325.InfEnergyScheduling.TieLine;

/**
 * The energy buyer in the energy marketplace.
 * @created 03-Jan-2024 1:52:02 PM
 */
public class CustomerConsumer extends Organisation {

	/**
	 * A  ControlAreaOperator or CustomerConsumer may ring their perimeter with
	 * metering, which can create a unique SubControlArea at the collection of
	 * metering points, called a TieLine.
	 */
	public TieLine CustChildOf;

	public CustomerConsumer(){

	}
}//end CustomerConsumer