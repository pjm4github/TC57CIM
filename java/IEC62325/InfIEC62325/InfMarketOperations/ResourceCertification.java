package IEC62325.InfIEC62325.InfMarketOperations;

import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.Float;

/**
 * This class represent the resource certification for a specific product type.
 * For example, a resource is certified for Non-Spinning reserve for RTM.
 * @created 03-Jan-2024 1:53:43 PM
 */
public class ResourceCertification {

	public YesNo certifiedDAM;
	public YesNo certifiedNonspinDAM;
	public Float certifiedNonspinDAMMw;
	public YesNo certifiedNonspinRTM;
	public Float certifiedNonspinRTMMw;
	public YesNo certifiedPIRP;
	public YesNo certifiedRegulation;
	public Float certifiedRegulationMw;
	public YesNo certifiedReplaceAS;
	public YesNo certifiedRTM;
	public YesNo certifiedRUC;
	public YesNo certifiedSpin;
	public Float certifiedSpinMw;

	public ResourceCertification(){

	}
}//end ResourceCertification