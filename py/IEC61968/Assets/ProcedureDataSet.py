from IEC61968.Assets.Asset import Asset
from IEC61968.Common.Document import Document
from IEC61968.InfIEC61968.InfAssets.TransformerObservation import TransformerObservation
from IEC61968.Work.WorkTask import WorkTask
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Meas.MeasurementValue import MeasurementValue


class ProcedureDataSet(Document):
    """
    A data set recorded each time a procedure is executed. Observed results are
    captured in associated measurement values and/or values for properties relevant
    to the type of procedure performed.
    """

    def __init__(self):
        """
        Constructor for ProcedureDataSet.
        """
        super().__init__()
        self.completed_date_time = DateTime()
        """
        Date and time procedure was completed.
        """

        self.asset = Asset()
        """
        Asset to which this procedure data set applies.
        """

        self.measurement_value = MeasurementValue()
        """
        Measurement value associated with this procedure data set.
        """

        self.transformer_observations = TransformerObservation()
        """
        Transformer observations associated with this procedure data set.
        """

        self.work_task = WorkTask()
        """
        Work task that created this procedure data set.
        """
