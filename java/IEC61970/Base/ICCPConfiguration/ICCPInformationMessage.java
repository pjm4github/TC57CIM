package IEC61970.Base.ICCPConfiguration;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class represents the TASE.2 Information Message Object.  The
 * IdentifiedObject.name attribute must be non-null.  The value of the attribute
 * shall be used as the TASE.2 Information Reference, as specified by 60870-6-503.
 * @author herb
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class ICCPInformationMessage extends IdentifiedObject {

	/**
	 * The Local Reference attribute specifies a value agreed upon between sender and
	 * receiver of the Information Message. It further identifies the Information
	 * Message.
	 */
	public String localReference;
	public ICCPScope scope;
	public TASE2BilateralTable TASE2BilateralTable;

	public ICCPInformationMessage(){

	}
}//end ICCPInformationMessage