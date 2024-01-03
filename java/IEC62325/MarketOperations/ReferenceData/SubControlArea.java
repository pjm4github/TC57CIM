package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Core.PowerSystemResource;
import IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched;
import IEC62325.MarketOperations.MarketSystem.MarketResults.GeneralClearingResults;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.EnergyTransaction;
import IEC62325.InfIEC62325.InfEnergyScheduling.InadvertentAccount;

/**
 * An area defined for the purpose of tracking interchange with surrounding areas
 * via tie points; may or may not serve as a control area.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class SubControlArea extends PowerSystemResource {

	/**
	 * Market area short name, which is the regulation zone. It references AGC
	 * regulation zone name.
	 */
	public String areaShortName;
	/**
	 * Loss estimate constant coefficient
	 */
	public Float constantCoefficient;
	/**
	 * Used in conjunction with the InternalCA flag. If the InternalCA flag is YES,
	 * this flag does not apply. If the InternaCA flag is NO, this flag provides an
	 * indication of AdjacentCA (NO) or Embedded CA (YES).
	 */
	public YesNo embeddedControlArea;
	/**
	 * A Yes/No indication that this control area is contained internal to the system.
	 */
	public YesNo internalCA;
	/**
	 * Loss estimate linear coefficient
	 */
	public Float linearCoefficient;
	/**
	 * Indication that this control area is the local control area.
	 */
	public YesNo localCA;
	/**
	 * Maximum amount of self schedule MWs allowed for an embedded control area.
	 */
	public Float maxSelfSchedMW;
	/**
	 * Minimum amount of self schedule MW allowed for an embedded control area.
	 */
	public Float minSelfSchedMW;
	/**
	 * Loss estimate quadratic coefficient
	 */
	public Float quadraticCoefficient;
	public BidSelfSched BidSelfSched;
	public GeneralClearingResults GeneralClearingResults;
	/**
	 * Energy is transferred between interchange areas
	 */
	public EnergyTransaction Export_EnergyTransactions;
	/**
	 * Energy is transferred between interchange areas
	 */
	public EnergyTransaction Import_EnergyTransactions;
	/**
	 * A control area can have one or more net inadvertent interchange accounts
	 */
	public InadvertentAccount InadvertentAccount;

	public SubControlArea(){

	}
}//end SubControlArea