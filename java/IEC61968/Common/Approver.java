package IEC61968.Common;


/**
 * Person who accepted/signed or rejected the document.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:18 PM
 */
public class Approver extends DocumentPersonRole {

	/**
	 * All documents for this approver.
	 */
	public Document Documents;

	public Approver(){

	}
}//end Approver