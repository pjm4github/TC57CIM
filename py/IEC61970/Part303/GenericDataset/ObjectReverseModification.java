package IEC61970.Part303.GenericDataset;


/**
 * Used to specify precondition properties for a preconditioned update.
 * @author 222206
 * @version 1.0
 * @created 22-Dec-2023 4:59:45 PM
 */
public class ObjectReverseModification extends ChangeSetMember {

	/**
	 * The associated data object representing the update. Normally the associaiton is
	 * specifed, but in the case of a proxy object where the association is removed,
	 * we might not reference any data object as it would only reference a proxy data
	 * object with no associations.
	 */
	public ObjectModification ObjectModification;

	public ObjectReverseModification(){

	}
}//end ObjectReverseModification