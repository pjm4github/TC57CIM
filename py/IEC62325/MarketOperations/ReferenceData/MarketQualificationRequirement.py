# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Domain.DateTime import DateTime


class MarketQualificationRequirement:
    '''
    Certain skills are required and shall be certified in order for a person
    (typically a member of a crew) to be qualified to work on types of equipment.
    @created 28-Dec-2023 12:17:20 PM
    '''

    def __init__(self) -> None:
        '''
        Effective date of the privilege, terminate date of the privilege, or effective
        date of the application for the organization
        '''
        self.effective_date: DateTime = DateTime()
        '''
        This is the terminate date of the application for the organization.
        The specific organization can no longer access the application as of the
        terminate date.
        '''
        self.expiration_date: DateTime = DateTime()
        '''
        Qualification identifier.
        '''
        self.qualification_id: str = ""
        '''
        The status of the privilege. Shows the status of the user's qualification.
        The current statuses are: 1=New, 2=Active, 3=Refused, 4=Terminated,
        5=Withdrawn and it is subject to update.
        '''
        self.status: int = 0
        '''
        This is the name of the status of the qualification and is used to display the
        status of the user's or organization's status.
        '''
        self.status_type: str = ""
