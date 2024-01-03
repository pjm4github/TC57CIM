from IEC61968.Assets.ProcedureDataSet import ProcedureDataSet
from IEC61970.Base.Domain.DateTime import DateTime


class TestDataSet(ProcedureDataSet):
    """
    Test results, usually obtained by a lab or other independent organisation.
    @created 29-Dec-2023 5:23:27 PM
    """
    def __init__(self):
        super().__init__()
        self.conclusion = ""  # Conclusion drawn from test results
        self.specimen_id = ""  # Identifier of specimen used in inspection or test
        self.specimen_to_lab_date_time = DateTime()  # Date and time the specimen was received by the lab
