package IEC61968.AssetMeas;

import IEC61970.Base.Meas.StringMeasurement;
import IEC61968.Assets.TestStandard;

/**
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AssetStringMeasurement extends StringMeasurement {

	/**
	 * Kind of string useful in asset domain.
	 */
	public AssetStringKind kind;
	public TestStandard TestStandard;

	public AssetStringMeasurement(){

	}
}//end AssetStringMeasurement