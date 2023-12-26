package IEC61970.Dynamics.StandardModels.LoadDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * General static load model representing the sensitivity of the real and reactive
 * power consumed by the load to the amplitude and frequency of the bus voltage.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class LoadStatic extends IdentifiedObject {

	/**
	 * First term voltage exponent for active power (Ep1).  Used only when .
	 * staticLoadModelType = exponential.
	 */
	public Float ep1;
	/**
	 * Second term voltage exponent for active power (Ep2).  Used only when .
	 * staticLoadModelType = exponential.
	 */
	public Float ep2;
	/**
	 * Third term voltage exponent for active power (Ep3).  Used only when .
	 * staticLoadModelType = exponential.
	 */
	public Float ep3;
	/**
	 * First term voltage exponent for reactive power (Eq1).  Used only when .
	 * staticLoadModelType = exponential.
	 */
	public Float eq1;
	/**
	 * Second term voltage exponent for reactive power (Eq2).  Used only when .
	 * staticLoadModelType = exponential.
	 */
	public Float eq2;
	/**
	 * Third term voltage exponent for reactive power (Eq3).  Used only when .
	 * staticLoadModelType = exponential.
	 */
	public Float eq3;
	/**
	 * First term voltage coefficient for active power (Kp1).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kp1;
	/**
	 * Second term voltage coefficient for active power (Kp2).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kp2;
	/**
	 * Third term voltage coefficient for active power (Kp3).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kp3;
	/**
	 * Frequency coefficient for active power (Kp4).  Must be non-zero when .
	 * staticLoadModelType = ZIP2.  Not used for all other values of .
	 * staticLoadModelType.
	 */
	public Float kp4;
	/**
	 * Frequency deviation coefficient for active power (Kpf).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kpf;
	/**
	 * First term voltage coefficient for reactive power (Kq1).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kq1;
	/**
	 * Second term voltage coefficient for reactive power (Kq2).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kq2;
	/**
	 * Third term voltage coefficient for reactive power (Kq3).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kq3;
	/**
	 * Frequency coefficient for reactive power (Kq4).  Must be non-zero when .
	 * staticLoadModelType = ZIP2.  Not used for all other values of .
	 * staticLoadModelType.
	 */
	public Float kq4;
	/**
	 * Frequency deviation coefficient for reactive power (Kqf).  Not used when .
	 * staticLoadModelType = constantZ.
	 */
	public Float kqf;
	/**
	 * Type of static load model.  Typical Value = constantZ.
	 */
	public StaticLoadModelKind staticLoadModelType;
	/**
	 * Aggregate load to which this aggregate static load belongs.
	 */
	public LoadAggregate LoadAggregate;

	public LoadStatic(){

	}
}//end LoadStatic