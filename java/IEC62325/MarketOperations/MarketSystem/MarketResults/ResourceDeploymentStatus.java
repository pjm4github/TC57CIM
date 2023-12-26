package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Float;

/**
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourceDeploymentStatus {

	/**
	 * Commenst to explain why the acceptance status. For example, to explain why a
	 * request is accepted only partially, instead of fully.
	 */
	public String acceptComments;
	/**
	 * Status of the resource for this deployment. Values include (full compliance,
	 * partial compliance, opt-out, etc.)
	 */
	public String acceptStatus;
	/**
	 * The MW amount the resource can contribute for this deployment. This is from the
	 * DR provider - as a response? Or actual? Does this belong in settlement? Discuss
	 * more.
	 */
	public Float resourceResponseMW;

	public ResourceDeploymentStatus(){

	}
}//end ResourceDeploymentStatus