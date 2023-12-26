package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer
 * model. The PSS4B model represents a structure based on multiple working
 * frequency bands. Three separate bands, respectively dedicated to the low-,
 * intermediate- and high-frequency modes of oscillations, are used in this delta-
 * omega (speed input) PSS.
 * 
 * Reference: IEEE 4B 421.5-2005 Section 8.4.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssIEEE4B extends PowerSystemStabilizerDynamics {

	/**
	 * Notch filter 1 (high-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
	 */
	public Float bwh1;
	/**
	 * Notch filter 2 (high-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
	 */
	public Float bwh2;
	/**
	 * Notch filter 1 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
	 */
	public Float bwl1;
	/**
	 * Notch filter 2 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
	 */
	public Float bwl2;
	/**
	 * High band gain (K<sub>H</sub>).  Typical Value = 120.
	 */
	public PU kh;
	/**
	 * High band differential filter gain (K<sub>H1</sub>).  Typical Value = 66.
	 */
	public PU kh1;
	/**
	 * High band first lead-lag blocks coefficient (K<sub>H11</sub>).  Typical Value =
	 * 1.
	 */
	public PU kh11;
	/**
	 * High band first lead-lag blocks coefficient (K<sub>H17</sub>).  Typical Value =
	 * 1.
	 */
	public PU kh17;
	/**
	 * High band differential filter gain (K<sub>H2</sub>).  Typical Value = 66.
	 */
	public PU kh2;
	/**
	 * Intermediate band gain (K<sub>I</sub>).  Typical Value = 30.
	 */
	public PU ki;
	/**
	 * Intermediate band differential filter gain (K<sub>I1</sub>).  Typical Value =
	 * 66.
	 */
	public PU ki1;
	/**
	 * Intermediate band first lead-lag blocks coefficient (K<sub>I11</sub>).  Typical
	 * Value = 1.
	 */
	public PU ki11;
	/**
	 * Intermediate band first lead-lag blocks coefficient (K<sub>I17</sub>).  Typical
	 * Value = 1.
	 */
	public PU ki17;
	/**
	 * Intermediate band differential filter gain (K<sub>I2</sub>).  Typical Value =
	 * 66.
	 */
	public PU ki2;
	/**
	 * Low band gain (K<sub>L</sub>).  Typical Value = 7.5.
	 */
	public PU kl;
	/**
	 * Low band differential filter gain (K<sub>L1</sub>).  Typical Value = 66.
	 */
	public PU kl1;
	/**
	 * Low band first lead-lag blocks coefficient (K<sub>L11</sub>).  Typical Value =
	 * 1.
	 */
	public PU kl11;
	/**
	 * Low band first lead-lag blocks coefficient (K<sub>L17</sub>).  Typical Value =
	 * 1.
	 */
	public PU kl17;
	/**
	 * Low band differential filter gain (K<sub>L2</sub>).  Typical Value = 66.
	 */
	public PU kl2;
	/**
	 * Notch filter 1 (high-frequency band): filter frequency (omega<sub>ni</sub>).
	 */
	public Float omeganh1;
	/**
	 * Notch filter 2 (high-frequency band): filter frequency (omega<sub>ni</sub>).
	 */
	public Float omeganh2;
	/**
	 * Notch filter 1 (low-frequency band): filter frequency (omega<sub>ni</sub>).
	 */
	public Float omeganl1;
	/**
	 * Notch filter 2 (low-frequency band): filter frequency (omega<sub>ni</sub>).
	 */
	public Float omeganl2;
	/**
	 * High band time constant (T<sub>H1</sub>).  Typical Value = 0.01513.
	 */
	public Seconds th1;
	/**
	 * High band time constant (T<sub>H10</sub>).  Typical Value = 0.
	 */
	public Seconds th10;
	/**
	 * High band time constant (T<sub>H11</sub>).  Typical Value = 0.
	 */
	public Seconds th11;
	/**
	 * High band time constant (T<sub>H12</sub>).  Typical Value = 0.
	 */
	public Seconds th12;
	/**
	 * High band time constant (T<sub>H2</sub>).  Typical Value = 0.01816.
	 */
	public Seconds th2;
	/**
	 * High band time constant (T<sub>H3</sub>).  Typical Value = 0.
	 */
	public Seconds th3;
	/**
	 * High band time constant (T<sub>H4</sub>).  Typical Value = 0.
	 */
	public Seconds th4;
	/**
	 * High band time constant (T<sub>H5</sub>).  Typical Value = 0.
	 */
	public Seconds th5;
	/**
	 * High band time constant (T<sub>H6</sub>).  Typical Value = 0.
	 */
	public Seconds th6;
	/**
	 * High band time constant (T<sub>H7</sub>).  Typical Value = 0.01816.
	 */
	public Seconds th7;
	/**
	 * High band time constant (T<sub>H8</sub>).  Typical Value = 0.02179.
	 */
	public Seconds th8;
	/**
	 * High band time constant (T<sub>H9</sub>).  Typical Value = 0.
	 */
	public Seconds th9;
	/**
	 * Intermediate band time constant (T<sub>I1</sub>).  Typical Value = 0.173.
	 */
	public Seconds ti1;
	/**
	 * Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
	 */
	public Seconds ti10;
	/**
	 * Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
	 */
	public Seconds ti11;
	/**
	 * Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.
	 */
	public Seconds ti12;
	/**
	 * Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.2075.
	 */
	public Seconds ti2;
	/**
	 * Intermediate band time constant (T<sub>I3</sub>).  Typical Value = 0.
	 */
	public Seconds ti3;
	/**
	 * Intermediate band time constant (T<sub>I4</sub>).  Typical Value = 0.
	 */
	public Seconds ti4;
	/**
	 * Intermediate band time constant (T<sub>I5</sub>).  Typical Value = 0.
	 */
	public Seconds ti5;
	/**
	 * Intermediate band time constant (T<sub>I6</sub>).  Typical Value = 0.
	 */
	public Seconds ti6;
	/**
	 * Intermediate band time constant (T<sub>I7</sub>).  Typical Value = 0.2075.
	 */
	public Seconds ti7;
	/**
	 * Intermediate band time constant (T<sub>I8</sub>).  Typical Value = 0.2491.
	 */
	public Seconds ti8;
	/**
	 * Intermediate band time constant (T<sub>I9</sub>).  Typical Value = 0.
	 */
	public Seconds ti9;
	/**
	 * Low band time constant (T<sub>L1</sub>).  Typical Value = 1.73.
	 */
	public Seconds tl1;
	/**
	 * Low band time constant (T<sub>L10</sub>).  Typical Value = 0.
	 */
	public Seconds tl10;
	/**
	 * Low band time constant (T<sub>L11</sub>).  Typical Value = 0.
	 */
	public Seconds tl11;
	/**
	 * Low band time constant (T<sub>L12</sub>).  Typical Value = 0.
	 */
	public Seconds tl12;
	/**
	 * Low band time constant (T<sub>L2</sub>).  Typical Value = 2.075.
	 */
	public Seconds tl2;
	/**
	 * Low band time constant (T<sub>L3</sub>).  Typical Value = 0.
	 */
	public Seconds tl3;
	/**
	 * Low band time constant (T<sub>L4</sub>).  Typical Value = 0.
	 */
	public Seconds tl4;
	/**
	 * Low band time constant (T<sub>L5</sub>).  Typical Value = 0.
	 */
	public Seconds tl5;
	/**
	 * Low band time constant (T<sub>L6</sub>).  Typical Value = 0.
	 */
	public Seconds tl6;
	/**
	 * Low band time constant (T<sub>L7</sub>).  Typical Value = 2.075.
	 */
	public Seconds tl7;
	/**
	 * Low band time constant (T<sub>L8</sub>).  Typical Value = 2.491.
	 */
	public Seconds tl8;
	/**
	 * Low band time constant (T<sub>L9</sub>).  Typical Value = 0.
	 */
	public Seconds tl9;
	/**
	 * High band output maximum limit (V<sub>Hmax</sub>).  Typical Value = 0.6.
	 */
	public PU vhmax;
	/**
	 * High band output minimum limit (V<sub>Hmin</sub>).  Typical Value = -0.6.
	 */
	public PU vhmin;
	/**
	 * Intermediate band output maximum limit (V<sub>Imax</sub>).  Typical Value = 0.6.
	 */
	public PU vimax;
	/**
	 * Intermediate band output minimum limit (V<sub>Imin</sub>).  Typical Value = -0.
	 * 6.
	 */
	public PU vimin;
	/**
	 * Low band output maximum limit (V<sub>Lmax</sub>).  Typical Value = 0.075.
	 */
	public PU vlmax;
	/**
	 * Low band output minimum limit (V<sub>Lmin</sub>).  Typical Value = -0.075.
	 */
	public PU vlmin;
	/**
	 * PSS output maximum limit (V<sub>STmax</sub>).  Typical Value = 0.15.
	 */
	public PU vstmax;
	/**
	 * PSS output minimum limit (V<sub>STmin</sub>).  Typical Value = -0.15.
	 */
	public PU vstmin;

	public PssIEEE4B(){

	}
}//end PssIEEE4B