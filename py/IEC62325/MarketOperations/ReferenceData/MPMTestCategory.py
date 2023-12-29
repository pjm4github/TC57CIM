# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC62325.MarketOperations.ReferenceData.MPMTestThreshold import MpmTestThreshold


class MpmTestCategory:
    """
    Provides a reference to the Market Power Mitigation test identifiers and
    methods for the results of the DA or RT markets. Specific data is the test
    identifier (Price, Conduct, or Impact) and the test method (System MPM,
    Local MPM, Alternate System MPM, or Alternate Local MPM).
    @created 28-Dec-2023 12:16:10 PM
    """

    def __init__(self) -> None:
        """
        Nature of threshold data:
        'M' - Mitigation threshold
        'R' - Reporting threshold
        """
        self.purpose_flag: PurposeFlagType = PurposeFlagType()

        """
        1 - Global Price Test
        2 - Global Conduct Test
        3 - Global Impact Test
        4 - Local Price Test
        5 - Local Conduct Test
        6 - Local Impact Test
        """
        self.test_identifier: MpmTestIdentifierType = MpmTestIdentifierType()

        """
        The method of performing the market power monitoring. Examples are Normal
        (default) thresholds or Alternate thresholds.
        """
        self.test_method: MpmTestMethodType = MpmTestMethodType()
        self.mpm_test_threshold: MpmTestThreshold = MpmTestThreshold()
        self.mpm_test_results: MpmTestResults = MpmTestResults()
        self.mpm_resource_status: MpmResourceStatus = MpmResourceStatus()

