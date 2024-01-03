package IEC62325.InfIEC62325.InfExternalInputs;

import IEC61968.Common.Status;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A logical grouping of resources that are used to model location of types of
 * requirements for ancillary services such as spinning reserve zones, regulation
 * zones, etc.
 * @created 03-Jan-2024 1:51:06 PM
 */
public class ResourceGroup extends IdentifiedObject {

	/**
	 * Status of this group.
	 */
	public Status status;
	/**
	 * Type of this group.
	 */
	public String type;
	public ResourceGroupReq ResourceGroupReqs;

	public ResourceGroup(){

	}
}//end ResourceGroup