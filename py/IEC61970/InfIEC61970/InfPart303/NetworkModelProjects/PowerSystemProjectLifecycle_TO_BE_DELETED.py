# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 17:13:56 2024
from IEC61970.Base.Domain.Date import Date


class PowerSystemProjectLifecycleToBeDeleted:
    """
    Represent the base lifecycle of a functional model change that could be a
    construction of new elements.
    @author: sveinols
    @version: 1.0
    @created: 25-Dec-2023 8:32:02 PM
    """

    def __init__(self):
        super().__init__()
        # The date the Power System Project is in cancelled stage.
        self.cancelled = Date()  # typical value can be passed as an argument here

        # The date Power System Project is in committed stage.
        self.committed = Date()  # typical value can be passed as an argument here

        # The date Power System Project is in build stage.
        self.in_build = Date()  # typical value can be passed as an argument here

        # The date Power System Project is in planning stage.
        self.in_plan = Date()  # typical value can be passed as an argument here
