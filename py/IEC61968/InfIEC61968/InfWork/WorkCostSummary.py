# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument


class WorkCostSummary(WorkDocument):
    """
    A roll up by cost type for the entire cost of a work order. For example, total labor.
    @created 29-Dec-2023 9:19:48 PM
    """

    def __init__(self) -> None:
        super().__init__()