package IEC61970.InfIEC61970.SCADA_EMS.Messages.MeasValueConfigurationReply;

import IEC61970.Base.Domain.String;

/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class IdentifiedObject {

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

	public IdentifiedObject(){

	}
}//end IdentifiedObject