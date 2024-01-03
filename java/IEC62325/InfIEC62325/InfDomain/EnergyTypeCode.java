package IEC62325.InfIEC62325.InfDomain;


/**
 * Valid Enumerations:
 * 1) DASE Day Ahead Scheduled Energy;
 * 2) DSSE Day Ahead Incremental Self Schedule Energy;
 * 3) DABE Day Ahead Incremental Energy Bid Awarded Energy;
 * 4) OE Optimal Energy;
 * 5) HASE Hour ahead pre-dispatched schedule energy;
 * 6) SRE Standard Ramping Energy;
 * 7) RED Ramping Energy Deviation;
 * 8) EDE Exceptional Dispatch energy;
 * 9) RMRE RMR Energy;
 * 10) MSSLFE MSSLF Energy;
 * 11) RE Residual Energy;
 * 12) MLE Minimum Load Energy;
 * 13) SE SLIC Energy;
 * 14) RTSSE Real time self scheduled energy;
 * 15) DMLE Day ahead minimum load energy;
 * 16) PE Pumping Energy;
 * 17) TEE Total Expected Energy;
 * 18) DAPE - Day-Ahead Pumping Energy;
 * @created 03-Jan-2024 1:48:21 PM
 */
public enum EnergyTypeCode {
	DASE,
	DSSE,
	DABE,
	OE,
	HASE,
	SRE,
	RED,
	EDE,
	RMRE,
	MSSLFE,
	RE,
	MLE,
	SE,
	RTSSE,
	DMLE,
	PE,
	TEE,
	DAPE
}