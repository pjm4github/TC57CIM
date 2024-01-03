package IEC61970.Base.LoadModel;


/**
 * The class is the root or first level in a hierarchical structure for grouping
 * of loads for the purpose of load flow load scaling.
 * @created 02-Jan-2024 11:12:26 PM
 */
public class LoadArea extends EnergyArea {

	/**
	 * The SubLoadAreas in the LoadArea.
	 */
	public SubLoadArea SubLoadAreas;

	public LoadArea(){

	}
}//end LoadArea