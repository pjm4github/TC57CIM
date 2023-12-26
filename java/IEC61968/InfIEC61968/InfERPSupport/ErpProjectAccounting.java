import IEC61968.InfIEC61968.InfWork.Project;

/**
 * Utility Project Accounting information, used by ERP applications to enable all
 * relevant sub-systems that submit single sided transactions to transfer
 * information with a Project Accounting Application. This would include, but not
 * necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order
 * Management, Purchasing, Time and Labor, Travel and Expense.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpProjectAccounting extends ErpDocument {

	public Project Projects;

	public ErpProjectAccounting(){

	}
}//end ErpProjectAccounting