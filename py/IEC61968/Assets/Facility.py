from IEC61968.Assets.AssetContainer import AssetContainer


class Facility(AssetContainer):
    #  * A facility may contain buildings, storage facilities, switching facilities,
    #  * power generation, manufacturing facilities, maintenance facilities, etc.
    def __init__(self):
        super().__init__()
        self.kind = ""  # Kind of this facility.
