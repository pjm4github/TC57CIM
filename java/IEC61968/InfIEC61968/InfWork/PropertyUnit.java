package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Status;

/**
 * Unit of property for reporting purposes.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class PropertyUnit extends WorkIdentifiedObject {

	/**
	 * A code that identifies appropriate type of property accounts such as
	 * distribution, streetlgihts, communications.
	 */
	public String accountingUsage;
	/**
	 * Activity code identifies a specific and distinguishable work action.
	 */
	public WorkActionKind activityCode;
	/**
	 * Used for property record accounting. For example, in the USA, this would be a
	 * FERC account.
	 */
	public String propertyAccount;
	public Status status;
	public CUMaterialItem CUMaterialItems;
	public CompatibleUnit CompatibleUnits;

	public PropertyUnit(){

	}
}//end PropertyUnit