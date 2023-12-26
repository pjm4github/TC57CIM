package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Power sensitive stabilizer model.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssSB4 extends PowerSystemStabilizerDynamics {

	/**
	 * Gain (Kx).
	 */
	public PU kx;
	/**
	 * Time constant (Ta).
	 */
	public Seconds ta;
	/**
	 * Time constant (Tb).
	 */
	public Seconds tb;
	/**
	 * Time constant (Tc).
	 */
	public Seconds tc;
	/**
	 * Time constant (Td).
	 */
	public Seconds td;
	/**
	 * Time constant (Te).
	 */
	public Seconds te;
	/**
	 * Time constant (Tt).
	 */
	public Seconds tt;
	/**
	 * Reset time constant (Tx1).
	 */
	public Seconds tx1;
	/**
	 * Time constant (Tx2).
	 */
	public Seconds tx2;
	/**
	 * Limiter (Vsmax).
	 */
	public PU vsmax;
	/**
	 * Limiter (Vsmin).
	 */
	public PU vsmin;

	public PssSB4(){

	}
}//end PssSB4