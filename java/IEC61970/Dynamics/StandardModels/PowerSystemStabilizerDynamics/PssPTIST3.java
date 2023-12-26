package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;

/**
 * PTI Microprocessor-Based Stabilizer type 3.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PssPTIST3 extends PowerSystemStabilizerDynamics {

	/**
	 * Filter coefficient (A0). 
	 */
	public PU a0;
	/**
	 * Limiter (Al). 
	 */
	public PU a1;
	/**
	 * Filter coefficient (A2). 
	 */
	public PU a2;
	/**
	 * Filter coefficient (A3). 
	 */
	public PU a3;
	/**
	 * Filter coefficient (A4). 
	 */
	public PU a4;
	/**
	 * Filter coefficient (A5). 
	 */
	public PU a5;
	/**
	 * Limiter (Al).
	 */
	public PU al;
	/**
	 * Threshold value above which output averaging will be bypassed (Athres).
	 * Typical Value = 0.005.
	 */
	public PU athres;
	/**
	 * Filter coefficient (B0). 
	 */
	public PU b0;
	/**
	 * Filter coefficient (B1). 
	 */
	public PU b1;
	/**
	 * Filter coefficient (B2). 
	 */
	public PU b2;
	/**
	 * Filter coefficient (B3). 
	 */
	public PU b3;
	/**
	 * Filter coefficient (B4). 
	 */
	public PU b4;
	/**
	 * Filter coefficient (B5). 
	 */
	public PU b5;
	/**
	 * Limiter (Dl). 
	 */
	public PU dl;
	/**
	 * Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical
	 * Value = 0.025.
	 */
	public Seconds dtc;
	/**
	 * Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025.
	 */
	public Seconds dtf;
	/**
	 * Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.
	 * 0125.
	 */
	public Seconds dtp;
	/**
	 * Digital/analog output switch (Isw).
	 * true = produce analog output
	 * false = convert to digital output, using tap selection table. 
	 */
	public Boolean isw;
	/**
	 * Gain (K).  Typical Value = 9.
	 */
	public PU k;
	/**
	 * Threshold value (Lthres).
	 */
	public PU lthres;
	/**
	 * (M).  M=2*H.  Typical Value = 5.
	 */
	public PU m;
	/**
	 * Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4.
	 */
	public Float nav;
	/**
	 * Number of counts at limit to active limit function (Ncl) (>0). 
	 */
	public Float ncl;
	/**
	 * Number of counts until reset after limit function is triggered (Ncr). 
	 */
	public Float ncr;
	/**
	 * (Pmin).
	 */
	public PU pmin;
	/**
	 * Time constant (T1).  Typical Value = 0.3.
	 */
	public Seconds t1;
	/**
	 * Time constant (T2).  Typical Value = 1.
	 */
	public Seconds t2;
	/**
	 * Time constant (T3).  Typical Value = 0.2.
	 */
	public Seconds t3;
	/**
	 * Time constant (T4).  Typical Value = 0.05.
	 */
	public Seconds t4;
	/**
	 * Time constant (T5). 
	 */
	public Seconds t5;
	/**
	 * Time constant (T6). 
	 */
	public Seconds t6;
	/**
	 * Time constant (Tf).  Typical Value = 0.2.
	 */
	public Seconds tf;
	/**
	 * Time constant (Tp).  Typical Value = 0.2.
	 */
	public Seconds tp;

	public PssPTIST3(){

	}
}//end PssPTIST3