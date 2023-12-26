package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Boolean;
import IEC62325.MarketOperations.MktDomain.AnalogLimitType;
import IEC61970.Base.Meas.AnalogLimit;

/**
 * Subclass of IEC 61970:Meas:AnalogLimit.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MktAnalogLimit extends AnalogLimit {

	/**
	 * true if limit exceeded
	 */
	public Boolean exceededLimit;
	/**
	 * The type of limit the value represents
	 * Branch Limit Types:
	 * Short Term
	 * Medium Term
	 * Long Term
	 * Voltage Limits:
	 * High
	 * Low
	 */
	public AnalogLimitType limitType;

	public MktAnalogLimit(){

	}
}//end MktAnalogLimit