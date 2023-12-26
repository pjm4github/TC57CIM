package IEC61970.Part303.GenericDataset;


/**
 * A generic container of a version of instance data. The MRID can be used in an
 * audit trail, not in reusable script intended to work with new versions of data.
 * 
 * A dataset could be serialized multiple times and in multiple technologies, yet
 * retain the same identity.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DataSet {

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
	 * The profiles that describe the contents of the data set and the rules governing
	 * the contents of the data set.
	 */
	public Profile Profile;

	public DataSet(){

	}
}//end DataSet