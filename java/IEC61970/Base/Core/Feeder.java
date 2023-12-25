package TC57CIM.IEC61970.Base.Core;


/**
 * A collection of equipment for organizational purposes, used for grouping
 * distribution resources.
 * The organization a feeder does not necessarily reflect connectivity or current
 * operation state.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class Feeder extends EquipmentContainer {

	/**
	 * The secondary substations that are normally energized from the feeder.  Used
	 * for naming purposes.   Should be consistent with the other associations for
	 * energizing terminal specification and the feeder energization specification.
	 */
	public Substation NamingSecondarySubstation;
	/**
	 * The normal head terminal or terminals of the feeder.
	 */
	public Terminal NormalHeadTerminal;
	/**
	 * The substations that are normally energized by the feeder.
	 */
	public Substation NormalEnergizedSubstation;

	public Feeder(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}