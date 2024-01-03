package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Boolean;
import IEC61968.Common.ElectronicAddress;
import IEC61970.Base.Domain.Money;
import IEC61968.Common.Status;
import IEC61970.Base.Core.PowerSystemResource;
import IEC61968.InfIEC61968.InfAssets.AssetPropertyCurve;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.InfIEC61968.InfAssets.Reconditioning;
import IEC61970.Base.Meas.Measurement;
import IEC61968.Common.ConfigurationEvent;
import IEC61968.Common.Location;
import IEC61968.Common.ActivityRecord;

/**
 * Tangible resource of the utility, including power system equipment, various end
 * devices, cabinets, buildings, etc. For electrical network equipment, the role
 * of the asset is defined through PowerSystemResource and its subclasses, defined
 * mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::
 * Wires). Asset description places emphasis on the physical characteristics of
 * the equipment fulfilling that role.
 * @created 03-Jan-2024 11:59:41 AM
 */
public class Asset extends IdentifiedObject {

	/**
	 * Information on acceptance test.
	 */
	public AcceptanceTest acceptanceTest;
	/**
	 * Condition of asset at last baseline. Examples include new, rebuilt, overhaul
	 * required, other. Refer to inspection data for information on the most current
	 * condition of the asset.
	 */
	public String baselineCondition;
	/**
	 * Percentage of initial life expectancy that has been lost as of the last life
	 * expectancy baseline. Represents
	 * (initial life expectancy - current life expectancy) / initial life expectancy.
	 */
	public PerCent baselineLossOfLife;
	/**
	 * True if asset is considered critical for some reason (for example, a pole with
	 * critical attachments).
	 */
	public Boolean critical;
	/**
	 * Electronic address.
	 */
	public ElectronicAddress electronicAddress;
	/**
	 * In use dates for this asset.
	 */
	public InUseDate inUseDate;
	/**
	 * Indication of whether asset is currently deployed (in use), ready to be put
	 * into use or not available for use.
	 */
	public InUseStateKind inUseState;
	/**
	 * Kind of asset. Used in description of asset components in asset instance
	 * templates.
	 */
	public AssetKind kind;
	/**
	 * <was lifecycle>
	 * Lifecycle dates for this asset.
	 */
	public LifecycleDate lifecycleDate;
	/**
	 * Current lifecycle state of asset.
	 */
	public AssetLifecycleStateKind lifecycleState;
	/**
	 * Lot number for this asset. Even for the same model and version number, many
	 * assets are manufactured in lots.
	 */
	public String lotNumber;
	/**
	 * Position of asset or asset component. May often be in relation to other assets
	 * or components. 
	 */
	public String position;
	/**
	 * Purchase price of asset.
	 */
	public Money purchasePrice;
	/**
	 * Reason asset retired.
	 */
	public RetiredReasonKind retiredReason;
	/**
	 * Serial number of this asset.
	 */
	public String serialNumber;
	/**
	 * Status of this asset.
	 */
	public Status status;
	/**
	 * Utility-specific classification of Asset and its subtypes, according to their
	 * corporate standards, practices, and existing IT systems (e.g., for management
	 * of assets, maintenance, work, outage, customers, etc.).
	 */
	public String type;
	/**
	 * Uniquely tracked commodity (UTC) number.
	 */
	public String utcNumber;
	public ErpInventory ErpInventory;
	/**
	 * All roles an organisation plays for this asset.
	 */
	public AssetOrganisationRole OrganisationRoles;
	public AssetFunction AssetFunction;
	/**
	 * All power system resources used to electrically model this asset. For example,
	 * transformer asset is electrically modelled with a transformer and its windings
	 * and tap changer.
	 */
	public PowerSystemResource PowerSystemResources;
	/**
	 * Container of this asset.
	 */
	public AssetContainer AssetContainer;
	public AssetPropertyCurve AssetPropertyCurves;
	public ErpRecDelvLineItem ErpRecDeliveryItems;
	/**
	 * This asset's deployment.
	 */
	public AssetDeployment AssetDeployment;
	public Reconditioning Reconditionings;
	/**
	 * Data applicable to this asset.
	 */
	public AssetInfo AssetInfo;
	public Measurement Measurements;
	/**
	 * The model of this asset.
	 */
	public ProductAssetModel ProductAssetModel;
	/**
	 * All configuration events created for this asset.
	 */
	public ConfigurationEvent ConfigurationEvents;
	/**
	 * Location of this asset.
	 */
	public Location Location;
	/**
	 * All activity records created for this asset.
	 */
	public ActivityRecord ActivityRecords;

	public Asset(){

	}
}//end Asset