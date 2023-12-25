# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:03:56 2023
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ReportingGroup import ReportingGroup


class ReportingSuperGroup(IdentifiedObject):
    """
    A reporting super group, groups reporting groups for a higher level report.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:29 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.reporting_group = ReportingGroup()

