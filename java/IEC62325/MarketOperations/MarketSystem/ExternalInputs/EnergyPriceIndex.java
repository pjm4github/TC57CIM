package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.EnergyPriceIndexType;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC62325.MarketOperations.ReferenceData.RegisteredGenerator;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An Energy Price Index for each Resource is valid for a period (e.g. daily) that
 * is identified by a Valid Period Start Time and a Valid Period End Time. An
 * Energy Price Index is in $/MWh.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class EnergyPriceIndex extends IdentifiedObject {

	/**
	 * Energy price index
	 */
	public Float energyPriceIndex;
	/**
	 * EPI type such as wholesale or retail
	 */
	public EnergyPriceIndexType energyPriceIndexType;
	/**
	 * Time updated
	 */
	public DateTime lastModified;
	/**
	 * Valid period for which the energy price index is valid.
	 */
	public DateTimeInterval validPeriod;
	public RegisteredGenerator RegisteredGenerator;

	public EnergyPriceIndex(){

	}
}//end EnergyPriceIndex