
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.OperationalLimits.OperationalLimitType import OperationalLimitType
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.InfIEC61970.InfOperationalLimits.LimitDependency import LimitDependency


class OperationalLimit(IdentifiedObject):
    """
    A value associated with a specific kind of limit.
    The sub class value attribute shall be positive.
    The sub class value attribute is inversely proportional to OperationalLimitType.
    AcceptableDuration (acceptableDuration for short). A pair of value_x and
    acceptableDuration_x are related to each other as follows:
    if value_1 > value_2 > value_3 >... then
    acceptableDuration_1 < acceptableDuration_2 < acceptableDuration_3 < ...
    A value_x with direction="high" shall be greater than a value_y with
    direction="low".
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """

    def __init__(self):
        super().__init__()
        self.operational_limit_type: OperationalLimitType = OperationalLimitType()
        self.limit_dependency_model: LimitDependency = LimitDependency()

