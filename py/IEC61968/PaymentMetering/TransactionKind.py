# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# transaction_kind.py

from enum import Enum

class TransactionKind(Enum):
    SERVICE_CHARGE_PAYMENT = 1
    TAX_CHARGE_PAYMENT = 2
    AUXILIARY_CHARGE_PAYMENT = 3
    ACCOUNT_PAYMENT = 4
    DIVERSE_PAYMENT = 5
    TRANSACTION_REVERSAL = 6
    TOKEN_SALE_PAYMENT = 7
    TOKEN_FREE_ISSUE = 8
    TOKEN_GRANT = 9
    TOKEN_EXCHANGE = 10
    TOKEN_CANCELLATION = 11
    METER_CONFIGURATION_TOKEN = 12
    OTHER = 13
