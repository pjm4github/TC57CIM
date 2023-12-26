package IEC61968.Assets;

import IEC61970.Base.Domain.Date;

/**
 * Dates for asset lifecycle state changes. May have multiple lifecycle dates for
 * this device and a compound type allows a query to return multiple dates.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class LifecycleDate {

	/**
	 * Date current installation was completed, which may not be the same as the in-
	 * service date. Asset may have been installed at other locations previously.
	 * Ignored if asset is (1) not currently installed (e.g., stored in a depot) or
	 * (2) not intended to be installed (e.g., vehicle, tool).
	 */
	public Date installationDate;
	/**
	 * Date the asset was manufactured.
	 */
	public Date manufacturedDate;
	/**
	 * Date the asset was purchased. Note that even though an asset may have been
	 * purchased, it may not have been received into inventory at the time of purchase.
	 */
	public Date purchaseDate;
	/**
	 * Date the asset was received and first placed into inventory.
	 */
	public Date receivedDate;
	/**
	 * Date when the asset was last removed from service. Ignored if (1) not intended
	 * to be in service, or (2) currently in service.
	 */
	public Date removalDate;
	/**
	 * Date the asset is permanently retired from service and may be scheduled for
	 * disposal. Ignored if asset is (1) currently in service, or (2) permanently
	 * removed from service.
	 */
	public Date retiredDate;

	public LifecycleDate(){

	}
}//end LifecycleDate