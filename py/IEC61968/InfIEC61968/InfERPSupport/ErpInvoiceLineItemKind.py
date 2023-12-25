# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# erp_invoice_line_item_kind.py
from enum import Enum


class ErpInvoiceLineItemKind(Enum):
    INITIAL = 1
    RECALCULATION = 2
    OTHER = 3
