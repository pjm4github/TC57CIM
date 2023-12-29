# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC62325.MarketManagement.MarketDocument import MarketDocument
from IEC62325.MarketManagement.Point import Point


# The motivation of an act.
# @author effantin-cyr
# @version 1.0
# @created 25-Dec-2023 9:21:23 PM
class Reason:

    def __init__(self):
        pass

        # The motivation of an act in coded form.
        self.code = ""

        # The textual explanation corresponding to the reason code.
        self.text = ""

        self.market_document = MarketDocument()
        self.point = Point()
