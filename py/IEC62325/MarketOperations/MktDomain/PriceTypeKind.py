# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import StrEnum


class PriceTypeKind(StrEnum):
    """
    Value of this enumeration for different prices include "total" for the
    complete/full/all-in price, "congestion" for the congestion cost associated
    with the total price, the "loss" for the loss price associated with the
    total price, "capacity" for prices related to installed or reserved capacity,
    "mileage" for use-based accounting, "system"
    for system-wide/copper-plate prices, and "delivery" for distribution-based
    prices.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """
    CAPACITY = "capacity"
    CONGESTION = "congestion"
    DELIVERY = "delivery"
    LOSS = "loss"
    MILEAGE = "mileage"
    SYSTEM = "system"
    TOTAL = "total"
