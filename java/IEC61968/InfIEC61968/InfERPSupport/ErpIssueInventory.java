import IEC61968.Common.Status;
import IEC61968.InfIEC61968.InfWork.TypeMaterial;
import IEC61968.Assets.CatalogAssetType;

/**
 * Can be used to request an application to process an issue or request
 * information about an issue.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpIssueInventory extends ErpIdentifiedObject {

	public Status status;
	public TypeMaterial TypeMaterial;
	public CatalogAssetType TypeAsset;

	public ErpIssueInventory(){

	}
}//end ErpIssueInventory