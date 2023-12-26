package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or
 * Pss2B can also be used).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssELIN2 extends PowerSystemStabilizerDynamics {

	/**
	 * Coefficient (a_PSS).  Typical Value = 0.1.
	 */
	public PU apss;
	/**
	 * Gain (Ks1).  Typical Value = 1.
	 */
	public PU ks1;
	/**
	 * Gain (Ks2).  Typical Value = 0.1.
	 */
	public PU ks2;
	/**
	 * Coefficient (p_PSS) (>=0 and <=4).  Typical Value = 0.1.
	 */
	public PU ppss;
	/**
	 * PSS limiter (psslim).  Typical Value = 0.1.
	 */
	public PU psslim;
	/**
	 * Time constant (Ts1).  Typical Value = 0.
	 */
	public Seconds ts1;
	/**
	 * Time constant (Ts2).  Typical Value = 1.
	 */
	public Seconds ts2;
	/**
	 * Time constant (Ts3).  Typical Value = 1.
	 */
	public Seconds ts3;
	/**
	 * Time constant (Ts4).  Typical Value = 0.1.
	 */
	public Seconds ts4;
	/**
	 * Time constant (Ts5).  Typical Value = 0.
	 */
	public Seconds ts5;
	/**
	 * Time constant (Ts6).  Typical Value = 1.
	 */
	public Seconds ts6;

	public PssELIN2(){

	}
}//end PssELIN2