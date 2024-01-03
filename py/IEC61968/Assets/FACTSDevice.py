from IEC61968.Assets.Asset import Asset
from IEC61968.InfIEC61968.InfAssets.FACTSDeviceKind import FACTSDeviceKind


class FACTSDevice(Asset):
    #  * FACTS device asset.
    #  * @created 29-Dec-2023 5:25:07 PM
    def __init__(self):
        super().__init__()
        self.kind = FACTSDeviceKind.SVC  # 	 * Kind of FACTS device.