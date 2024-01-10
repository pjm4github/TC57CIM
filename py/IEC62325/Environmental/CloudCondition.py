# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from IEC62325.Environmental.AtmosphericPhenomenon import AtmosphericPhenomenon
from IEC62325.Environmental.EnvDomain.CloudKind import CloudKind


class CloudCondition(AtmosphericPhenomenon):
    """
    A classified cloud phenomenon with a type.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    # The type of the cloud as defined by the CloudKind enumeration.

    def __init__(self):
        super().__init__()
        self.kind = CloudKind.CIRRUS
