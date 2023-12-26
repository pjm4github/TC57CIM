package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Document;

/**
 * A schedule of charges; structure associated with Tariff that allows the
 * definition of complex tarif structures such as step and time of use when used
 * in conjunction with TimeTariffInterval and Charge. Inherited 'status.value' is
 * defined in the context of the utility's business rules, for example: active,
 * inactive, etc.
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TariffProfile extends Document {

	/**
	 * The frequency at which the tariff charge schedule is repeated. Examples are:
	 * once off on a specified date and time; hourly; daily; weekly; monthly; 3-
	 * monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business
	 * rules are reset to start from the beginning again.
	 */
	public String tariffCycle;
	/**
	 * All consumption tariff intervals used to define this tariff profile.
	 */
	public ConsumptionTariffInterval ConsumptionTariffIntervals;
	/**
	 * All time tariff intervals used to define this tariff profile.
	 */
	public TimeTariffInterval TimeTariffIntervals;

	public TariffProfile(){

	}
}//end TariffProfile