from IEC61968.Work.VehicleUsageKind import VehicleUsageKind
from IEC61968.Work.WorkAsset import WorkAsset
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Length import Length


class Vehicle(WorkAsset):
    """
    Vehicle asset.
    @created 29-Dec-2023 5:41:47 PM
    """

    def __init__(self):
        super().__init__()

        # Date and time the last odometer reading was recorded.
        self.odometer_read_date_time = DateTime()

        # Odometer reading of this vehicle as of the 'odometer_reading_date_time'. Refer to
        # associated ActivityRecords for earlier readings.
        self.odometer_reading = Length()

        # Kind of usage of the vehicle.
        self.usage_kind = VehicleUsageKind.CREW
