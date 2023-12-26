package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;
import IEC61968.Metering.ReadingType;

/**
 * One of a sequence of intervals defined in terms of consumption quantity of a
 * service such as electricity, water, gas, etc. It is typically used in
 * association with TariffProfile to define the steps or blocks in a step tariff
 * structure, where startValue simultaneously defines the entry value of this step
 * and the closing value of the previous step. Where consumption is >= startValue
 * it falls within this interval and where consumption is < startValue it falls
 * within the previous interval.
 * @created 25-Dec-2023 8:45:20 PM
 */
public class ConsumptionTariffInterval {

	/**
	 * A sequential reference that defines the identity of this interval and its
	 * relative position with respect to other intervals in a sequence of intervals.
	 */
	public Integer sequenceNumber;
	/**
	 * The lowest level of consumption that defines the starting point of this
	 * interval. The interval extends to the start of the next interval or until it is
	 * reset to the start of the first interval by TariffProfile.tariffCycle.
	 */
	public Float startValue;
	/**
	 * All time of use tariff intervals influenced by this consumption tariff interval.
	 */
	public TimeTariffInterval TouTariffIntervals;
	/**
	 * All charges used to define this consumption tariff interval.
	 */
	public Charge Charges;
	/**
	 * Reading type for 'startValue'.
	 */
	public ReadingType ReadingType;

	public ConsumptionTariffInterval(){

	}
}//end ConsumptionTariffInterval