///////////////////////////////////////////////////////////
//  AssetDeployment.h
//  Implementation of the Class AssetDeployment
//  Created on:      25-Dec-2023 8:45:19 PM
//  Original author: ppbr003
///////////////////////////////////////////////////////////

#if !defined(EA_86154306_5DC8_4d15_B4F9_970F15DF2DB3__INCLUDED_)
#define EA_86154306_5DC8_4d15_B4F9_970F15DF2DB3__INCLUDED_

#include "IEC61968\Assets\BreakerApplicationKind.java"
#include "IEC61968\Assets\DeploymentDate.java"
#include "IEC61968\Assets\DeploymentStateKind.java"
#include "IEC61968\Assets\FacilityKind.java"
#include "Integer.h"
#include "IEC61968\Assets\TransformerApplicationKind.java"
#include "BaseVoltage.py"
#include "IdentifiedObject.py"

/**
 * Deployment of asset deployment in a power system resource role.
 */
class AssetDeployment : public IdentifiedObject
{

public:
	AssetDeployment();
	/**
	 * Type of network role breaker is playing in this deployment (applies to breaker
	 * assets only).
	 */
	BreakerApplicationKind breakerApplication;
	/**
	 * Dates of asset deployment.
	 */
	DeploymentDate deploymentDate;
	/**
	 * Current deployment state of asset.
	 */
	DeploymentStateKind deploymentState;
	/**
	 * Kind of facility (like substation or pole or building or plant or service
	 * center) at which asset deployed.
	 */
	FacilityKind facilityKind;
	/**
	 * Likelihood of asset failure on a scale of 1(low) to 100 (high).
	 */
	Integer likelihoodOfFailure;
	/**
	 * Type of network role transformer is playing in this deployment (applies to
	 * transformer assets only).
	 */
	TransformerApplicationKind transformerApplication;
	/**
	 * Base voltage of this network asset deployment.
	 */
	BaseVoltage *BaseVoltage;

};
#endif // !defined(EA_86154306_5DC8_4d15_B4F9_970F15DF2DB3__INCLUDED_)
