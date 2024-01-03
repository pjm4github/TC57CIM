package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * This class models the transmission (either a transmission interface or a
 * POR/POD pair) capacity including Total Transfer Capacity (TTC), Operating
 * Transfer Capacity (OTC), and Capacity Benefit Margin (CBM).
 * @created 03-Jan-2024 2:08:11 PM
 */
public class TransmissionCapacity {

	/**
	 * Capacity Benefit Margin (CBM) is used by Markets to calculate the transmission
	 * interface limits. This number could be manually or procedurally determined. The
	 * CBM is defined per transmission interface (branch group).
	 */
	public Float capacityBenefitMargin;
	/**
	 * The Operational Transmission Capacity (OTC) is the transmission capacity under
	 * the operating condition during a specific time period, incorporating the
	 * effects of derates and current settings of operation controls. The OTCs for all
	 * transmission interface (branch group) are always provided regardless of outage
	 * or switching conditions.
	 */
	public Float operationalTransmissionCapacity;
	/**
	 * The Operational Transmission Capacity (OTC) 15 minute Emergency Limit
	 */
	public Float OTC15min_emergency;
	/**
	 * The Operational Transmission Capacity (OTC) Emergency Limit.
	 */
	public Float OTCemergency;
	/**
	 * point of delivery
	 */
	public String POD;
	/**
	 * point of receipt
	 */
	public String POR;
	/**
	 * Operating date & hour when the entitlement applies
	 */
	public DateTime startOperatingDate;
	/**
	 * Total Transmission Capacity
	 */
	public Float totalTransmissionCapacity;

	public TransmissionCapacity(){

	}
}//end TransmissionCapacity