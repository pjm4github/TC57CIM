package IEC61968.Common;


/**
 * Person who issued the document and is responsible for its content.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class Issuer extends DocumentPersonRole {

	/**
	 * All documents for this issuer.
	 */
	public Document Documents;

	public Issuer(){

	}
}//end Issuer