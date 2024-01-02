# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:55:16 2023
from typing import Optional

class DynamicsFunctionBlock:
    """
    Abstract parent class for all Dynamics function blocks.

    @author: ppbr003
    @version: 1.0
    @created: 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor for DynamicsFunctionBlock
        """
        self.enabled: bool = False
