package IEC61970.Base.Generation.Production;


/**
 * A wind driven generating unit, connected to the grid by means of a rotating
 * machine.  May be used to represent a single turbine or an aggregation.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindGeneratingUnit extends GeneratingUnit {

	/**
	 * The kind of wind generating unit
	 */
	public WindGenUnitKind windGenUnitType;

	public WindGeneratingUnit(){

	}
}//end WindGeneratingUnit