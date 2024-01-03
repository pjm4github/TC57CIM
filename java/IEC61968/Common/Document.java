package IEC61968.Common;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Parent class for different groupings of information collected and managed as a
 * part of a business process. It will frequently contain references to other
 * objects, such as assets, people and power system resources.
 * @created 03-Jan-2024 12:10:48 PM
 */
public class Document extends IdentifiedObject {

	/**
	 * Name of the author of this document.
	 */
	public String authorName;
	/**
	 * Free text comment.
	 */
	public String comment;
	/**
	 * Date and time that this document was created.
	 */
	public DateTime createdDateTime;
	/**
	 * Status of this document. For status of subject matter this document represents
	 * (e.g., Agreement, Work), use 'status' attribute.
	 * Example values for 'docStatus.status' are draft, approved, cancelled, etc.
	 */
	public Status docStatus;
	/**
	 * Electronic address.
	 */
	public ElectronicAddress electronicAddress;
	/**
	 * Date and time this document was last modified. Documents may potentially be
	 * modified many times during their lifetime.
	 */
	public DateTime lastModifiedDateTime;
	/**
	 * Revision number for this document.
	 */
	public String revisionNumber;
	/**
	 * Status of subject matter (e.g., Agreement, Work) this document represents. For
	 * status of the document itself, use 'docStatus' attribute.
	 */
	public Status status;
	/**
	 * Document subject.
	 */
	public String subject;
	/**
	 * Document title.
	 */
	public String title;
	/**
	 * Utility-specific classification of this document, according to its corporate
	 * standards, practices, and existing IT systems (e.g., for management of assets,
	 * maintenance, work, outage, customers, etc.).
	 */
	public String type;
	/**
	 * All configuration events created for this document.
	 */
	public ConfigurationEvent ConfigurationEvents;

	public Document(){

	}
}//end Document