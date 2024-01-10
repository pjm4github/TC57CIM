from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime


class MeasValueConfiguration(IdentifiedObject):
    """
    Author: selaost1
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.read_all_values = bool()  # Indicates whether all values should be read
        self.sample_time = DateTime()  # The time at which the sample is taken
        self.meas_value_set = None  # Placeholder for associated MeasValueSet
        # Assuming MeasValueSet is a previously defined class
        # If MeasValueSet is not defined, this will raise an error and needs to be implemented
