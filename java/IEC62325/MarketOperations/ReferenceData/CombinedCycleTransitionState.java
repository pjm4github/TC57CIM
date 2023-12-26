package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Boolean;

/**
 * Defines the available from and to Transition States for the Combine Cycle
 * Configurations.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class CombinedCycleTransitionState {

	/**
	 * Flag indicating whether this is an UP transition.
	 * If not, it is a DOWN transition.
	 */
	public Boolean upTransition;

	public CombinedCycleTransitionState(){

	}
}//end CombinedCycleTransitionState