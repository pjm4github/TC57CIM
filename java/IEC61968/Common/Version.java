package IEC61968.Common;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Integer;

/**
 * This is the version for a group of devices or objects.  This could be used to
 * track the version for any group of objects or devices over time. For example,
 * for a DERGroup, the requesting system may want to get the details of a specific
 * version of a DERGroup.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public class Version {

	/**
	 * date of this version
	 */
	public DateTime date;
	/**
	 * major release level for this version
	 */
	public Integer major;
	/**
	 * minor release level for this version
	 */
	public Integer minor;
	/**
	 * revision level for this version
	 */
	public Integer revision;

	public Version(){

	}
}//end Version