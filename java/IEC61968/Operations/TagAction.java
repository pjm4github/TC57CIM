package IEC61968.Operations;


/**
 * Action on operation tag as a switching step.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TagAction extends SwitchingAction {

	/**
	 * Kind of tag action.
	 */
	public TagActionKind kind;
	/**
	 * Tag associated with this tag action.
	 */
	public OperationalTag OperationalTag;

	public TagAction(){

	}
}//end TagAction