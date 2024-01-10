# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:37:42 2023
from enum import Enum


class LandPropertyKind(Enum):
    """
    Kind of (land) property.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:08:12 PM
    """

    # Site enclosed within a building.
    BUILDING = 1

    # Site with a customer.
    CUSTOMER_PREMISE = 2

    # Storehouse for supplies that also serves as a station for supporting crews.
    DEPOT = 3

    # Place of storage (e.g., a warehouse) to put aside, or accumulate, material and equipment for use when needed.
    STORE = 4

    # Transmission network switchyard.
    SUBSTATION = 5

    # Substation where the distribution and transmission networks meet and hence have mixed ownership and mixed operational control.
    GRID_SUPPLY_POINT = 6

    # Property owned or used by an external party that is not a customer.
    EXTERNAL = 7
