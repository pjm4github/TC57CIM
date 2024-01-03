package IEC61968.Assets;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.BaseVoltage;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Deployment of asset deployment in a power system resource role.
 * @author ppbr003
 * @version 1.0
 * @created 03-Jan-2024 12:00:35 PM
 */
public class AssetDeployment extends IdentifiedObject {

	/**
	 * Type of network role breaker is playing in this deployment (applies to breaker
	 * assets only).
	 */
	public BreakerApplicationKind breakerApplication;
	/**
	 * Dates of asset deployment.
	 */
	public DeploymentDate deploymentDate;
	/**
	 * Current deployment state of asset.
	 */
	public DeploymentStateKind deploymentState;
	/**
	 * Kind of facility (like substation or pole or building or plant or service
	 * center) at which asset deployed.
	 */
	public FacilityKind facilityKind;
	/**
	 * Likelihood of asset failure on a scale of 1(low) to 100 (high).
	 */
	public Integer likelihoodOfFailure;
	/**
	 * Type of network role transformer is playing in this deployment (applies to
	 * transformer assets only).
	 */
	public TransformerApplicationKind transformerApplication;
	/**
	 * Base voltage of this network asset deployment.
	 */
	public BaseVoltage BaseVoltage;

	public AssetDeployment(){

	}
}//end AssetDeployment