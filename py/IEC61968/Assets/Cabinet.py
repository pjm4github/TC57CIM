# package IEC61968.Assets;
#
#
# /**
#  * Enclosure that offers protection to the equipment it contains and/or safety to
#  * people/animals outside it.
#  * @created 29-Dec-2023 5:23:56 PM
#  */
# public class Cabinet extends AssetContainer {
#
# 	public Cabinet(){
#
# 	}
# }//end Cabinet
#
from IEC61968.Assets.AssetContainer import AssetContainer


class Cabinet(AssetContainer):
    def __init__(self):
        super().__init__()