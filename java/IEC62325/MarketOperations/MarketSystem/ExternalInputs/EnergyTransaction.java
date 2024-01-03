package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.EnergyTransactionType;
import IEC62325.InfIEC62325.InfEnergyScheduling.TieLine;
import IEC62325.MarketOperations.ParticipantInterfaces.EnergyPriceCurve;
import IEC62325.InfIEC62325.InfEnergyScheduling.EnergyProduct;
import IEC61968.Common.Document;
import IEC62325.InfIEC62325.InfEnergyScheduling.CurtailmentProfile;
import IEC62325.InfIEC62325.InfEnergyScheduling.LossProfile;

/**
 * Specifies the schedule for energy transfers between interchange areas that are
 * necessary to satisfy the associated interchange transaction.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class EnergyTransaction extends Document {

	/**
	 * Interchange capacity flag. When the flag is set to true, it indicates a
	 * transaction is capacity backed. 
	 */
	public Boolean capacityBacked;
	/**
	 * Maximum congestion charges in monetary units.
	 */
	public Money congestChargeMax;
	/**
	 * Delivery point active power.
	 */
	public ActivePower deliveryPointP;
	/**
	 * Transaction minimum active power if dispatchable.
	 */
	public ActivePower energyMin;
	/**
	 * Firm interchange flag indicates whether or not this energy transaction can be
	 * changed without potential financial consequences.
	 */
	public Boolean firmInterchangeFlag;
	/**
	 * Willing to Pay congestion flag
	 */
	public Boolean payCongestion;
	/**
	 * Reason for energy transaction.
	 */
	public String reason;
	/**
	 * Receipt point active power.
	 */
	public ActivePower receiptPointP;
	/**
	 * { Approve | Deny | Study }
	 */
	public EnergyTransactionType state;
	/**
	 * A dynamic energy transaction can act as a pseudo tie line.
	 */
	public TieLine TieLines;
	public EnergyPriceCurve EnergyPriceCurves;
	/**
	 * The "Source" for an EnergyTransaction is an EnergyProduct which is injected
	 * into a ControlArea. Typically this is a ServicePoint.
	 */
	public EnergyProduct EnergyProduct;
	/**
	 * An EnergyTransaction shall have at least one EnergyProfile.
	 */
	public EnergyProfile EnergyProfiles;
	/**
	 * An EnergyTransaction may be curtailed by any of the participating entities.
	 */
	public CurtailmentProfile CurtailmentProfiles;
	/**
	 * An EnergyTransaction may have a LossProfile.
	 */
	public LossProfile LossProfiles;

	public EnergyTransaction(){

	}
}//end EnergyTransaction