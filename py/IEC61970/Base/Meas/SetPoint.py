from IEC61970.Base.Meas.AnalogControl import AnalogControl


class SetPoint(AnalogControl):
    """
    An analog control that issues a set point value.
    Created: 02-Jan-2024 11:25:13 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.normal_value = float()  # Normal value for Control.value, e.g., used for percentage scaling
        self.value = float()  # The value representing the actuator output
