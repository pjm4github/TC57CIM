package IEC61968.Common;


/**
 * Person who created document or activity record.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class Author extends DocumentPersonRole {

	/**
	 * All documents of this this author.
	 */
	public Document Documents;
	/**
	 * All activity records with this author.
	 */
	public ActivityRecord ActivityRecords;

	public Author(){

	}
}//end Author