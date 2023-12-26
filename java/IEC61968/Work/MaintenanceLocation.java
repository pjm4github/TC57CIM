package IEC61968.Work;

import IEC61970.Base.Domain.String;

/**
 * Location where to perform maintenance work.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class MaintenanceLocation extends WorkLocation {

	/**
	 * (if applicable) Name, identifier, or description of the block in which work is
	 * to occur.
	 */
	public String block;
	/**
	 * (if applicable) Name, identifier, or description of the lot in which work is to
	 * occur.
	 */
	public String lot;
	/**
	 * The names of streets at the nearest intersection to work area.
	 */
	public String nearestIntersection;
	/**
	 * (if applicable) Name, identifier, or description of the subdivision in which
	 * work is to occur.
	 */
	public String subdivision;

	public MaintenanceLocation(){

	}
}//end MaintenanceLocation