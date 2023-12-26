package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61968.Common.Agreement;

/**
 * An ad-hoc auxiliary account agreement associated with a customer agreement, not
 * part of the customer's account, but typically subject to formal agreement
 * between customer and supplier (utility). Typically this is used to collect
 * revenue owed by the customer for other services or arrears accrued with the
 * utility for other services. It is typically linked to a prepaid token purchase
 * transaction, thus forcing the customer to make a payment towards settlement of
 * the auxiliary account balance whenever the customer needs to purchase a prepaid
 * token for electricity.
 * The present status of the auxiliary agreement can be defined in the context of
 * the utility's business rules, for example: enabled, disabled, pending, over
 * recovered, under recovered, written off, etc.
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AuxiliaryAgreement extends Agreement {

	/**
	 * The interest per annum to be charged prorata on 'AuxiliaryAccount.dueArrears'
	 * at the end of each 'payCycle'.
	 */
	public PerCent arrearsInterest;
	/**
	 * The frequency for automatically recurring auxiliary charges, where
	 * 'AuxiliaryAccount.initialCharge' is recursively added to 'AuxiliaryAccount.
	 * dueCurrent' at the start of each 'auxCycle'. For example: on a specified date
	 * and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc.
	 */
	public String auxCycle;
	/**
	 * The coded priority indicating the priority that this auxiliary agreement has
	 * above other auxiliary agreements (associated with the same customer agreement)
	 * when it comes to competing for settlement from a payment transaction or token
	 * purchase.
	 */
	public String auxPriorityCode;
	/**
	 * The fixed amount that has to be collected from each vending transaction towards
	 * settlement of this auxiliary agreement. Note that there may be multiple tokens
	 * vended per vending transaction, but this is not relevant.
	 */
	public Money fixedAmount;
	/**
	 * The minimum amount that has to be paid at any transaction towards settling this
	 * auxiliary agreement or reducing the balance.
	 */
	public Money minAmount;
	/**
	 * The contractually expected payment frequency (by the customer). Examples are:
	 * ad-hoc; on specified date; hourly, daily, weekly, monthly. etc.
	 */
	public String payCycle;
	/**
	 * Sub-classification of the inherited 'type' for this AuxiliaryAgreement.
	 */
	public String subType;
	/**
	 * The percentage of the transaction amount that has to be collected from each
	 * vending transaction towards settlement of this auxiliary agreement when
	 * payments are not in arrears. Note that there may be multiple tokens vended per
	 * vending transaction, but this is not relevant.
	 */
	public PerCent vendPortion;
	/**
	 * The percentage of the transaction amount that has to be collected from each
	 * vending transaction towards settlement of this auxiliary agreement when
	 * payments are in arrears. Note that there may be multiple tokens vended per
	 * vending transaction, but this is not relevant.
	 */
	public PerCent vendPortionArrear;
	/**
	 * All auxiliary accounts regulated by this agreement.
	 */
	public AuxiliaryAccount AuxiliaryAccounts;

	public AuxiliaryAgreement(){

	}
}//end AuxiliaryAgreement