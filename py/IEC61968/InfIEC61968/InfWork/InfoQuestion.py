# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61970.Base.Domain.DateTime import DateTime


class InfoQuestion(WorkDocument):
    """
    Questions and answers associated with a type of document for purposes of
    clarification. Questions may be predefined or ad hoc.
    @created 29-Dec-2023 9:16:16 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.answer: Optional[str] = ""  # Answer to question.
        self.answer_date_time: Optional[DateTime] = DateTime()  # The date and time the quesiton was answered.
        self.answer_remark: Optional[str] = ""  # Remarks to qualify the answer.
        self.question_code: Optional[str] = ""  # The question code. If blank, refer to questionText.
        self.question_remark: Optional[str] = ""  # Remarks to qualify the question in this situation.
        self.question_text: Optional[str] = ""  # For non-coded questions, the question is provided here.
        self.question_type: Optional[str] = ""  # The type of the question.