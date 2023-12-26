package IEC62325.MarketManagement;

import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.String;

/**
 * A set of similar physical or conceptual objects defined for the same period or
 * point of time.
 * @author ENTSO-E
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class Series extends TimeSeries {

	/**
	 * The date of the last update related to this market object.
	 */
	public Date lastUpdateDate;
	/**
	 * Type of method used in the business process related to this Series, e.g.
	 * metering method.
	 */
	public String methodType;
	/**
	 * For a market object, the date of registration of a contract, e.g. the date of
	 * change of supplier for a customer.
	 */
	public Date registrationDate;
	public Series SelfSeries;

	public Series(){

	}
}//end Series