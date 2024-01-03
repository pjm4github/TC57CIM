package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Integer;
import IEC61968.Common.Document;
import IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute;

/**
 * Models various charges to support billing and settlement.
 * @created 28-Dec-2023 8:18:27 PM
 */
public class BillDeterminant extends Document {

	/**
	 * Level in charge calculation order.
	 */
	public String calculationLevel;
	/**
	 * The version of configuration of calculation logic in the settlement.
	 */
	public String configVersion;
	public String deleteStatus;
	public DateTime effectiveDate;
	public String exception;
	public String factor;
	public String frequency;
	/**
	 * Number of intervals of bill determiant in trade day, e.g. 300 for five minute
	 * intervals.
	 */
	public Integer numberInterval;
	public String offset;
	/**
	 * The level of precision in the current value. 
	 */
	public String precisionLevel;
	public String primaryYN;
	public String referenceFlag;
	public String reportable;
	public String roundOff;
	public String source;
	public DateTime terminationDate;
	/**
	 * The UOM for the current value of the Bill Determinant. 
	 */
	public String unitOfMeasure;
	public ChargeProfileData ChargeProfileData;
	public MktUserAttribute MktUserAttribute;

	public BillDeterminant(){

	}
}//end BillDeterminant