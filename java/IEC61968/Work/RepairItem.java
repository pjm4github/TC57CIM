package IEC61968.Work;


/**
 * Asset component to be repaired or problem area to be corrected.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class RepairItem {

	/**
	 * Breaker component or problem area which is the focus of this maintenance work
	 * task (for work tasks related to breakers only).
	 */
	public BreakerRepairItemKind breakerRepairItem;
	/**
	 * Transformer component or problem area which is the focus of this maintenance
	 * work task (for work tasks related to transformers only).
	 */
	public TransformerRepairItemKind transformerRepairItem;
	/**
	 * Repair work task under which breaker item of this type is repaired.
	 */
	public RepairWorkTask RepairWorkTask;

	public RepairItem(){

	}
}//end RepairItem