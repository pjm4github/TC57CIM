from IEC61968.Assets.Asset import Asset
from IEC61968.Assets.ProcedureDataSet import ProcedureDataSet
from IEC61968.Assets.ProcedureKind import ProcedureKind
from IEC61968.Common.Document import Document
from IEC61970.Base.Meas.Limit import Limit
from IEC61970.Base.Meas.Measurement import Measurement


class Procedure(Document):
    """
    Documented procedure for various types of work or work tasks on assets.
    @created 29-Dec-2023 5:28:01 PM
    """
    def __init__(self):
        super().__init__()
        self.instruction = ""  # Textual description of this procedure
        self.kind = ProcedureKind.DIAGNOSIS  # Kind of procedure
        self.sequence_number = ""  # Sequence number in a sequence of procedures being performed
        self.measurements = Measurement()  # Document containing this measurement
        self.limits = Limit()
        self.assets = Asset()  # All assets to which this procedure applies
        self.procedure_data_sets = ProcedureDataSet()  # All data sets captured by this procedure
