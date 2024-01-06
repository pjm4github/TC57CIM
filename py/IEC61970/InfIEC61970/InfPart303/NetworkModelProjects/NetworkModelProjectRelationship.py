# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 17:13:56 2024
# A relationship that assists humans and software building cases by assembling project changes in the correct sequence.
# This class may be specialized to create specific types of relationships.
# @author 222206
# @version 1.0
# @created 25-Dec-2023 8:32:00 PM

from IEC61970.InfIEC61970.InfPart303.IdentifiedObject import IdentifiedObject

from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectComponent import \
    NetworkModelProjectComponent


class NetworkModelProjectRelationship(IdentifiedObject):
    """
    A relationship that assists humans and software building cases by assembling project changes in the correct sequence.
    This class may be specialized to create specific types of relationships.
    """

    def __init__(self):
        super().__init__()
        self.project_a = NetworkModelProjectComponent()  # Typical value used
        self.project_b = NetworkModelProjectComponent()  # Typical value used

