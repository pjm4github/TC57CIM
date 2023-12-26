package IEC62325.MarketOperations.MktDomain;


/**
 * Value of this enumeration for different prices include "total" for the
 * complete/full/all-in price, "congestion" for the congestion cost associated
 * with the total price, the "loss" for the loss price associated with the total
 * price, "capacity" for prices related to installed or reserved capacity,
 * "mileage" for use-based accounting, "system" for system-wide/copper-plate
 * prices, and "delivery" for distribution-based prices.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public enum PriceTypeKind {
	capacity,
	congestion,
	delivery,
	loss,
	mileage,
	system,
	total
}