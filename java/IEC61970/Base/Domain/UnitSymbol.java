package IEC61970.Base.Domain;


/**
 * The derived units defined for usage in the CIM. In some cases, the derived unit
 * is equal to an SI unit. Whenever possible, the standard derived symbol is used
 * instead of the formula for the derived unit. For example, the unit symbol Farad
 * is defined as "F" instead of "CPerV". In cases where a standard symbol does not
 * exist for a derived unit, the formula for the unit is used as the unit symbol.
 * For example, density does not have a standard symbol and so it is represented
 * as "kgPerm3". With the exception of the "kg", which is an SI unit, the unit
 * symbols do not contain multipliers and therefore represent the base derived
 * unit to which a multiplier can be applied as a whole.
 * 
 * Every unit symbol is treated as an unparseable text as if it were a single-
 * letter symbol. The meaning of each unit symbol is defined by the accompanying
 * descriptive text and not by the text contents of the unit symbol.
 * 
 * To allow the widest possible range of serializations without requiring special
 * character handling, several substitutions are made which deviate from the
 * format described in IEC 80000-1. The division symbol "/" is replaced by the
 * letters"Per". Exponents are written in plain text after the unit as "m3"
 * instead of being formatted as in "m<sup>3</sup>" or introducing a symbol as in
 * "m^3". The degree symbol "ø" is replaced with the letters "deg". Any
 * clarification of the meaning for a substitution is included in the description
 * for the unit symbol.
 * 
 * Non-SI units are included in list of unit symbols to allow sources of data to
 * be correctly labeled with their non-SI units (for example, a GPS sensor that is
 * reporting numbers that represent feet instead of meters). This allows software
 * to use the unit symbol information correctly convert and scale the raw data of
 * those sources into SI-based units.
 * @created 30-Dec-2023 4:19:38 PM
 */
