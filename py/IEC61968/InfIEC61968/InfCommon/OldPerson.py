# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfCommon.PersonOrganisationRole import PersonOrganisationRole
from IEC61968.InfIEC61968.InfCommon.PersonPropertyRole import PersonPropertyRole
from IEC61968.InfIEC61968.InfCommon.Skill import Skill
from IEC61968.InfIEC61968.InfERPSupport.ErpCompetency import ErpCompetency
from IEC61968.InfIEC61968.InfERPSupport.ErpPersonnel import ErpPersonnel
from IEC61968.InfIEC61968.InfWork.LaborItem import LaborItem
from IEC61970.Base.Meas.MeasurementValue import MeasurementValue


class OldPerson:
    """
    General purpose information for name and other information to contact people.
    """

    def __init__(self) -> None:
        self.status: Status = Status()
        """
        Utility-specific classification for this person, according to the utility's
        corporate standards and practices. Examples include employee, contractor,
        agent, not affiliated, etc.
        Note that this field is not used to indicate whether this person is a customer
        of the utility. Often an employee or contractor is also a customer. Customer
        information is gained with relationship to Organisation and CustomerData. In
        similar fashion, this field does not indicate the various roles this person
        may fill as part of utility operations.
        """
        self.type: str
        self.measurement_values: MeasurementValue = MeasurementValue()
        self.erp_competency: ErpCompetency = ErpCompetency()
        self.labor_items: LaborItem = LaborItem()
        self.erp_personnel: ErpPersonnel = ErpPersonnel()
        self.skills: Skill = Skill()
        self.organisation_roles: PersonOrganisationRole = PersonOrganisationRole()
        self.land_property_roles: PersonPropertyRole = PersonPropertyRole()
