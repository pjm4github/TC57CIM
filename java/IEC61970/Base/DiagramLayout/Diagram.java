package IEC61970.Base.DiagramLayout;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The diagram being exchanged.  The coordinate system is a standard Cartesian
 * coordinate system and the orientation attribute defines the orientation.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class Diagram extends IdentifiedObject {

	/**
	 * Coordinate system orientation of the diagram.
	 */
	public OrientationKind orientation;
	/**
	 * X coordinate of the first corner of the initial view.
	 */
	public Float x1InitialView;
	/**
	 * X coordinate of the second corner of the initial view.
	 */
	public Float x2InitialView;
	/**
	 * Y coordinate of the first corner of the initial view.
	 */
	public Float y1InitialView;
	/**
	 * Y coordinate of the second corner of the initial view.
	 */
	public Float y2InitialView;

	public Diagram(){

	}
}//end Diagram