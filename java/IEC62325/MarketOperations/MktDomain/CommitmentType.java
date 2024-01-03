package IEC62325.MarketOperations.MktDomain;


/**
 * For example:
 * SELF - Self commitment
 * ISO - New commitment for this market period
 * UC - Existing commitment that was a hold over from a previous market
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum CommitmentType {
	SELF,
	ISO,
	UC
}