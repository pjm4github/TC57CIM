package IEC61968.InfIEC61968.InfCustomers;

import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.CostPerEnergyUnit;
import IEC61968.Common.Document;

/**
 * Pricing can be based on power quality.
 * @created 29-Dec-2023 9:25:37 PM
 */
public class PowerQualityPricing extends Document {

	/**
	 * Emergency high voltage limit.
	 */
	public Voltage emergencyHighVoltLimit;
	/**
	 * Emergency low voltage limit.
	 */
	public Voltage emergencyLowVoltLimit;
	/**
	 * Normal high voltage limit.
	 */
	public Voltage normalHighVoltLimit;
	/**
	 * Normal low voltage limit.
	 */
	public Voltage normalLowVoltLimit;
	/**
	 * Threshold minimum power factor for this PricingStructure, specified in
	 * instances where a special charge is levied if the actual power factor for a
	 * Service falls below the value specified here.
	 */
	public Float powerFactorMin;
	/**
	 * Value of uninterrupted service (Cost per energy).
	 */
	public CostPerEnergyUnit valueUninterruptedServiceEnergy;
	/**
	 * Value of uninterrupted service (Cost per active power).
	 */
	public Float valueUninterruptedServiceP;
	/**
	 * Voltage imbalance violation cost (Cost per unit Voltage).
	 */
	public Float voltImbalanceViolCost;
	/**
	 * Voltage limit violation cost (Cost per unit Voltage).
	 */
	public Float voltLimitViolCost;

	public PowerQualityPricing(){

	}
}//end PowerQualityPricing