package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Customers.CustomerAgreement;

/**
 * Set of values obtained from the meter.
 * @created 25-Dec-2023 8:45:23 PM
 */
public class MeterReading extends IdentifiedObject {

	/**
	 * If true, this meter reading is the meter reading for which other coincident
	 * meter readings are requested or provided.
	 */
	public Boolean isCoincidentTrigger;
	/**
	 * Date and time interval of the data items contained within this meter reading.
	 */
	public DateTimeInterval valuesInterval;
	/**
	 * Usage point from which this meter reading (set of values) has been obtained.
	 */
	public UsagePoint UsagePoint;
	/**
	 * All end device events associated with this set of measured values.
	 */
	public EndDeviceEvent EndDeviceEvents;
	/**
	 * (could be deprecated in the future) Customer agreement for this meter reading.
	 */
	public CustomerAgreement CustomerAgreement;

	public MeterReading(){

	}
}//end MeterReading