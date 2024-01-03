# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from datetime import datetime
from work_document import WorkDocument

class Assignment(WorkDocument):
    """
    An assignment is given to an ErpPerson, Crew, Organisation, Equipment
    Item, Tool, etc. and may be used to perform Work, WorkTasks, Procedures, 
    etc. TimeSchedules may be set up directly for Assignments or indirectly 
    via the associated WorkTask. Note that these associations are all inherited 
    through the recursive relationship on Document.
    @created 29-Dec-2023 9:10:57 PM
    """

    def __init__(self) -> None:
        super().__init__()
        """
        Period between the assignment becoming effective and its expiration.
        """
        self.effective_period: DateTimeInterval
