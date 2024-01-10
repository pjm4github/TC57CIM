# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money


class ShutdownCurve(Curve):
    # Relationship between the rate in gross active power/minute (Y-axis) at which a
    # unit should be shutdown and its present gross MW output (X-axis).
    # @created 02-Jan-2024 10:57:43 PM
    def __init__(self):
        super().__init__()

        # Fixed shutdown cost.
        self.shutdown_cost = Money()  # Typical value as argument to Money class method call

        # The date and time of the most recent generating unit shutdown.
        self.shutdown_date = DateTime()  # Typical value as argument to DateTime class method call
