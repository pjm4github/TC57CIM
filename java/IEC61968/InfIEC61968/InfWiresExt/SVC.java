package IEC61968.InfIEC61968.InfWiresExt;

import IEC61970.Base.Domain.Reactance;
import IEC61970.Base.Wires.ShuntCompensator;

/**
 * SVC asset allows the capacitive and inductive ratings for each phase to be
 * specified individually if required.
 * @created 29-Dec-2023 5:59:41 PM
 */
public class SVC extends ShuntCompensator {

	/**
	 * Maximum capacitive reactive power.
	 */
	public Reactance capacitiveRating;
	/**
	 * Maximum inductive reactive power.
	 */
	public Reactance inductiveRating;

	public SVC(){

	}
}//end SVC