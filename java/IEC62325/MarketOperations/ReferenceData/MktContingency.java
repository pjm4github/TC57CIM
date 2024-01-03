package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Contingency.Contingency;

/**
 * Subclass of IEC 61970:Contingency.
 * @created 29-Dec-2023 1:40:35 PM
 */
public class MktContingency extends Contingency {

	/**
	 * load change flag
	 * Flag that indicates whether load rollover and load pickup should be processed
	 * for this contingency
	 */
	public Boolean loadRolloverFlag;
	/**
	 * ltc enable flag
	 * Flag that indicates if LTCs regulate voltage during the solution of the
	 * contingency
	 */
	public Boolean ltcControlFlag;
	/**
	 * Participation Factor flag
	 * An indication which set of generator participation factors should be used to re-
	 * allocate generation in this contingency
	 */
	public String participationFactorSet;
	/**
	 * sceening flag for outage
	 * Flag that indicated whether screening is bypassed for the contingency
	 */
	public Boolean screeningFlag;

	public MktContingency(){

	}
}//end MktContingency