package IEC61970.Base.DC;

import IEC61970.Base.Core.SubGeographicalRegion;

/**
 * Overhead lines and/or cables connecting two or more HVDC substations.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DCLine extends DCEquipmentContainer {

	/**
	 * The SubGeographicalRegion containing the DC line.
	 */
	public SubGeographicalRegion Region;

	public DCLine(){

	}
}//end DCLine