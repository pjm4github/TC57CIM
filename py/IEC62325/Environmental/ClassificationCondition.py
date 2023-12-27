# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Seconds import Seconds
from IEC62325.Environmental.EnvDomain.TestKind import TestKind
from IEC62325.Environmental.PhenomenonClassification import PhenomenonClassification


class ClassificationCondition(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.duration = Seconds()
        self.test = TestKind.GREATER_THAN
        self.phenomenon_classification = PhenomenonClassification()
