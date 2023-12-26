package IEC62325.Environmental.EnvDomain;


/**
 * Fujita scale (referred to as EF-scale starting in 2007) for tornado damage.  A
 * set of wind estimates (not measurements) based on damage. It uses three-second
 * gusts estimated at the point of damage based on a judgment of 8 levels of
 * damage to 28 indicators. These estimates vary with height and exposure.
 * The 3 second gust is not the same wind as in standard surface observations.
 * Enumerations based on NOAA conventions.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public enum FScale {
	/**
	 * 65-85 mph 3-second gust.
	 */
	zero,
	/**
	 * 86-110 mph 3-second gust.
	 */
	one,
	/**
	 * 111-135 mph 3-second gust.
	 */
	two,
	/**
	 * 136-165 mph 3-second gust.
	 */
	three,
	/**
	 * 166-200 mph 3-second gust.
	 */
	four,
	/**
	 * Over 200 mph 3-second gust.
	 */
	five,
	/**
	 * Unknown.
	 */
	minusNine
}