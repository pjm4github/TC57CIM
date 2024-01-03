package IEC62325.InfIEC62325.InfMarketOperations;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Participation level of a given Pnode in a given AggregatePnode.
 * @created 03-Jan-2024 1:53:43 PM
 */
public class Participation extends IdentifiedObject {

	/**
	 * Used to calculate "participation" of Pnode in an AggregatePnode. For example,
	 * for regulation region this factor is 1 and total sum of all factors for a
	 * specific regulation region does not have to be 1. For pricing zone the total
	 * sum of all factors has to be 1.
	 */
	public Float factor;

	public Participation(){

	}
}//end Participation