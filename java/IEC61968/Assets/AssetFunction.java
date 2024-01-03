package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Function performed by an asset.
 * @created 03-Jan-2024 12:00:48 PM
 */
public class AssetFunction extends IdentifiedObject {

	/**
	 * Configuration specified for this function.
	 */
	public String configID;
	/**
	 * Firmware version.
	 */
	public String firmwareID;
	/**
	 * Hardware version.
	 */
	public String hardwareID;
	/**
	 * Password needed to access this function.
	 */
	public String password;
	/**
	 * Name of program.
	 */
	public String programID;

	public AssetFunction(){

	}
}//end AssetFunction