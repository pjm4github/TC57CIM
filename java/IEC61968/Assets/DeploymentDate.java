package IEC61968.Assets;

import IEC61970.Base.Domain.DateTime;

/**
 * Dates for deployment events of an asset.  May have multiple deployment type
 * dates for this device and a compound type allows a query to return multiple
 * dates.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DeploymentDate {

	/**
	 * Date and time asset most recently put in service.
	 */
	public DateTime inServiceDate;
	/**
	 * Date and time asset most recently installed.
	 */
	public DateTime installedDate;
	/**
	 * Date and time of asset deployment transition to not yet installed.
	 */
	public DateTime notYetInstalledDate;
	/**
	 * Date and time asset most recently taken out of service.
	 */
	public DateTime outOfServiceDate;
	/**
	 * Date and time asset most recently removed.
	 */
	public DateTime removedDate;

	public DeploymentDate(){

	}
}//end DeploymentDate