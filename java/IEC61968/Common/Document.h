///////////////////////////////////////////////////////////
//  Document.h
//  Implementation of the Class Document
//  Created on:      25-Dec-2023 8:45:21 PM
///////////////////////////////////////////////////////////

#if !defined(EA_878A8924_C1F4_4965_AFF9_15BF3B9D033B__INCLUDED_)
#define EA_878A8924_C1F4_4965_AFF9_15BF3B9D033B__INCLUDED_

#include "String.h"
#include "DateTime.py"
#include "Status.py"
#include "ElectronicAddress.h"
#include "IdentifiedObject.py"
#include "ConfigurationEvent.py"

/**
 * Parent class for different groupings of information collected and managed as a
 * part of a business process. It will frequently contain references to other
 * objects, such as assets, people and power system resources.
 */
class Document : public IdentifiedObject
{

public:
	Document();
	/**
	 * Name of the author of this document.
	 */
	String authorName;
	/**
	 * Free text comment.
	 */
	String comment;
	/**
	 * Date and time that this document was created.
	 */
	DateTime createdDateTime;
	/**
	 * Status of this document. For status of subject matter this document represents
	 * (e.g., Agreement, Work), use 'status' attribute.
	 * Example values for 'docStatus.status' are draft, approved, cancelled, etc.
	 */
	Status docStatus;
	/**
	 * Electronic address.
	 */
	ElectronicAddress electronicAddress;
	/**
	 * Date and time this document was last modified. Documents may potentially be
	 * modified many times during their lifetime.
	 */
	DateTime lastModifiedDateTime;
	/**
	 * Revision number for this document.
	 */
	String revisionNumber;
	/**
	 * Status of subject matter (e.g., Agreement, Work) this document represents. For
	 * status of the document itself, use 'docStatus' attribute.
	 */
	Status status;
	/**
	 * Document subject.
	 */
	String subject;
	/**
	 * Document title.
	 */
	String title;
	/**
	 * Utility-specific classification of this document, according to its corporate
	 * standards, practices, and existing IT systems (e.g., for management of assets,
	 * maintenance, work, outage, customers, etc.).
	 */
	String type;
	/**
	 * All configuration events created for this document.
	 */
	ConfigurationEvent *ConfigurationEvents;

};
#endif // !defined(EA_878A8924_C1F4_4965_AFF9_15BF3B9D033B__INCLUDED_)
