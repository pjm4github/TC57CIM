package IEC61968.Metering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Abstraction for management of group communications within a two-way AMR system
 * or the data for a group of related usage points. Commands can be issued to all
 * of the usage points that belong to a usage point group using a defined group
 * address and the underlying AMR communication infrastructure.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class UsagePointGroup extends IdentifiedObject {

	/**
	 * Type of this group.
	 */
	public String type;
	/**
	 * All usage points in this group.
	 */
	public UsagePoint UsagePoints;

	public UsagePointGroup(){

	}
}//end UsagePointGroup