import IEC61970.Base.Domain.String;
import IEC61968.InfIEC61968.InfCommon.BankAccount;

/**
 * Relationship under a particular name, usually evidenced by a deposit against
 * which withdrawals can be made. Types of bank accounts include: demand, time,
 * custodial, joint, trustee, corporate, special, and regular accounts.
 * A statement of transactions during a fiscal period and the resulting balance is
 * maintained on each account.
 * For Payment metering, the account is associated with Bank and Supplier,
 * reflecting details of the bank account used for depositing revenue collected by
 * TokenVendor. The name of the account holder should be specified in 'name'
 * attribute.
 * @created 03-Jan-2024 12:36:37 PM
 */
public class ErpBankAccount extends BankAccount {

	/**
	 * Bank ABA.
	 */
	public String bankABA;

	public ErpBankAccount(){

	}
}//end ErpBankAccount