package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Money;
import IEC61968.Work.Work;

/**
 * A design for consideration by customers, potential customers, or internal work.
 * 
 * Note that the Version of design is the revision attribute that is inherited
 * from Document.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class Design extends WorkDocument {

	/**
	 * Estimated cost (not price) of design.
	 */
	public Money costEstimate;
	/**
	 * Kind of this design.
	 */
	public DesignKind kind;
	/**
	 * Price to customer for implementing design.
	 */
	public Money price;
	public WorkCostDetail WorkCostDetails;
	public ErpBOM ErpBOMs;
	public OldWorkTask WorkTasks;
	public ConditionFactor ConditionFactors;
	public Work Work;

	public Design(){

	}
}//end Design