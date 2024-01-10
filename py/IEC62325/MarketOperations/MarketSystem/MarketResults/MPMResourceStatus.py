# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
class MPMResourceStatus:
    """
    Model of results of Market Power tests, gives status of resource for the
    associated interval.
    @created 28-Dec-2023 8:22:45 PM
    """

    def __init__(self) -> None:
        self.resource_status: str = "N"  # Interval Test Status, 'N' - not applicable
