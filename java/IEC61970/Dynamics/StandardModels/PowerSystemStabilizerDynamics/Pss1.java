package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;

/**
 * Italian PSS - three input PSS (speed, frequency, power).
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class Pss1 extends PowerSystemStabilizerDynamics {

	/**
	 * Frequency power input gain (K<sub>F</sub>).  Typical Value = 5.
	 */
	public Float kf;
	/**
	 * Electric power input gain (K<sub>PE</sub>).  Typical Value = 0.3.
	 */
	public Float kpe;
	/**
	 * PSS gain (K<sub>S</sub>).  Typical Value = 1.
	 */
	public Float ks;
	/**
	 * Shaft speed power input gain (K<sub>W</sub>).  Typical Value = 0.
	 */
	public Float kw;
	/**
	 * Minimum power PSS enabling (P<sub>MIN</sub>).  Typical Value = 0.25.
	 */
	public PU pmin;
	/**
	 * Lead/lag time constant (T<sub>10</sub>).  Typical Value = 0.
	 */
	public Seconds t10;
	/**
	 * Washout (T<sub>5</sub>).  Typical Value = 3.5.
	 */
	public Seconds t5;
	/**
	 * Filter time constant (T<sub>6</sub>).  Typical Value = 0.
	 */
	public Seconds t6;
	/**
	 * Lead/lag time constant (T<sub>7</sub>).  Typical Value = 0.
	 */
	public Seconds t7;
	/**
	 * Lead/lag time constant (T<sub>8</sub>).  Typical Value = 0.
	 */
	public Seconds t8;
	/**
	 * Lead/lag time constant (T<sub>9</sub>).  Typical Value = 0.
	 */
	public Seconds t9;
	/**
	 * Electric power filter time constant (T<sub>PE</sub>).  Typical Value = 0.05.
	 */
	public Seconds tpe;
	/**
	 * <font color="#0f0f0f">Signal selector (V<sub>adAt</sub>).</font>
	 * <font color="#0f0f0f">true = closed (Generator Power is greater than
	 * Pmin)</font>
	 * <font color="#0f0f0f">false = open (Pe is smaller than Pmin).</font>
	 * <font color="#0f0f0f">Typical Value = true.</font>
	 */
	public Boolean vadat;
	/**
	 * Stabilizer output max limit (V<sub>SMN</sub>).  Typical Value = -0.06.
	 */
	public PU vsmn;
	/**
	 * Stabilizer output min limit (V<sub>SMX</sub>).  Typical Value = 0.06.
	 */
	public PU vsmx;

	public Pss1(){

	}
}//end Pss1