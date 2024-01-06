from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Profile(IdentifiedObject):
    """
    Describes the existence of a profile. The MRID is usually defined as a static
    value by the document or artifact that defines the contents of the profile and
    the rules for using the profile.
    Author: SELAOST1
    Version: 1.0
    Created: 22-Dec-2023 4:59:45 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        # No additional attributes are defined in the provided Java class
