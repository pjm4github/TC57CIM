# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 17:13:56 2024
# Class to represent AnnotatedProjectDependency
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.DependencyType import DependencyType
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProjectStage import NetworkModelProjectStage


class AnnotatedProjectDependency(IdentifiedObject):
    # constructor
    def __init__(self):
        super().__init__()
        self.dependency_type = DependencyType.REQUIRED  # Typical value for dependency type
        self.dependent_on_stage = NetworkModelProjectStage()  # Typical value for dependent on stage
        self.depending_stage = NetworkModelProjectStage()  # Typical value for depending stage
