package IEC61968.Assets;

import IEC61970.Base.Domain.Length;
import IEC61968.InfIEC61968.InfAssets.StreetlightLampKind;
import IEC61970.Base.Domain.ActivePower;

/**
 * Streetlight asset.
 * @created 07-Jan-2024 9:48:50 PM
 */
public class Streetlight extends Asset {

	/**
	 * Length of arm. Note that a new light may be placed on an existing arm.
	 */
	public Length armLength;
	/**
	 * Lamp kind.
	 */
	public StreetlightLampKind lampKind;
	/**
	 * Power rating of light.
	 */
	public ActivePower lightRating;

	public Streetlight(){

	}
}//end Streetlight