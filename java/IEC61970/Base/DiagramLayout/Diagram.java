package TC57CIM.IEC61970.Base.DiagramLayout;

import TC57CIM.IEC61970.Base.Domain.Float;
import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * The diagram being exchanged.  The coordinate system is a standard Cartesian
 * coordinate system and the orientation attribute defines the orientation.
 * @author mcmorran
 * @version 1.0
 * @created 15-Dec-2023 4:38:27 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}