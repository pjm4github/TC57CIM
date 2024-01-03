package IEC62325.MarketOperations.MktDomain;


/**
 * For example:
 * 'S' - Mitigated by SMPM because of "misconduct"
 * 'L; - Mitigated by LMPM because of "misconduct"
 * 'R' - Modified by LMPM because of RMR rules
 * 'M' - Mitigated because of "misconduct" both by SMPM and LMPM
 * 'B' - Mitigated because of "misconduct" both by SMPM and modified by LMLM
 * because of RMR rules
 * 'O' - original
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum BidMitigationStatus {
	S,
	L,
	R,
	M,
	B,
	O
}