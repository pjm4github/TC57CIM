package IEC61968.Assets;

import IEC61970.Base.Domain.Volume;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A substance that either (1) provides the means of transmission of a force or
 * effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping
 * substance, such as oil in a transformer or circuit breaker.
 * @created 07-Jan-2024 9:48:28 PM
 */
public class Medium extends IdentifiedObject {

	/**
	 * Kind of this medium.
	 */
	public MediumKind kind;
	/**
	 * The volume of the medium specified for this application. Note that the actual
	 * volume is a type of measurement associated witht the asset.
	 */
	public Volume volumeSpec;
	public Asset Asset;

	public Medium(){

	}
}//end Medium