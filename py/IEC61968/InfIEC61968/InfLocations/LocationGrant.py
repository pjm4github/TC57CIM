# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:37:42 2023
from IEC61968.Common.Agreement import Agreement


class LocationGrant(Agreement):
    """
    A grant provides a right, as defined by type, for a parcel of land. Note that
    the association to Location, Asset, Organisation, etc. for the Grant is
    inherited from Agreement, a type of Document.
    @created 29-Dec-2023 6:06:41 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.property_data = ""
        # 	 * Property related information that describes the Grant's land parcel. For
        # 	 * example, it may be a deed book number, deed book page number, and parcel number.
