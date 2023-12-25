package TC57CIM.IEC61970.Base.Wires;


/**
 * A per phase non linear shunt compensator has bank or section admittance values
 * that differs.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class NonlinearShuntCompensatorPhase extends ShuntCompensatorPhase {

	/**
	 * All points of the non-linear shunt compensator phase.
	 */
	public NonlinearShuntCompensatorPhasePoint NonlinearShuntCompensatorPhasePoints;

	public NonlinearShuntCompensatorPhase(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}