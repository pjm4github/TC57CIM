package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61968.Work.Work;

/**
 * Business justification for capital expenditures, usually addressing operations
 * and maintenance costs as well.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class BusinessCase extends WorkDocument {

	/**
	 * A codified representation of the business case (i.e., codes for highway
	 * relocation, replace substation transformers, etc.).
	 */
	public String corporateCode;
	public Project Projects;
	public Work Works;

	public BusinessCase(){

	}
}//end BusinessCase