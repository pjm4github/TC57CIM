package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.CloudKind;

/**
 * A classified cloud phenomenon with a type.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class CloudCondition extends AtmosphericPhenomenon {

	/**
	 * The type of the cloud as defined by the CloudKind enumeration.
	 */
	public CloudKind kind;

	public CloudCondition(){

	}
}//end CloudCondition