package IEC61970.Base.Core;

import IEC61970.Base.Domain.String;
import IEC61970.Base.DiagramLayout.DiagramObject;

/**
 * This is a root class to provide common identification for all classes needing
 * identification and naming attributes.
 * @created 02-Jan-2024 10:34:48 PM
 */
public class IdentifiedObject {

	/**
	 * The aliasName is free text human readable name of the object alternative to
	 * IdentifiedObject.name. It may be non unique and may not correlate to a naming
	 * hierarchy.
	 * The attribute aliasName is retained because of backwards compatibility between
	 * CIM relases. It is however recommended to replace aliasName with the Name class
	 * as aliasName is planned for retirement at a future time.
	 */
	public String aliasName;
	/**
	 * The description is a free human readable text describing or naming the object.
	 * It may be non unique and may not correlate to a naming hierarchy.
	 */
	public String description;
	/**
	 * Master resource identifier issued by a model authority. The mRID is unique
	 * within an exchange context. Global uniqueness is easily achieved by using a
	 * UUID,  as specified in RFC 4122, for the mRID. The use of UUID is strongly
	 * recommended.
	 * For CIMXML data files in RDF syntax conforming to IEC 61970-552 Edition 1, the
	 * mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object
	 * elements.
	 */
	public String mRID;
	/**
	 * The name is any free human readable and possibly non unique text naming the
	 * object.
	 */
	public String name;
	/**
	 * The diagram objects that are associated with the domain object.
	 */
	public DiagramObject DiagramObjects;

	public IdentifiedObject(){

	}
}//end IdentifiedObject