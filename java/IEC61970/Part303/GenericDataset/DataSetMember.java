package IEC61970.Part303.GenericDataset;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A generic description of a version of instance data.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DataSetMember {

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
	 * The CIM object holding the properties of this dataset context.   Sometimes
	 * properties are not required and only the reference to the registered object is
	 * required.
	 */
	public IdentifiedObject PropertiesObject;
	/**
	 * The registered CIM object.
	 */
	public IdentifiedObject TargetObject;

	public DataSetMember(){

	}
}//end DataSetMember