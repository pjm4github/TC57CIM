package TC57CIM.IEC61970.Base.Wires;


/**
 * A non linear shunt compensator has bank or section admittance values that
 * differs.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class NonlinearShuntCompensator extends ShuntCompensator {

	/**
	 * All points of the non-linear shunt compensator.
	 */
	public NonlinearShuntCompensatorPoint NonlinearShuntCompensatorPoints;

	public NonlinearShuntCompensator(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}