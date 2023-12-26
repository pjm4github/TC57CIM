package IEC61968.Common;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.String;

/**
 * Set of spatial coordinates that determine a point, defined in the coordinate
 * system specified in 'Location.CoordinateSystem'. Use a single position point
 * instance to desribe a point-oriented location. Use a sequence of position
 * points to describe a line-oriented object (physical location of non-point
 * oriented objects like cables or lines), or area of an object (like a substation
 * or a geographical zone - in this case, have first and last position point with
 * the same values).
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class PositionPoint {

	/**
	 * Zero-relative sequence number of this group within a series of points; used
	 * when there is a need to express disjoint groups of points that are considered
	 * to be part of a single location.
	 */
	public Integer groupNumber;
	/**
	 * Zero-relative sequence number of this point within a series of points.
	 */
	public Integer sequenceNumber;
	/**
	 * X axis position.
	 */
	public String xPosition;
	/**
	 * Y axis position.
	 */
	public String yPosition;
	/**
	 * (if applicable) Z axis position.
	 */
	public String zPosition;

	public PositionPoint(){

	}
}//end PositionPoint