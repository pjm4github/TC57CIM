# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.ParticipantInterfaces.LoadBid import LoadBid


class RegisteredLoad(RegisteredResource):
    """
    Model of a load that is registered to participate in the market.

    RegisteredLoad is used to model any load that is served by the wholesale market
    directly. RegisteredLoads may be dispatchable or non-dispatchable and may or
    may not have bid curves. Examples of RegisteredLoads would include:
    distribution company load, energy retailer load, large bulk power system
    connected facility load.

    Loads that are served indirectly, for example - through an energy retailer or a
    vertical utility, should be modeled as RegisteredDistributedResources. Examples
    of RegisteredDistributedResources would include: distribution level storage,
    distribution level generation and distribution level demand response.
    """

    def __init__(self):
        super().__init__()
        self.block_load_transferOptional[bool] = False  # Flag to indicate that the Resource is Block
        # Load pseudo resource.
        self.dynamically_scheduled_load_resourceOptional[
            bool] = False  # Flag to indicate that a Load Resource is part of a DSR Load
        self.dynamically_scheduled_qualificationOptional[bool] = False  # Qualification status
        # (used for DSR qualification)
        self.load_bidsOptional[LoadBid] = LoadBid()

