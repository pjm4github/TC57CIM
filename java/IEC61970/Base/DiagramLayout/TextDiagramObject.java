package TC57CIM.IEC61970.Base.DiagramLayout;

import TC57CIM.IEC61970.Base.Domain.String;

/**
 * A diagram object for placing free-text or text derived from an associated
 * domain object.
 * @author mcmorran
 * @version 1.0
 * @created 15-Dec-2023 4:38:30 PM
 */
public class TextDiagramObject extends DiagramObject {

	/**
	 * The text that is displayed by this text diagram object.
	 */
	public String text;

	public TextDiagramObject(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}