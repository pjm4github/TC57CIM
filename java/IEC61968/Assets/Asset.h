///////////////////////////////////////////////////////////
//  Asset.h
//  Implementation of the Class Asset
//  Created on:      25-Dec-2023 8:45:19 PM
///////////////////////////////////////////////////////////

#if !defined(EA_4AAB4750_294A_43ed_8F88_6BDC6A4F8AD9__INCLUDED_)
#define EA_4AAB4750_294A_43ed_8F88_6BDC6A4F8AD9__INCLUDED_

#include "IEC61968\Assets\AcceptanceTest.java"
#include "String.h"
#include "PerCent.py"
#include "Boolean.h"
#include "ElectronicAddress.h"
#include "IEC61968\Assets\InUseDate.java"
#include "IEC61968\Assets\InUseStateKind.java"
#include "IEC61968\Assets\AssetKind.java"
#include "IEC61968\Assets\LifecycleDate.java"
#include "IEC61968\Assets\AssetLifecycleStateKind.java"
#include "Money.py"
#include "IEC61968\Assets\RetiredReasonKind.java"
#include "Status.py"
#include "\ErpInventory.java"
#include "IEC61968\Assets\AssetOrganisationRole.java"
#include "AssetFunction.h"
#include "PowerSystemResource.py"
#include "AssetContainer.py"
#include "AssetPropertyCurve.h"
#include "IdentifiedObject.py"
#include "\ErpRecDelvLineItem.java"
#include "AssetDeployment.h"
#include "Reconditioning.h"
#include "IEC61968\Assets\AssetInfo.java"
#include "Measurement.py"
#include "IEC61968\Assets\ProductAssetModel.java"
#include "ConfigurationEvent.py"
#include "IEC61968\Common\Location.java"
#include "ActivityRecord.py"

/**
 * Tangible resource of the utility, including power system equipment, various end
 * devices, cabinets, buildings, etc. For electrical network equipment, the role
 * of the asset is defined through PowerSystemResource and its subclasses, defined
 * mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::
 * Wires). Asset description places emphasis on the physical characteristics of
 * the equipment fulfilling that role.
 */
class Asset : public IdentifiedObject
{

public:
	Asset();
	/**
	 * Information on acceptance test.
	 */
	AcceptanceTest acceptanceTest;
	/**
	 * Condition of asset at last baseline. Examples include new, rebuilt, overhaul
	 * required, other. Refer to inspection data for information on the most current
	 * condition of the asset.
	 */
	String baselineCondition;
	/**
	 * Percentage of initial life expectancy that has been lost as of the last life
	 * expectancy baseline. Represents
	 * (initial life expectancy - current life expectancy) / initial life expectancy.
	 */
	PerCent baselineLossOfLife;
	/**
	 * True if asset is considered critical for some reason (for example, a pole with
	 * critical attachments).
	 */
	Boolean critical;
	/**
	 * Electronic address.
	 */
	ElectronicAddress electronicAddress;
	/**
	 * In use dates for this asset.
	 */
	InUseDate inUseDate;
	/**
	 * Indication of whether asset is currently deployed (in use), ready to be put
	 * into use or not available for use.
	 */
	InUseStateKind inUseState;
	/**
	 * Kind of asset. Used in description of asset components in asset instance
	 * templates.
	 */
	AssetKind kind;
	/**
	 * <was lifecycle>
	 * Lifecycle dates for this asset.
	 */
	LifecycleDate lifecycleDate;
	/**
	 * Current lifecycle state of asset.
	 */
	AssetLifecycleStateKind lifecycleState;
	/**
	 * Lot number for this asset. Even for the same model and version number, many
	 * assets are manufactured in lots.
	 */
	String lotNumber;
	/**
	 * Position of asset or asset component. May often be in relation to other assets
	 * or components. 
	 */
	String position;
	/**
	 * Purchase price of asset.
	 */
	Money purchasePrice;
	/**
	 * Reason asset retired.
	 */
	RetiredReasonKind retiredReason;
	/**
	 * Serial number of this asset.
	 */
	String serialNumber;
	/**
	 * Status of this asset.
	 */
	Status status;
	/**
	 * Utility-specific classification of Asset and its subtypes, according to their
	 * corporate standards, practices, and existing IT systems (e.g., for management
	 * of assets, maintenance, work, outage, customers, etc.).
	 */
	String type;
	/**
	 * Uniquely tracked commodity (UTC) number.
	 */
	String utcNumber;
	ErpInventory *ErpInventory;
	/**
	 * All roles an organisation plays for this asset.
	 */
	AssetOrganisationRole *OrganisationRoles;
	AssetFunction *AssetFunction;
	/**
	 * All power system resources used to electrically model this asset. For example,
	 * transformer asset is electrically modelled with a transformer and its windings
	 * and tap changer.
	 */
	PowerSystemResource *PowerSystemResources;
	/**
	 * Container of this asset.
	 */
	AssetContainer *AssetContainer;
	AssetPropertyCurve *AssetPropertyCurves;
	ErpRecDelvLineItem *ErpRecDeliveryItems;
	/**
	 * This asset's deployment.
	 */
	AssetDeployment *AssetDeployment;
	Reconditioning *Reconditionings;
	/**
	 * Data applicable to this asset.
	 */
	AssetInfo *AssetInfo;
	Measurement *Measurements;
	/**
	 * The model of this asset.
	 */
	ProductAssetModel *ProductAssetModel;
	/**
	 * All configuration events created for this asset.
	 */
	ConfigurationEvent *ConfigurationEvents;
	/**
	 * Location of this asset.
	 */
	Location *Location;
	/**
	 * All activity records created for this asset.
	 */
	ActivityRecord *ActivityRecords;

};
#endif // !defined(EA_4AAB4750_294A_43ed_8F88_6BDC6A4F8AD9__INCLUDED_)
