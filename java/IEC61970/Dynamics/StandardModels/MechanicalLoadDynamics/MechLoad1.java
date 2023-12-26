package IEC61970.Dynamics.StandardModels.MechanicalLoadDynamics;

import IEC61970.Base.Domain.Float;

/**
 * Mechanical load model type 1.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MechLoad1 extends MechanicalLoadDynamics {

	/**
	 * Speed squared coefficient (a).
	 */
	public Float a;
	/**
	 * Speed coefficient (b).
	 */
	public Float b;
	/**
	 * Speed to the exponent coefficient (d).
	 */
	public Float d;
	/**
	 * Exponent (e).
	 */
	public Float e;

	public MechLoad1(){

	}
}//end MechLoad1