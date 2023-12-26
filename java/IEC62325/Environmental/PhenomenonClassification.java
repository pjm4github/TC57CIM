package IEC62325.Environmental;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * A pre-defined phenomenon classification as defined by a particular authority.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class PhenomenonClassification extends IdentifiedObject {

	/**
	 * Authority defining this environmental phenomenon.
	 */
	public EnvironmentalDataAuthority EnvironmentalDataAuthority;

	public PhenomenonClassification(){

	}
}//end PhenomenonClassification