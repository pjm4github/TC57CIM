from IEC61968.Work.WorkAsset import WorkAsset
from IEC61970.Base.Domain.Date import Date


class Tool(WorkAsset):
    """
    Tool asset.
    @updated 02-Jan-2024 10:05:05 PM
    """

    def __init__(self):
        super().__init__()

        # (if applicable) Date the tool was last calibrated.
        self.last_calibration_date = Date()
