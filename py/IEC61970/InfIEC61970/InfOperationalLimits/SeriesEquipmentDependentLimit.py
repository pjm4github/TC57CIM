from IEC61970.InfIEC61970.InfOperationalLimits.EquipmentLimitSeriesComponent import EquipmentLimitSeriesComponent
from IEC61970.InfIEC61970.InfOperationalLimits.LimitDependency import LimitDependency


class SeriesEquipmentDependentLimit(LimitDependency):
    """
    Represents a limit based on the most restrictive series equipment limit.
    A specification of equipment that determines the calculated operational limit values based upon other equipment and their ratings.
    The most restrictive limit connected in series within the group is used.
    The physical connection based on switch status, for example, may also impact which elements in the group are considered.
    Any equipment in the group that is presently connected in series with the equipment of the directly associated operational limit is used.
    This provides a means to indicate which potentially series equipment limits are considered for a computed operational limit.
    The operational limit of the same operational limit type is assumed to be used from the grouped equipment.
    It is also possible to make assumptions or calculations regarding how flow might split if the equipment is not simply in series.
    """
    def __init__(self):
        super().__init__()
        self.equipment_limit_series_component = EquipmentLimitSeriesComponent()

