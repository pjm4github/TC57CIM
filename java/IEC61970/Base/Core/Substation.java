package IEC61970.Base.Core;

import IEC61970.Base.DC.DCConverterUnit;

/**
 * A collection of equipment for purposes other than generation or utilization,
 * through which electric energy in bulk is passed for the purposes of switching
 * or modifying its characteristics.
 * @created 02-Jan-2024 10:37:56 PM
 */
public class Substation extends EquipmentContainer {

	/**
	 * The voltage levels within this substation.
	 */
	public VoltageLevel VoltageLevels;
	/**
	 * Bays contained in the substation.
	 */
	public Bay Bays;
	/**
	 * The DC converter unit belonging of the substation.
	 */
	public DCConverterUnit DCConverterUnit;
	/**
	 * The normal energized feeders of the substation. Also used for naming purposes.
	 */
	public Feeder NormalEnergizedFeeder;

	public Substation(){

	}
}//end Substation