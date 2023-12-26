package IEC61968.AssetMeas;

import IEC61970.Base.Meas.Discrete;
import IEC61968.Assets.TestStandard;

/**
 * Definition of type of discrete useful in asset domain.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AssetDiscrete extends Discrete {

	/**
	 * The lab test standard to which this asset health discrete is related.
	 */
	public TestStandard TestStandard;

	public AssetDiscrete(){

	}
}//end AssetDiscrete