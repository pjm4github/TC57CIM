package IEC61970.InfIEC61970.InfOperationalLimits;


/**
 * Limit based on most restrictive series equipment limit.
 * A specification of  of equipment that determines the calculated operational
 * limit values based upon other equipment and their ratings.  The most
 * restrictive limit connected in series within the group is used.   The physical
 * connection based on switch status for example may also impact which elements in
 * the group are considered. Any equipment in the group that are presently
 * connected in series with the equipment of the directly associated operational
 * limit are used.   This provides a means to indicate which potentially series
 * equipment limits are considered for a computed operational limit. The
 * operational limit of the same operational limit type is assumed to be used from
 * the grouped equipment.   It is also possible to make assumptions or
 * calculations regarding how flow might split if the equipment is not simply in
 * series.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class SeriesEquipmentDependentLimit extends LimitDependency {

	/**
	 * Equipment linkages that participates in the limit calculation.
	 */
	public EquipmentLimitSeriesComponent EquipmentLimitSeriesComponent;

	public SeriesEquipmentDependentLimit(){

	}
}//end SeriesEquipmentDependentLimit