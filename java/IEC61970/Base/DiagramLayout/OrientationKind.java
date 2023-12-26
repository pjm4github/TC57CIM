package IEC61970.Base.DiagramLayout;


/**
 * The orientation of the coordinate system with respect to top, left, and the
 * coordinate number system.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public enum OrientationKind {
	/**
	 * For 2D diagrams, a positive orientation will result in X values increasing from
	 * left to right and Y values increasing from bottom to top.  This is also known
	 * as a right hand orientation.
	 */
	positive,
	/**
	 * For 2D diagrams, a negative orientation gives the left-hand orientation
	 * (favoured by computer graphics displays) with X values increasing from left to
	 * right and Y values increasing from top to bottom.   This is also known as a
	 * left hand orientation.
	 */
	negative
}