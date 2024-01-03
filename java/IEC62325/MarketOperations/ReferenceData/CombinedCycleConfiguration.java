package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Boolean;

/**
 * Configuration options for combined cycle units.
 * For example, a Combined Cycle with (CT1, CT2, ST1) will have (CT1, ST1) and
 * (CT2, ST1) configurations as part of(1CT + 1STlogicalconfiguration).
 * @created 03-Jan-2024 2:15:33 PM
 */
public class CombinedCycleConfiguration extends RegisteredGenerator {

	/**
	 * Whether this CombinedCycleConfiguration is the primary configuration in the
	 * associated Logical configuration?
	 */
	public Boolean primaryConfiguration;
	/**
	 * Whether Combined Cycle Plant can be shut-down in this Configuration?
	 */
	public Boolean ShutdownFlag;
	/**
	 * Whether Combined Cycle Plant can be started in this Logical Configuration?
	 */
	public Boolean StartupFlag;
	public CombinedCycleTransitionState ToTransitionState;
	public CombinedCycleTransitionState FromTransitionState;
	public CombinedCycleConfigurationMember CombinedCycleConfigurationMember;

	public CombinedCycleConfiguration(){

	}
}//end CombinedCycleConfiguration