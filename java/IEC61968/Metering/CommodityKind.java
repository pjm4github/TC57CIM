package IEC61968.Metering;


/**
 * Kind of commodity being measured.
 * @author Marty
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum CommodityKind {
	/**
	 * Not Applicable
	 */
	none,
	/**
	 * All types of metered quantities. This type of reading comes from the meter and
	 * represents a "secondary" metered value.
	 */
	electricitySecondaryMetered,
	/**
	 * It is possible for a meter to be outfitted with an external VT and/or CT. The
	 * meter might not be aware of these devices, and the display not compensate for
	 * their presence. Ultimately, when these scalars are applied, the value that
	 * represents the service value is called the "primary metered" value. The "index"
	 * in sub-category 3 mirrors those of sub-category 0.
	 */
	electricityPrimaryMetered,
	/**
	 * A measurement of the communication infrastructure itself.
	 */
	communication,
	air,
	/**
	 * (SF<sub>6</sub> is found separately below.)
	 */
	insulativeGas,
	insulativeOil,
	naturalGas,
	propane,
	/**
	 * Drinkable water
	 */
	potableWater,
	/**
	 * Water in steam form, usually used for heating.
	 */
	steam,
	/**
	 * (Sewerage)
	 */
	wasteWater,
	/**
	 * This fluid is likely in liquid form. It is not necessarily water or water based.
	 * The warm fluid returns cooler than when it was sent. The heat conveyed may be
	 * metered.
	 */
	heatingFluid,
	/**
	 * The cool fluid returns warmer than when it was sent. The heat conveyed may be
	 * metered.
	 */
	coolingFluid,
	/**
	 * Reclaimed water - possibly used for irrigation but not sufficiently treated to
	 * be considered safe for drinking.
	 */
	nonpotableWater,
	/**
	 * Nitrous Oxides NO<sub>X</sub>
	 */
	nox,
	/**
	 * Sulfur Dioxide SO<sub>2</sub>
	 */
	so2,
	/**
	 * Methane CH<sub>4</sub>
	 */
	ch4,
	/**
	 * Carbon Dioxide CO<sub>2</sub>
	 */
	co2,
	carbon,
	/**
	 * Hexachlorocyclohexane HCH
	 */
	hch,
	/**
	 * Perfluorocarbons PFC
	 */
	pfc,
	/**
	 * Sulfurhexafluoride SF<sub>6</sub>
	 */
	sf6,
	/**
	 * Television
	 */
	tvLicence,
	/**
	 * Internet service
	 */
	internet,
	/**
	 * trash
	 */
	refuse
}