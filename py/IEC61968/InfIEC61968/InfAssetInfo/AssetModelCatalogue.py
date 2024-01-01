# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class AssetModelCatalogue(IdentifiedObject):

    """
    Catalogue of available types of products and materials that are used to build
    or install, maintain or operate an Asset. Each catalogue item is for a specific
    product (AssetModel) available from a specific supplier.
    @created 29-Dec-2023 6:22:31 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.status: Status = Status()



