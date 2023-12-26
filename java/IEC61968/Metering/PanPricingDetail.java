package IEC61968.Metering;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Integer;

/**
 * Detail for a single price command/action.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class PanPricingDetail {

	/**
	 * Alternative measure of the cost of the energy consumed. An example might be the
	 * emissions of CO2 for each kWh of electricity consumed providing a measure of
	 * the environmental cost.
	 */
	public Float alternateCostDelivered;
	/**
	 * Cost unit for the alternate cost delivered field. One example is kg of CO2 per
	 * unit of measure.
	 */
	public String alternateCostUnit;
	/**
	 * Current time as determined by a PAN device.
	 */
	public DateTime currentTimeDate;
	/**
	 * Price of the commodity measured in base unit of currency per 'unitOfMeasure'.
	 */
	public Money generationPrice;
	/**
	 * Ratio of 'generationPrice' to the "normal" price chosen by the commodity
	 * provider.
	 */
	public Float generationPriceRatio;
	/**
	 * Price of the commodity measured in base unit of currency per 'unitOfMeasure'.
	 */
	public Money price;
	/**
	 * Ratio of 'price' to the "normal" price chosen by the commodity provider.
	 */
	public Float priceRatio;
	/**
	 * Pricing tier as chosen by the commodity provider.
	 */
	public Integer priceTier;
	/**
	 * Maximum number of price tiers available.
	 */
	public Integer priceTierCount;
	/**
	 * Label for price tier.
	 */
	public String priceTierLabel;
	/**
	 * Label of the current billing rate specified by commodity provider.
	 */
	public String rateLabel;
	/**
	 * Register tier accumulating usage information.
	 */
	public String registerTier;
	/**
	 * Defines commodity as well as its base unit of measure.
	 */
	public String unitOfMeasure;

	public PanPricingDetail(){

	}
}//end PanPricingDetail