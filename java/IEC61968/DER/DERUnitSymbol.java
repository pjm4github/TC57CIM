package IEC61968.DER;


/**
 * The units defined for usage in the CIM.
 * @created 03-Jan-2024 12:20:05 PM
 */
public enum DERUnitSymbol {
	/**
	 * Time in seconds.
	 */
	s,
	/**
	 * Current in Ampere.
	 */
	A,
	/**
	 * Plane angle in degrees.
	 */
	deg,
	/**
	 * Relative temperature in degrees Celsius.
	 * In the SI unit system the symbol is §C. Electric charge is measured in coulomb
	 * that has the unit symbol C. To distinguish degree Celsius form coulomb the
	 * symbol used in the UML is degC. Reason for not using §C is the special
	 * character § is difficult to manage in software.
	 */
	degC,
	/**
	 * Electric potential in Volt (W/A).
	 */
	V,
	/**
	 * Electric resistance in ohm (V/A).
	 */
	ohm,
	/**
	 * Frequency in Hertz (1/s).
	 */
	Hz,
	/**
	 * Real power in Watt (J/s). Electrical power may have real and reactive
	 * components. The real portion of electrical power (IýR or VIcos(phi)), is
	 * expressed in Watts. (See also apparent power and reactive power.)
	 */
	W,
	/**
	 * Apparent power in Volt Ampere (See also real power and reactive power.)
	 */
	VA,
	/**
	 * Reactive power in Volt Ampere reactive. The "reactive" or "imaginary" component
	 * of electrical power (VIsin(phi)). (See also real power and apparent power).
	 * Note: Different meter designs use different methods to arrive at their results.
	 * Some meters may compute reactive power as an arithmetic value, while others
	 * compute the value vectorially. The data consumer should determine the method in
	 * use and the suitability of the measurement for the intended purpose.
	 */
	VAr,
	/**
	 * Volt second (Ws/A).
	 */
	Vs,
	/**
	 * Ampere seconds (Aús).
	 */
	As,
	/**
	 * Apparent energy in Volt Ampere hours.
	 */
	VAh,
	/**
	 * Real energy in Watt hours.
	 */
	Wh,
	/**
	 * Reactive energy in Volt Ampere reactive hours.
	 */
	VArh,
	/**
	 * Ramp rate in Watt per second.
	 */
	WPers,
	/**
	 * Time, hour = 60 min = 3600 s.
	 */
	h,
	/**
	 * Time, minute  = 60 s.
	 */
	min,
	/**
	 * Quantity power, Q.
	 */
	Q,
	/**
	 * Quantity energy, Qh.
	 */
	Qh,
	/**
	 * resistivity, Ohm metre, (rho).
	 */
	ohmm,
	/**
	 * Ampere-hours, Ampere-hours.
	 */
	Ah,
	/**
	 * Energy, British Thermal Unit.
	 */
	Btu,
	/**
	 * Power factor, PF, the ratio of the active power to the apparent power. Note:
	 * The sign convention used for power factor will differ between IEC meters and
	 * EEI (ANSI) meters. It is assumed that the data consumers understand the type of
	 * meter being used and agree on the sign convention in use at any given utility.
	 */
	VPerVA,
	/**
	 * Energy, Therm.
	 */
	therm,
	/**
	 * Volt-hour, Volt hours.
	 */
	Vh,
	/**
	 * Active power per current flow, watt per Ampere.
	 */
	WPerA,
	/**
	 * Reciprocal of frequency (1/Hz).
	 */
	onePerHz,
	/**
	 * Power factor, PF, the ratio of the active power to the apparent power. Note:
	 * The sign convention used for power factor will differ between IEC meters and
	 * EEI (ANSI) meters. It is assumed that the data consumers understand the type of
	 * meter being used and agree on the sign convention in use at any given utility.
	 */
	VPerVAr,
	/**
	 * Electric resistance per length in ohm per metre ((V/A)/m).
	 */
	ohmPerm
}