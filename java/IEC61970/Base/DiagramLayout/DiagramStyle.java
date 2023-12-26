package IEC61970.Base.DiagramLayout;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * The diagram style refer to a style used by the originating system for a diagram.
 *  A diagram style describes information such as schematic, geographic, bus-
 * branch etc.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiagramStyle extends IdentifiedObject {

	/**
	 * A DiagramStyle can be used by many Diagrams.
	 */
	public Diagram Diagram;

	public DiagramStyle(){

	}
}//end DiagramStyle