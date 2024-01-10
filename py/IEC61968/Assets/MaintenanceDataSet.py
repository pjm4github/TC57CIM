from IEC61968.Assets.ProcedureDataSet import ProcedureDataSet


class MaintenanceDataSet(ProcedureDataSet):
    """
    The result of a maintenance activity, a type of Procedure, for a given
    attribute of an asset.
    @created 29-Dec-2023 5:22:23 PM
    """
    def __init__(self):
        super().__init__()
        self.condition_after = ""  # Condition of asset just following maintenance procedure
        self.condition_before = ""  # Description of the condition of the asset just prior to maintenance being performed
        self.maint_code = ""  # Code for the type of maintenance performed

