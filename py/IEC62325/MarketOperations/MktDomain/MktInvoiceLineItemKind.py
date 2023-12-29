# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Define the enum for kind of invoice line item
from enum import Enum


class MktInvoiceLineItemKind(Enum):
    # Enum values
    INITIAL = 1
    RECALCULATION = 2
    OTHER = 3
