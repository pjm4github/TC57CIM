package IEC61970.Base.DiagramLayout;

import IEC61970.Base.Domain.String;

/**
 * A diagram object for placing free-text or text derived from an associated
 * domain object.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TextDiagramObject extends DiagramObject {

	/**
	 * The text that is displayed by this text diagram object.
	 */
	public String text;

	public TextDiagramObject(){

	}
}//end TextDiagramObject