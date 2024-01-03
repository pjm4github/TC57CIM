package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.String;
import IEC61968.InfIEC61968.InfCommon.Ratio;
import IEC61970.Base.Domain.Voltage;
import IEC61968.Assets.AssetInfo;

/**
 * Properties of potential transformer asset.
 * @created 29-Dec-2023 6:22:55 PM
 */
public class PotentialTransformerInfo extends AssetInfo {

	public String accuracyClass;
	public Ratio nominalRatio;
	/**
	 * Ratio for the primary winding tap changer.
	 */
	public Ratio primaryRatio;
	public String ptClass;
	/**
	 * Rated voltage on the primary side.
	 */
	public Voltage ratedVoltage;
	/**
	 * Ratio for the secondary winding tap changer.
	 */
	public Ratio secondaryRatio;
	/**
	 * Ratio for the tertiary winding tap changer.
	 */
	public Ratio tertiaryRatio;

	public PotentialTransformerInfo(){

	}
}//end PotentialTransformerInfo