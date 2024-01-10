# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023


class MPMTestResults:
    """
    Provides the outcome and margin percent (as appropriate) result data for the
    MPM tests. There are relationships to Zone for Designated Congestion Area
    Tests, CurveSchedData for bid segment tests, to the SubControlArea for the
    system wide level tests, and Pnodes for the LMPM impact tests.

    @created 28-Dec-2023 8:22:54 PM
    """

    def __init__(self) -> None:
        """
        Constructor for MPM Test Results
        """
        self.margin_percent: float = 0.0  # Used to show the Margin % result of the Impact test
        self.outcome: str = "NA"  # The results of the test. For the Price, Impact, and Conduct tests, typical values are NA, Pass, Fail, Disable, or Skip
