package IEC61970.Base.Generation.Production;


/**
 * The source of controls for a generating unit.
 * @created 02-Jan-2024 11:03:04 PM
 */
public enum GeneratorControlSource {
	/**
	 * Not available.
	 */
	unavailable,
	/**
	 * Off of automatic generation control (AGC).
	 */
	offAGC,
	/**
	 * On automatic generation control (AGC).
	 */
	onAGC,
	/**
	 * Plant is controlling.
	 */
	plantControl
}