package IEC61968.InfIEC61968.InfLocations;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Status;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.InfIEC61968.InfCommon.PropertyOrganisationRole;
import IEC61968.InfIEC61968.InfCommon.PersonPropertyRole;
import IEC61968.Assets.AssetContainer;
import IEC61968.Common.Location;

/**
 * Information about a particular piece of (land) property such as its use.
 * Ownership of the property may be determined through associations to
 * Organisations and/or ErpPersons.
 * @created 03-Jan-2024 12:48:06 PM
 */
public class LandProperty extends IdentifiedObject {

	/**
	 * Demographics around the site.
	 */
	public DemographicKind demographicKind;
	/**
	 * Reference allocated by the governing organisation (such as municipality) to
	 * this piece of land that has a formal reference to Surveyor General's records.
	 * The governing organisation is specified in associated Organisation.
	 */
	public String externalRecordReference;
	/**
	 * Kind of (land) property, categorised according to its main functional use from
	 * the utility's perspective.
	 */
	public LandPropertyKind kind;
	public Status status;
	/**
	 * All location grants this land property has.
	 */
	public LocationGrant LocationGrants;
	public ErpSiteLevelData ErpSiteLevelDatas;
	public PropertyOrganisationRole ErpOrganisationRoles;
	public PersonPropertyRole ErpPersonRoles;
	public AssetContainer AssetContainers;
	/**
	 * The spatail description of a piece of property.
	 */
	public Location Locations;

	public LandProperty(){

	}
}//end LandProperty