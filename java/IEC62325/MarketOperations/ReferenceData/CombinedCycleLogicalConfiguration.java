package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Logical Configuration of a Combined Cycle plant.
 * 
 * Operating Combined Cycle Plant (CCP) configurations are represented as Logical
 * CCP Resources. Logical representation shall be used for Market applications to
 * optimize and control Market Operations. Logical representation is also
 * necessary for controlling the number of CCP configurations and to temper
 * performance issues that may otherwise occur.
 * 
 * For example,(2CT configuration),(1CT + 1ST configuration) are examples of
 * logical configuration, without specifying the specific CT and ST participating
 * in the configuration.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class CombinedCycleLogicalConfiguration extends IdentifiedObject {

	public MktCombinedCyclePlant MktCombinedCyclePlant;
	public CombinedCycleConfiguration CombinedCycleConfiguration;

	public CombinedCycleLogicalConfiguration(){

	}
}//end CombinedCycleLogicalConfiguration