public enum UnitSymbol {
	/**
	 * Dimension less quantity, e.g. count, per unit, etc.
	 */
	none,
	/**
	 * Length in meter.
	 */
	m,
	/**
	 * Mass in kilogram.  Note: multiplier "k" is included in this unit symbol for
	 * compatibility with IEC 61850-7-3.
	 */
	kg,
	/**
	 * Time in seconds.
	 */
	s,
	/**
	 * Current in Ampere.
	 */
	A,
	/**
	 * Temperature in Kelvin.
	 */
	K,
	/**
	 * Amount of substance in mole.
	 */
	mol,
	/**
	 * Luminous intensity in candela.
	 */
	cd,
	/**
	 * Plane angle in degrees.
	 */
	deg,
	/**
	 * Plane angle in radian (m/m).
	 */
	rad,
	/**
	 * Solid angle in steradian (m2/m2).
	 */
	sr,
	/**
	 * Absorbed dose in Gray (J/kg).
	 */
	Gy,
	/**
	 * Radioactivity in Becquerel (1/s).
	 */
	Bq,
	/**
	 * Relative temperature in degrees Celsius.
	 * In the SI unit system the symbol is §C. Electric charge is measured in coulomb
	 * that has the unit symbol C. To distinguish degree Celsius form coulomb the
	 * symbol used in the UML is degC. Reason for not using §C is the special
	 * character § is difficult to manage in software.
	 */
	degC,
	/**
	 * Dose equivalent in Sievert (J/kg).
	 */
	Sv,
	/**
	 * Electric capacitance in Farad (C/V).
	 */
	F,
	/**
	 * Electric charge in Coulomb (Aús).
	 */
	C,
	/**
	 * Conductance in Siemens.
	 */
	S,
	/**
	 * Electric inductance in Henry (Wb/A).
	 */
	H,
	/**
	 * Electric potential in Volt (W/A).
	 */
	V,
	/**
	 * Electric resistance in ohm (V/A).
	 */
	ohm,
	/**
	 * Energy in joule (Núm = CúV = Wús).
	 */
	J,
	/**
	 * Force in Newton (kgúm/sý).
	 */
	N,
	/**
	 * Frequency in Hertz (1/s).
	 */
	Hz,
	/**
	 * Illuminance in lux (lm/mý).
	 */
	lx,
	/**
	 * Luminous flux in lumen (cdúsr).
	 */
	lm,
	/**
	 * Magnetic flux in Weber (Vús).
	 */
	Wb,
	/**
	 * Magnetic flux density in Tesla (Wb/m2).
	 */
	T,
	/**
	 * Real power in Watt (J/s). Electrical power may have real and reactive
	 * components. The real portion of electrical power (IýR or VIcos(phi)), is
	 * expressed in Watts. (See also apparent power and reactive power.)
	 */
	W,
	/**
	 * Pressure in Pascal (N/mý). Note: the absolute or relative measurement of
	 * pressure is implied with this entry. See below for more explicit forms.
	 */
	Pa,
	/**
	 * Area in square metre (mý).
	 */
	m2,
	/**
	 * Volume in cubic metre (m3).
	 */
	m3,
	/**
	 * Velocity in metre per second (m/s).
	 */
	mPers,
	/**
	 * Acceleration in metre per second squared (m/sý).
	 */
	mPers2,
	/**
	 * Volumetric flow rate in cubic metres per second (m3/s).
	 */
	m3Pers,
	/**
	 * Fuel efficiency in metre per cubic metre (m/m3).
	 */
	mPerm3,
	/**
	 * Moment of mass in kilogram metre (kgúm) (first moment of mass). Note:
	 * multiplier "k" is included in this unit symbol for compatibility with IEC 61850-
	 * 7-3.
	 */
	kgm,
	/**
	 * Density in kilogram/cubic metre (kg/m3). Note: multiplier "k" is included in
	 * this unit symbol for compatibility with IEC 61850-7-3.
	 */
	kgPerm3,
	/**
	 * Thermal conductivity in Watt/metre Kelvin.
	 */
	WPermK,
	/**
	 * Heat capacity in Joule/Kelvin.
	 */
	JPerK,
	/**
	 * Concentration in parts per million.
	 */
	ppm,
	/**
	 * Rotations per second (1/s). See also Hz (1/s).
	 */
	rotPers,
	/**
	 * Angular velocity in radians per second (rad/s).
	 */
	radPers,
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
	 * Power factor, dimensionless.
	 * Note 1: This definition of power factor only holds for balanced systems. See
	 * the alternative definition under code 153.
	 * Note 2ÿ: Beware of differing sign conventions in use between the IEC and EEI.
	 * It is assumed that the data consumer understands the type of meter in use and
	 * the sign convention in use by the utility.
	 */
	cosPhi,
	/**
	 * Volt second (Ws/A).
	 */
	Vs,
	/**
	 * Volt squared (Wý/Aý).
	 */
	V2,
	/**
	 * Ampere seconds (Aús).
	 */
	As,
	/**
	 * Ampere squared (Aý).
	 */
	A2,
	/**
	 * Ampere squared time in square ampere (Aýs).
	 */
	A2s,
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
	 * Magnetic flux in Volt per Hertz.
	 */
	VPerHz,
	/**
	 * Rate of change of frequency in Hertz per second.
	 */
	HzPers,
	/**
	 * Number of characters.
	 */
	character,
	/**
	 * Data rate (baud) in characters per second.
	 */
	charPers,
	/**
	 * Moment of mass in kilogram square metre (kgúmý) (Second moment of mass,
	 * commonly called the moment of inertia). Note: multiplier "k" is included in
	 * this unit symbol for compatibility with IEC 61850-7-3.
	 */
	kgm2,
	/**
	 * Sound pressure level in decibel. Note:  multiplier "d" is included in this unit
	 * symbol for compatibility with IEC 61850-7-3.
	 */
	dB,
	/**
	 * Ramp rate in Watt per second.
	 */
	WPers,
	/**
	 * Volumetric flow rate in litre per second.
	 */
	lPers,
	/**
	 * Power level (logrithmic ratio of signal strength , Bel-mW), normalized to 1mW.
	 * Note:  multiplier "d" is included in this unit symbol for compatibility with
	 * IEC 61850-7-3.
	 */
	dBm,
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
	 * A/m, magnetic field strength, Ampere per metre.
	 */
	APerm,
	/**
	 * volt-squared hour, Volt-squared-hours.
	 */
	V2h,
	/**
	 * ampere-squared hour, Ampere-squared hour.
	 */
	A2h,
	/**
	 * Ampere-hours, Ampere-hours.
	 */
	Ah,
	/**
	 * Amount of substance, Counter value.
	 */
	count,
	/**
	 * Volume, cubic foot.
	 */
	ft3,
	/**
	 * Volumetric flow rate, cubic metre per hour.
	 */
	m3Perh,
	/**
	 * Volume, US gallon (1 gal = 231 in3 = 128 fl ounce).
	 */
	gal,
	/**
	 * Energy, British Thermal Unit.
	 */
	Btu,
	/**
	 * Volume, litre = dm3 = m3/1000.
	 */
	l,
	/**
	 * Volumetric flow rate, litre per hour.
	 */
	lPerh,
	/**
	 * Concentration, The ratio of the volume of a solute divided by the volume of
	 * the solution. Note: Users may need use a prefix such a `æ' to express a
	 * quantity such as `æL/L'.
	 */
	lPerl,
	/**
	 * Concentration, The ratio of the mass of a solute divided by the mass of  the
	 * solution. Note: Users may need use a prefix such a `æ' to express a quantity
	 * such as `æg/g'.
	 */
	gPerg,
	/**
	 * Concentration, The amount of substance concentration, (c), the amount of
	 * solvent in moles divided by the volume of solution in m3.
	 */
	molPerm3,
	/**
	 * Concentration, Molar fraction (?), the ratio of the molar amount of a solute
	 * divided by the molar amount of the solution.
	 */
	molPermol,
	/**
	 * Concentration, Molality, the amount of solute in moles and the amount of
	 * solvent in kilograms.
	 */
	molPerkg,
	/**
	 * Time, Ratio of time Note: Users may need to supply a prefix such as `æ' to show
	 * rates such as `æs/s'
	 */
	sPers,
	/**
	 * Frequency, Rate of frequency change  Note: Users may need to supply a prefix
	 * such as `m' to show rates such as `mHz/Hz'.
	 */
	HzPerHz,
	/**
	 * Voltage, Ratio of voltages Note: Users may need to supply a prefix such as `m'
	 * to show rates such as `mV/V'.
	 */
	VPerV,
	/**
	 * Current, Ratio of Amperages  Note: Users may need to supply a prefix such as
	 * `m' to show rates such as `mA/A'.
	 */
	APerA,
	/**
	 * Power factor, PF, the ratio of the active power to the apparent power. Note:
	 * The sign convention used for power factor will differ between IEC meters and
	 * EEI (ANSI) meters. It is assumed that the data consumers understand the type of
	 * meter being used and agree on the sign convention in use at any given utility.
	 */
	VPerVA,
	/**
	 * Amount of rotation, Revolutions.
	 */
	rev,
	/**
	 * Catalytic activity, katal = mol / s.
	 */
	kat,
	/**
	 * Specific energy, Joule / kg.
	 */
	JPerkg,
	/**
	 * Volume, cubic metre, with the value uncompensated for weather effects.
	 */
	m3Uncompensated,
	/**
	 * Volume, cubic metre, with the value compensated for weather effects.
	 */
	m3Compensated,
	/**
	 * Signal Strength, Ratio of power  Note: Users may need to supply a prefix such
	 * as `m' to show rates such as `mW/W'.
	 */
	WPerW,
	/**
	 * Energy, Therm.
	 */
	therm,
	/**
	 * Wavenumber, reciprocal metre,  (1/m).
	 */
	onePerm,
	/**
	 * Specific volume, cubic metre per kilogram, v.
	 */
	m3Perkg,
	/**
	 * Dynamic viscosity, Pascal second.
	 */
	Pas,
	/**
	 * Moment of force, Newton metre.
	 */
	Nm,
	/**
	 * Surface tension, Newton per metre.
	 */
	NPerm,
	/**
	 * Angular acceleration, radian per second squared.
	 */
	radPers2,
	/**
	 * Heat flux density, irradiance, Watt per square metre.
	 */
	WPerm2,
	/**
	 * Specific heat capacity, specific entropy, Joule per kilogram Kelvin.
	 */
	JPerkgK,
	/**
	 * energy density, Joule per cubic metre.
	 */
	JPerm3,
	/**
	 * electric field strength, Volt per metre.
	 */
	VPerm,
	/**
	 * electric charge density, Coulomb per cubic metre.
	 */
	CPerm3,
	/**
	 * surface charge density, Coulomb per square metre.
	 */
	CPerm2,
	/**
	 * permittivity, Farad per metre.
	 */
	FPerm,
	/**
	 * permeability, Henry per metre.
	 */
	HPerm,
	/**
	 * molar energy, Joule per mole.
	 */
	JPermol,
	/**
	 * molar entropy, molar heat capacity, Joule per mole kelvin.
	 */
	JPermolK,
	/**
	 * exposure (x rays), Coulomb per kilogram.
	 */
	CPerkg,
	/**
	 * absorbed dose rate, Gray per second.
	 */
	GyPers,
	/**
	 * Radiant intensity, Watt per steradian.
	 */
	WPersr,
	/**
	 * radiance, Watt per square metre steradian.
	 */
	WPerm2sr,
	/**
	 * catalytic activity concentration, katal per cubic metre.
	 */
	katPerm3,
	/**
	 * Time, day = 24 h = 86400 s.
	 */
	d,
	/**
	 * Plane angle, minute.
	 */
	anglemin,
	/**
	 * Plane angle, second.
	 */
	anglesec,
	/**
	 * Area, hectare.
	 */
	ha,
	/**
	 * mass, "tonne" or "metric  ton" (1000 kg = 1 Mg).
	 */
	tonne,
	/**
	 * Pressure, bar (1 bar = 100 kPa).
	 */
	bar,
	/**
	 * Pressure, millimeter of mercury (1 mmHg is approximately 133.3 Pa).
	 */
	mmHg,
	/**
	 * Length, nautical mile (1 M = 1852 m).
	 */
	M,
	/**
	 * Speed, knot (1 kn = 1852/3600) m/s.
	 */
	kn,
	/**
	 * Volt-hour, Volt hours.
	 */
	Vh,
	/**
	 * Magnetic flux, Maxwell (1 Mx = 10-8 Wb).
	 */
	Mx,
	/**
	 * Magnetic flux density, Gauss (1 G = 10-4 T).
	 */
	G,
	/**
	 * Magnetic field, Orsted (1 Oe = (103/4p) A/m).
	 */
	Oe,
	/**
	 * Active power per current flow, watt per Ampere.
	 */
	WPerA,
	/**
	 * Conductance per length (F/m).
	 */
	SPerm,
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
	ohmPerm,
	/**
	 * Weigh per energy in kilogram/joule (kg/J). Note: multiplier "k" is included in
	 * this unit symbol for compatibility with IEC 61850-7-3.
	 */
	kgPerJ,
	/**
	 * Energy rate joule per second (J/s),
	 */
	JPers,
	/**
	 * Viscosity in metre square / second (mý/s).
	 */
	m2Pers,
	/**
	 * Insulation energy density, Joule per square metre or watt second per square
	 * metre.
	 */
	JPerm2,
	/**
	 * Temperature change rate in Kelvin per second.
	 */
	KPers,
	/**
	 * Pressure change rate in Pascal per second.
	 */
	PaPers
}