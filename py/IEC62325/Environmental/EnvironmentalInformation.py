# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.Environmental.EnvironmentalDataProvider import EnvironmentalDataProvider


class EnvironmentalInformation(IdentifiedObject):
    """
    Abstract class (with concrete child classes of Observation and Forecast) that
    groups phenomenon and/or environmental value sets.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        The timestamp of when the forecast was created
        """
        super().__init__()
        self.created = DateTime()

        # Environmental data provider supplying this environmental information.
        self.environmental_data_provider = EnvironmentalDataProvider()
