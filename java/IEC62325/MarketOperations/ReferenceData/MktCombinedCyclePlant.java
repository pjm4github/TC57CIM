package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Generation.Production.CombinedCyclePlant;

/**
 * Subclass of Production: CombinedCyclePlant from IEC 61970 package.
 * A set of combustion turbines and steam turbines where the exhaust heat from the
 * combustion turbines is recovered to make steam for the steam turbines,
 * resulting in greater overall plant efficiency.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MktCombinedCyclePlant extends CombinedCyclePlant {

	public AggregatedPnode AggregatedPnode;

	public MktCombinedCyclePlant(){

	}
}//end MktCombinedCyclePlant