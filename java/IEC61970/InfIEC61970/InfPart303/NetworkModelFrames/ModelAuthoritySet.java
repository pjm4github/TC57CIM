package IEC61970.InfIEC61970.InfPart303.NetworkModelFrames;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A Modeling Authority Set is a group of objects in a network model where the
 * data is supplied and maintained by the same Modeling Authority.
 * This class is typically not included in instance data exchange as this
 * information is tracked by other mechanisms in the exchange.
 * @created 02-Jan-2024 9:22:40 PM
 */
public class ModelAuthoritySet extends IdentifiedObject {

	/**
	 * A Modeling Authority set supplies and maintains the data for the objects in a
	 * Modeling Authority Set.
	 */
	public ModelAuthority ModelingAuthority;

	public ModelAuthoritySet(){

	}
}//end ModelAuthoritySet