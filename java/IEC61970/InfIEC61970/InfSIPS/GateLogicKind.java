package IEC61970.InfIEC61970.InfSIPS;


/**
 * Define the different logical operations.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:36:01 PM
 */
public enum GateLogicKind {
	/**
	 * A logical AND operation. True when all input are true.
	 */
	and,
	/**
	 * A logical OR operation. True when one or more input are true.
	 */
	or,
	/**
	 * A logical NOR operation. False when one or more input are true.
	 */
	nor,
	/**
	 * A logical NAND operation. False when all input are true.
	 */
	nand,
	/**
	 * A logical NOT operation. Only one input and true input will give false out and
	 * false in will give true out. An inverter.
	 */
	not,
	/**
	 * A logical XNOR operation. The function is the inverse of the exclusive OR (XOR)
	 * gate. All input false or true will give true. Otherwise false.
	 */
	xnor,
	/**
	 * A logical XOR operation.  All input false or true will give false. Otherwise
	 * true.
	 */
	xor
}