package IEC62325.InfIEC62325.InfDomain;


/**
 * self schedule types
 * 
 * PT
 * ETC
 * TOR
 * RMR
 * RMT
 * RGMR
 * ORFC
 * SP
 * @created 03-Jan-2024 1:48:21 PM
 */
public enum SelfScheduleType {
	PT,
	ETC,
	TOR,
	RMR,
	RMT,
	RGMR,
	ORFC,
	/**
	 * Self-Provision
	 */
	SP,
	IFM,
	RUC,
	/**
	 * RA Obligations
	 */
	RA,
	PUMP_ETC,
	PUMP_TOR,
	/**
	 * Base Schedule
	 */
	BAS,
	/**
	 * Lay-off schedule
	 */
	LOF,
	WHL
}