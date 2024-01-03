from IEC61968.Assets.ProcedureDataSet import ProcedureDataSet
from IEC61970.Base.Core.PhaseCode import PhaseCode
from IEC61970.Base.Domain.DateTime import DateTime


class DiagnosisDataSet(ProcedureDataSet):
    # The result of a problem (typically an asset failure) diagnosis. Contains
    # complete information like what might be received from a lab doing forensic
    # analysis of a failed asset.
    # @created 29-Dec-2023 5:26:27 PM
    def __init__(self):
        super().__init__()
        self.effect = ""  # Effect of problem.
        self.failure_mode = ""  # Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to
        # contain oil; Failure to provide ground plane; Other.
        self.final_cause = ""  # Cause of problem determined during diagnosis.
        self.final_code = ""  # Code for diagnosed probem type.
        self.final_origin = ""  # Origin of problem determined during diagnosis.
        self.final_remark = ""  # Remarks pertaining to findings during problem diagnosis.
        self.phase_code = PhaseCode()  # Phase(s) diagnosed.
        self.preliminary_code = ""  # Code for problem type determined during preliminary assessment.
        self.preliminary_date_time = DateTime()  # Date and time preliminary assessment of problem was performed.
        self.preliminary_remark = ""  # Remarks pertaining to preliminary assessment of problem.
        self.root_cause = ""  # Root cause of problem determined during diagnosis.
        self.root_origin = ""  # Root origin of problem determined during diagnosis.
        self.root_remark = ""  # Remarks pertaining to root cause findings during problem diagnosis.
