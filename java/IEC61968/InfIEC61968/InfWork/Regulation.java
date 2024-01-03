package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;

/**
 * Special requirements and/or regulations may pertain to certain types of assets
 * or work. For example, fire protection and scaffolding.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class Regulation extends WorkDocument {

	/**
	 * External reference to regulation, if applicable.
	 */
	public String referenceNumber;

	public Regulation(){

	}
}//end Regulation