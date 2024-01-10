# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional


class SubstitutionResourceList:
    """
    List of resources that can be substituted for within the bounds of a Contract
    definition. This class has a precedence and a resource.
    @created 28-Dec-2023 12:24:04 PM
    """

    def __init__(self) -> None:
        """
        An indicator of the order a resource should be substituted. The lower the
        number the higher the precedence.
        """
        self.precedence: Optional[int] = 0
