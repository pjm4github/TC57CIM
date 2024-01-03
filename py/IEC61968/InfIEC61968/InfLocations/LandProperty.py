# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:37:42 2023
from typing import Optional

from IEC61968.Assets.AssetContainer import AssetContainer
from IEC61968.Common.Location import Location
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfCommon.PersonPropertyRole import PersonPropertyRole
from IEC61968.InfIEC61968.InfCommon.PropertyOrganisationRole import PropertyOrganisationRole
from IEC61968.InfIEC61968.InfERPSupport.ErpSiteLevelData import ErpSiteLevelData
from IEC61968.InfIEC61968.InfLocations.DemographicKind import DemographicKind
from IEC61968.InfIEC61968.InfLocations.LandPropertyKind import LandPropertyKind
from IEC61968.InfIEC61968.InfLocations.LocationGrant import LocationGrant
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class LandProperty(IdentifiedObject):
    """
    Information about a particular piece of (land) property such as its use.
    Ownership of the property may be determined through associations to
    Organisations and/or ErpPersons.
    @created 29-Dec-2023 6:06:23 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.demographic_kind: Optional[DemographicKind] = DemographicKind.RURAL  # Demographics around the site.
        self.external_record_reference: Optional[str] = ""  # Reference allocated by the governing organisation (such as municipality) to
        # this piece of land that has a formal reference to Surveyor General's records.
        # The governing organisation is specified in associated Organisation.
        self.kind: Optional[LandPropertyKind] = LandPropertyKind.DEPOT  # Kind of (land) property, categorized according to its main functional use from
        # the utility's perspective.
        self.status: Optional[Status] = Status()
        self.location_grants: Optional[LocationGrant] = LocationGrant()  # All location grants this land property has.
        self.erp_site_level_datas: Optional[ErpSiteLevelData] = ErpSiteLevelData()
        self.erp_organisation_roles: Optional[PropertyOrganisationRole] = PropertyOrganisationRole()
        self.erp_person_roles: Optional[PersonPropertyRole] = PersonPropertyRole()
        self.asset_containers: Optional[AssetContainer] = AssetContainer()
        self.locations: Optional[Location] = Location()  # The spatial description of a piece of property.
