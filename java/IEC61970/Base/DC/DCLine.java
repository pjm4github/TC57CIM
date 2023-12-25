package TC57CIM.IEC61970.Base.DC;

import TC57CIM.IEC61970.Base.Core.SubGeographicalRegion;

/**
 * Overhead lines and/or cables connecting two or more HVDC substations.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
 */
public class DCLine extends DCEquipmentContainer {

	/**
	 * The SubGeographicalRegion containing the DC line.
	 */
	public SubGeographicalRegion Region;

	public DCLine(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}