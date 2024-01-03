package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Integer;

/**
 * List of resources that can be substituted for within the bounds of a Contract
 * definition. This class has a precedence and a resource.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class SubstitutionResourceList {

	/**
	 * An indicator of the order a resource should be substituted. The lower the
	 * number the higher the precedence.
	 */
	public Integer precedence;

	public SubstitutionResourceList(){

	}
}//end SubstitutionResourceList