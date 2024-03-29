# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# asset_kind.py

from enum import Enum


class AssetKind(Enum):
    BREAKER_AIR_BLAST_BREAKER = 1
    BREAKER_BULK_OIL_BREAKER = 2
    BREAKER_MINIMUM_OIL_BREAKER = 3
    BREAKER_SF6_DEAD_TANK_BREAKER = 4
    BREAKER_SF6_LIVE_TANK_BREAKER = 5
    BREAKER_TANK_ASSEMBLY = 6
    BREAKER_INSULATING_STACK_ASSEMBLY = 7
    TRANSFORMER = 8
    TRANSFORMER_TANK = 9
    OTHER = 10
