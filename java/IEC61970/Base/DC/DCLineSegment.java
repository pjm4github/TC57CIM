package IEC61970.Base.DC;

import IEC61970.Base.Domain.Capacitance;
import IEC61970.Base.Domain.Inductance;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.Resistance;

/**
 * A wire or combination of wires not insulated from one another, with consistent
 * electrical characteristics, used to carry direct current between points in the
 * DC region of the power system.
 * @created 02-Jan-2024 10:41:05 PM
 */
public class DCLineSegment extends DCConductingEquipment {

	/**
	 * Capacitance of the DC line segment. Significant for cables only.
	 */
	public Capacitance capacitance;
	/**
	 * Inductance of the DC line segment. Neglectable compared with DCSeriesDevice
	 * used for smoothing.
	 */
	public Inductance inductance;
	/**
	 * Segment length for calculating line section capabilities.
	 */
	public Length length;
	/**
	 * Resistance of the DC line segment.
	 */
	public Resistance resistance;

	public DCLineSegment(){

	}
}//end DCLineSegment