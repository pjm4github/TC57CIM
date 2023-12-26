package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Meas.AnalogLimitSet;

/**
 * Subclass of IEC 61970:Meas:AnalogLimitSet.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MktAnalogLimitSet extends AnalogLimitSet {

	/**
	 * Rating set numbers
	 */
	public Integer ratingSet;

	public MktAnalogLimitSet(){

	}
}//end MktAnalogLimitSet