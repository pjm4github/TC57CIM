package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;

/**
 * Priority definition.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class Priority {

	/**
	 * Justification for 'rank'.
	 */
	public String justification;
	/**
	 * Priority level; usually, lower number means high priority, but the details are
	 * provided in 'type'.
	 */
	public Integer rank;
	/**
	 * Type describing 'rank'; e.g., high, emergency, etc.
	 */
	public String type;

	public Priority(){

	}
}//end Priority