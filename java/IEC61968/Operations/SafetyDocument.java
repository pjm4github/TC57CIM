package IEC61968.Operations;

import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Document;

/**
 * Document restricting or authorising works on electrical equipment (for example
 * a permit to work, sanction for test, limitation of access, or certificate of
 * isolation), defined based upon organisational practices.
 * @created 03-Jan-2024 1:17:50 PM
 */
public class SafetyDocument extends Document {

	/**
	 * Date and time this safety document has been issued.
	 */
	public DateTime issuedDateTime;
	/**
	 * Date and time this safety document has been released.
	 */
	public DateTime releasedDateTime;

	public SafetyDocument(){

	}
}//end SafetyDocument