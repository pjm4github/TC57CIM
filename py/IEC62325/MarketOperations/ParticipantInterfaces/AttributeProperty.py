# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute import MktUserAttribute


class AttributeProperty:
    def __init__(self):
        self.property_nameOptional[str] = ""
        self.property_valueOptional[str] = ""
        self.sequenceOptional[str] = ""
        self.mkt_user_attributeOptional[MktUserAttribute] = MktUserAttribute()

