package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Italian PSS - Detailed PSS.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class Pss5 extends PowerSystemStabilizerDynamics {

	/**
	 * Selector for Second washout enabling (C<sub>TW2</sub>).
	 * true = second washout filter is bypassed
	 * false = second washout filter in use.
	 * Typical Value = true.
	 */
	public Boolean ctw2;
	/**
	 * Stabilizer output dead band (DeadBand).  Typical Value = 0.
	 */
	public PU deadband;
	/**
	 * Selector for Frequency/shaft speed input (IsFreq).
	 * true = speed
	 * false = frequency.
	 * Typical Value = true.
	 */
	public Boolean isfreq;
	/**
	 * Frequency/shaft speed input gain (K<sub>F</sub>).  Typical Value = 5.
	 */
	public Float kf;
	/**
	 * Electric power input gain (K<sub>PE</sub>).  Typical Value = 0.3.
	 */
	public Float kpe;
	/**
	 * PSS gain (K<sub>PSS</sub>).  Typical Value = 1.
	 */
	public Float kpss;
	/**
	 * Minimum power PSS enabling (P<sub>mn</sub>).  Typical Value = 0.25.
	 */
	public PU pmm;
	/**
	 * Lead/lag time constant (T<sub>L1</sub>).  Typical Value = 0.
	 */
	public Seconds tl1;
	/**
	 * Lead/lag time constant (T<sub>L2</sub>).  Typical Value = 0.
	 */
	public Seconds tl2;
	/**
	 * Lead/lag time constant (T<sub>L3</sub>).  Typical Value = 0.
	 */
	public Seconds tl3;
	/**
	 * Lead/lag time constant (T<sub>L4</sub>).  Typical Value = 0.
	 */
	public Seconds tl4;
	/**
	 * Electric power filter time constant (T<sub>PE</sub>).  Typical Value = 0.05.
	 */
	public Seconds tpe;
	/**
	 * First WashOut (T<sub>w1</sub>).  Typical Value = 3.5.
	 */
	public Seconds tw1;
	/**
	 * Second WashOut (T<sub>w2</sub>).  Typical Value = 0.
	 */
	public Seconds tw2;
	/**
	 * <font color="#0f0f0f">Signal selector (V<sub>adAtt</sub>).</font>
	 * <font color="#0f0f0f">true = closed (Generator Power is greater than
	 * Pmin)</font>
	 * <font color="#0f0f0f">false = open (Pe is smaller than Pmin).</font>
	 * <font color="#0f0f0f">Typical Value = true.</font>
	 */
	public Boolean vadat;
	/**
	 * Stabilizer output max limit (V<sub>SMN</sub>).  Typical Value = -0.1.
	 */
	public PU vsmn;
	/**
	 * Stabilizer output min limit (V<sub>SMX</sub>).  Typical Value = 0.1.
	 */
	public PU vsmx;

	public Pss5(){

	}
}//end Pss5