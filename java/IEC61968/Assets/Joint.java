package IEC61968.Assets;

import IEC61968.InfIEC61968.InfAssets.JointConfigurationKind;
import IEC61968.InfIEC61968.InfAssets.JointFillKind;
import IEC61970.Base.Domain.String;

/**
 * Joint connects two or more cables. It includes the portion of cable under wipes,
 * welds, or other seals.
 * @created 07-Jan-2024 9:47:59 PM
 */
public class Joint extends Asset {

	/**
	 * Configuration of joint.
	 */
	public JointConfigurationKind configurationKind;
	/**
	 * Material used to fill the joint.
	 */
	public JointFillKind fillKind;
	/**
	 * The type of insulation around the joint, classified according to the utility's
	 * asset management standards and practices.
	 */
	public String insulation;

	public Joint(){

	}
}//end Joint