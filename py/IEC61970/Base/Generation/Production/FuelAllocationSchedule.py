# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
# The amount of fuel of a given type which is allocated for consumption over a specified period of time.
# @created 02-Jan-2024 10:53:25 PM
from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Generation.Production.FuelType import FuelType


class FuelAllocationSchedule(Curve):

    def __init__(self):
        super().__init__()

        # The end time and date of the fuel allocation schedule.
        self.fuel_allocation_end_date = DateTime()  # Typical value: DateTime.now()

        # The start time and date of the fuel allocation schedule.
        self.fuel_allocation_start_date = DateTime()  # Typical value: DateTime.now()

        # The type of fuel, which also indicates the corresponding measurement unit.
        self.fuel_type = FuelType.GASOLINE  # Typical value: FuelType.GASOLINE

        # The maximum amount fuel that is allocated for consumption for the scheduled time period.
        self.max_fuel_allocation = 0.0  # Typical value: 0.0

        # The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a
        # "take-or-pay" contract.
        self.min_fuel_allocation = 0.0  # Typical value: 0.0
