package IEC61968.Customers;

import IEC61970.Base.Domain.Date;
import IEC61968.PaymentMetering.TariffProfile;
import IEC61968.Common.Document;

/**
 * Document, approved by the responsible regulatory agency, listing the terms and
 * conditions, including a schedule of prices, under which utility services will
 * be provided. It has a unique number within the state or province. For rate
 * schedules it is frequently allocated by the affiliated Public utilities
 * commission (PUC).
 * @created 03-Jan-2024 12:18:10 PM
 */
public class Tariff extends Document {

	/**
	 * (if tariff became inactive) Date tariff was terminated.
	 */
	public Date endDate;
	/**
	 * Date tariff was activated.
	 */
	public Date startDate;
	/**
	 * All tariff profiles using this tariff.
	 */
	public TariffProfile TariffProfiles;

	public Tariff(){

	}
}//end Tariff