package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ReferenceData.SubControlArea;

/**
 * Provides the MW loss for RUC Zones, subcontrol areas, and the total loss.
 * @created 28-Dec-2023 8:22:26 PM
 */
public class LossClearingResults {

	public Float lossMW;
	public SubControlArea SubControlArea;

	public LossClearingResults(){

	}
}//end LossClearingResults