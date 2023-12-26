package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Customers.CustomerAgreement;

/**
 * Demand response program.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DemandResponseProgram extends IdentifiedObject {

	/**
	 * Type of demand response program; examples are CPP (critical-peak pricing), RTP
	 * (real-time pricing), DLC (direct load control), DBP (demand bidding program),
	 * BIP (base interruptible program). Note that possible types change a lot and it
	 * would be impossible to enumerate them all.
	 */
	public String type;
	/**
	 * Interval within which the program is valid.
	 */
	public DateTimeInterval validityInterval;
	/**
	 * All usage point groups enrolled in this demand response program.
	 */
	public UsagePointGroup UsagePointGroups;
	/**
	 * All groups of end devices enrolled in this demand response program.
	 */
	public EndDeviceGroup EndDeviceGroups;
	/**
	 * All customer agreements through which the customer is enrolled in this demand
	 * response program.
	 */
	public CustomerAgreement CustomerAgreements;

	public DemandResponseProgram(){

	}
}//end DemandResponseProgram