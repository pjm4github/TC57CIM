# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023

class LoadDistributionFactor:
    """
    This class models the load distribution factors. This class should be used in
    one of two ways:
    *
    Use it along with the AggregatedPnode and the IndividualPnode to show the
    distriubtion of each individual party
    *
    OR
    *
    Use it with Mkt_EnergyConsumer to represent the current MW/Mvar distribution
    within it's parnet load group.
    @created 27-Dec-2023 3:29:42 PM
    """

    def __init__(self) -> None:
        pass
        self.p_dist_factor: float = 0.0  # Real power (MW) load distribution factor
        self.q_dist_factor: float = 0.0  # Reactive power (MVAr) load distribution factor
