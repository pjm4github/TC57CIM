package IEC61968.DER;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.ReactivePower;

/**
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public class DispatchablePowerCapability {

	/**
	 * Product of RMS value of the voltage and the RMS value of the in-phase component
	 * of the current
	 */
	public ActivePower currentActivePower;
	/**
	 * Product of the RMS value of the voltage and the RMS value of the current
	 */
	public ApparentPower currentApparentPower;
	/**
	 * Product of RMS value of the voltage and the RMS value of the quadrature
	 * component of the current
	 */
	public ReactivePower currentReactivePower;
	/**
	 * Product of RMS value of the voltage and the RMS value of the in-phase component
	 * of the current
	 */
	public ActivePower maxActivePower;
	/**
	 * Product of the RMS value of the voltage and the RMS value of the current
	 */
	public ApparentPower maxApparentPower;
	/**
	 * Product of RMS value of the voltage and the RMS value of the quadrature
	 * component of the current
	 */
	public ReactivePower maxReactivePower;
	/**
	 * Product of RMS value of the voltage and the RMS value of the in-phase component
	 * of the current
	 */
	public ActivePower minActivePower;
	/**
	 * Product of the RMS value of the voltage and the RMS value of the current
	 */
	public ApparentPower minApparentPower;
	/**
	 * Product of RMS value of the voltage and the RMS value of the quadrature
	 * component of the current
	 */
	public ReactivePower minReactivePower;

	public DispatchablePowerCapability(){

	}
}//end DispatchablePowerCapability