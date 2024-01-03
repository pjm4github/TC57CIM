package IEC62325.InfIEC62325.InfDomain;


/**
 * Status indication for bids
 * 
 * CV - Conditionally Valid Bid
 * CM - Conditionally Modified Bid
 * V - Valid Bid
 * M - Modified Bid
 * RJ - Rejected Bid
 * I - Invalid Bid
 * CX - Cancelled Bid
 * O - Obsolete Bid
 * CL - Clean Bid
 * RP - Replicated Bid
 * @created 03-Jan-2024 1:48:21 PM
 */
public enum BidStatusType {
	/**
	 * Clean
	 */
	CL,
	/**
	 * Replicated
	 */
	RP,
	RJ,
	I,
	CV,
	CM,
	V,
	M,
	CX,
	O
}