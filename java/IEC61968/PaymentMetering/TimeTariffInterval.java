package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Time;

/**
 * One of a sequence of time intervals defined in terms of real time. It is
 * typically used in association with TariffProfile to define the intervals in a
 * time of use tariff structure, where startDateTime simultaneously determines the
 * starting point of this interval and the ending point of the previous interval.
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TimeTariffInterval {

	/**
	 * A sequential reference that defines the identity of this interval and its
	 * relative position with respect to other intervals in a sequence of intervals.
	 */
	public Integer sequenceNumber;
	/**
	 * A real time marker that defines the starting time (typically it is the time of
	 * day) for this interval. The interval extends to the start of the next interval
	 * or until it is reset to the start of the first interval by TariffProfile.
	 * tariffCycle.
	 */
	public Time startTime;
	/**
	 * All charges used to define this time tariff interval.
	 */
	public Charge Charges;

	public TimeTariffInterval(){

	}
}//end TimeTariffInterval