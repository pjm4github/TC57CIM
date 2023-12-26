package IEC61970.Base.DiagramLayout;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.AngleDegrees;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An object that defines one or more points in a given space. This object can be
 * associated with anything that specializes IdentifiedObject. For single line
 * diagrams such objects typically include such items as analog values, breakers,
 * disconnectors, power transformers, and transmission lines.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiagramObject extends IdentifiedObject {

	/**
	 * The drawing order of this element. The higher the number, the later the element
	 * is drawn in sequence. This is used to ensure that elements that overlap are
	 * rendered in the correct order.
	 */
	public Integer drawingOrder;
	/**
	 * Defines whether or not the diagram objects points define the boundaries of a
	 * polygon or the routing of a polyline. If this value is true then a receiving
	 * application should consider the first and last points to be connected.
	 */
	public Boolean isPolygon;
	/**
	 * The offset in the X direction. This is used for defining the offset from centre
	 * for rendering an icon (the default is that a single point specifies the centre
	 * of the icon).
	 * 
	 * The offset is in per-unit with 0 indicating there is no offset from the
	 * horizontal centre of the icon.  -0.5 indicates it is offset by 50% to the left
	 * and 0.5 indicates an offset of 50% to the right.
	 */
	public Float offsetX;
	/**
	 * The offset in the Y direction. This is used for defining the offset from centre
	 * for rendering an icon (the default is that a single point specifies the centre
	 * of the icon).
	 * 
	 * The offset is in per-unit with 0 indicating there is no offset from the
	 * vertical centre of the icon.  The offset direction is dependent on the
	 * orientation of the diagram, with -0.5 and 0.5 indicating an offset of +/- 50%
	 * on the vertical axis.
	 */
	public Float offsetY;
	/**
	 * Sets the angle of rotation of the diagram object.  Zero degrees is pointing to
	 * the top of the diagram.  Rotation is clockwise.
	 */
	public AngleDegrees rotation;
	/**
	 * A diagram object is part of a diagram.
	 */
	public Diagram Diagram;
	/**
	 * A diagram object can be part of multiple visibility layers.
	 */
	public VisibilityLayer VisibilityLayers;
	/**
	 * A diagram object can have 0 or more points to reflect its layout position,
	 * routing (for polylines) or boundary (for polygons).
	 */
	public DiagramObjectPoint DiagramObjectPoints;
	/**
	 * A diagram object has a style associated that provides a reference for the style
	 * used in the originating system.
	 */
	public DiagramObjectStyle DiagramObjectStyle;

	public DiagramObject(){

	}
}//end DiagramObject