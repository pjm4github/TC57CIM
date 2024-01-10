# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106


class CombinedCycleTransitionState:
    """
    Defines the available from and to Transition States for the Combine Cycle
    Configurations.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        Flag indicating whether this is an 'UP' transition.
        If not, it is a 'DOWN' transition.
        """
        self.up_transition = False

