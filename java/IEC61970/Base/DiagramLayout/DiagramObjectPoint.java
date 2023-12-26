package IEC61970.Base.DiagramLayout;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;

/**
 * A point in a given space defined by 3 coordinates and associated to a diagram
 * object.  The coordinates may be positive or negative as the origin does not
 * have to be in the corner of a diagram.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiagramObjectPoint {

	/**
	 * The sequence position of the point, used for defining the order of points for
	 * diagram objects acting as a polyline or polygon with more than one point.
	 */
	public Integer sequenceNumber;
	/**
	 * The X coordinate of this point.
	 */
	public Float xPosition;
	/**
	 * The Y coordinate of this point.
	 */
	public Float yPosition;
	/**
	 * The Z coordinate of this point.
	 */
	public Float zPosition;
	/**
	 * The 'glue' point to which this point is associated.
	 */
	public DiagramObjectGluePoint DiagramObjectGluePoint;

	public DiagramObjectPoint(){

	}
}//end DiagramObjectPoint