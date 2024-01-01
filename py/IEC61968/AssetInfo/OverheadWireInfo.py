# package IEC61968.AssetInfo;
#
#
# /**
#  * Overhead wire data.
#  * @created 29-Dec-2023 5:38:24 PM
#  */
# public class OverheadWireInfo extends WireInfo {
#
# 	public OverheadWireInfo(){
#
# 	}
# }//end OverheadWireInfo
from IEC61968.AssetInfo.WireInfo import WireInfo


class OverheadWireInfo(WireInfo):
    def __init__(self):
        super().__init__()