# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from IEC61968.Common.Document import Document


class StandardIndustryCode(Document):
    """
    The Standard Industrial Classification (SIC) are the codes that identify the
    type of products/service an industry is involved in, and used for statutory
    reporting purposes. For example, in the USA these codes are located by the 
    federal government, and then published in a book entitled "The Standard
    Industrial Classification Manual". The codes are arranged in a hierarchical
    structure.
    Note that Residential Service Agreements are not classified according to the
    SIC codes.
    @created 29-Dec-2023 9:26:01 PM
    """
    def __init__(self) -> None:
        super().__init__()
        """
        Standard alphanumeric code1 assigned to a particular product/service within
        an industry.
        """
        self.code = ""
