# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.ActivityRecord import ActivityRecord
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC62325.Environmental.AlertTypeList import AlertTypeList
from IEC62325.Environmental.EnvironmentalDataProvider import EnvironmentalDataProvider
from IEC62325.Environmental.EnvironmentalLocationType import EnvironmentalLocationType


class EnvironmentalAlert(ActivityRecord):
    """
    An environmental alert issued by a provider or system.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

        # The type of the issued alert which is drawn from the specified alert type list.
        self.alert_type = ""

        # Time and date alert cancelled. Used only if alert is cancelled before it expires.
        self.cancelled_date_time = DateTime()

        # An abbreviated textual description of the alert issued.
        # Note: the full text of the alert appears in the .description attribute
        # (inherited from IdentifiedObject).
        self.headline = ""

        # The interval for which this weather alert is in effect.
        self.in_effect = DateTimeInterval()

        # Environmental data provider for this alert.
        self.environmental_data_provider = EnvironmentalDataProvider()

        # The list of alert types from which the type of this alert is drawn.
        self.alert_type_list = AlertTypeList()

        # Type of location to which this environmental alert applies.
        self.environmental_location_kind = EnvironmentalLocationType()
