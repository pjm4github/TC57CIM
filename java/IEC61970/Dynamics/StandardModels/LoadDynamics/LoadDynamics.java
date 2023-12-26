package IEC61970.Dynamics.StandardModels.LoadDynamics;

import IEC61970.Base.Wires.EnergyConsumer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Load whose behaviour is described by reference to a standard model <font
 * color="#0f0f0f">or by definition of a user-defined model.</font>
 * 
 * A standard feature of dynamic load behaviour modelling is the ability to
 * associate the same behaviour to multiple energy consumers by means of a single
 * aggregate load definition.  Aggregate loads are used to represent all or part
 * of the real and reactive load from one or more loads in the static (power flow)
 * data. This load is usually the aggregation of many individual load devices and
 * the load model is approximate representation of the aggregate response of the
 * load devices to system disturbances. The load model is always applied to
 * individual bus loads (energy consumers) but a single set of load model
 * parameters can used for all loads in the grouping.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class LoadDynamics extends IdentifiedObject {

	/**
	 * Energy consumer to which this dynamics load model applies.
	 */
	public EnergyConsumer EnergyConsumer;

	public LoadDynamics(){

	}
}//end LoadDynamics