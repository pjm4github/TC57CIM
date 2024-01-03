package IEC61968.InfIEC61968.InfAssets;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Reconditioning information for an asset.
 * @created 03-Jan-2024 12:26:49 PM
 */
public class Reconditioning extends IdentifiedObject {

	/**
	 * Date and time this reconditioning (or a major overhaul) has been performed.
	 */
	public DateTime dateTime;
	public TransformerObservation TransformerObservations;

	public Reconditioning(){

	}
}//end Reconditioning