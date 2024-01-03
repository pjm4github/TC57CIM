package IEC61970.Base.Contingency;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An event threatening system reliability, consisting of one or more contingency
 * elements.
 * @created 29-Dec-2023 1:45:04 PM
 */
public class Contingency extends IdentifiedObject {

	/**
	 * Set true if must study this contingency.
	 */
	public Boolean mustStudy;
	/**
	 * A contingency can have any number of contingency elements.
	 */
	public ContingencyElement ContingencyElement;

	public Contingency(){

	}
}//end Contingency