package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.SubControlArea;

/**
 * Model results of ex-post calculation of MW losses. Summarizes loss in two
 * categories losses on the the extra high voltage transmission and total losses.
 * Calculated for each subcontrol area.
 * @created 28-Dec-2023 8:20:21 PM
 */
public class ExPostLossResults {

	/**
	 * EHV MW losses in the company
	 * Attribute Usage: Information purposes - Output of LPA engine.
	 */
	public Float ehvLossMW;
	/**
	 * Total MW losses in the company
	 * Attribute Usage: Information purposes - Output of LPA engine.
	 */
	public Float totalLossMW;
	public SubControlArea SubControlArea;
	public ExPostLoss ExPostLoss;

	public ExPostLossResults(){

	}
}//end ExPostLossResults