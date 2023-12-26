package IEC61970.Base.Topology;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.ReportingGroup;
import IEC61970.Base.Core.ACDCTerminal;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Used to apply user standard names to topology buses. Typically used for
 * "bus/branch" case generation. Associated with one or more terminals that are
 * normally connected with the bus name.    The associated terminals are normally
 * connected by non-retained switches. For a ring bus station configuration, all
 * busbar terminals in the ring are typically associated.   For a breaker and a
 * half scheme, both busbars would normally be associated.  For a ring bus, all
 * busbars would normally be associated.  For a "straight" busbar configuration,
 * normally only the main terminal at the busbar would be associated.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class BusNameMarker extends IdentifiedObject {

	/**
	 * Priority of bus name marker for use as topology bus name.  Use 0 for don t care.
	 *  Use 1 for highest priority.  Use 2 as priority is less than 1 and so on.
	 */
	public Integer priority;
	/**
	 * The reporting group to which this bus name marker belongs.
	 */
	public ReportingGroup ReportingGroup;
	/**
	 * The terminals associated with this bus name marker.
	 */
	public ACDCTerminal Terminal;
	/**
	 * A user defined topological node that was originally defined in a planning model
	 * not yet having topology described by ConnectivityNodes. Once ConnectivityNodes
	 * has been created they may linked to user defined ToplogicalNdes using
	 * BusNameMarkers.
	 */
	public TopologicalNode TopologicalNode;

	public BusNameMarker(){

	}
}//end BusNameMarker