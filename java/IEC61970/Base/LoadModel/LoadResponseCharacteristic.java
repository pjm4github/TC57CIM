package IEC61970.Base.LoadModel;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Models the characteristic response of the load demand due to changes in system
 * conditions such as voltage and frequency. This is not related to demand
 * response.
 * 
 * If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are
 * specified and used as to calculate:
 * 
 * Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) **
 * cim:LoadResponseCharacteristic.pVoltageExponent
 * 
 * Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.
 * nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent
 * 
 * Where  * means "multiply" and ** is "raised to power of".
 * @author kdd
 * @version 1.0
 * @created 02-Jan-2024 11:10:58 PM
 */
public class LoadResponseCharacteristic extends IdentifiedObject {

	/**
	 * Indicates the exponential voltage dependency model is to be used.   If false,
	 * the coefficient model is to be used.
	 * The exponential voltage dependency model consist of the attributes
	 * - pVoltageExponent
	 * - qVoltageExponent.
	 * The coefficient model consist of the attributes
	 * - pConstantImpedance
	 * - pConstantCurrent
	 * - pConstantPower
	 * - qConstantImpedance
	 * - qConstantCurrent
	 * - qConstantPower.
	 * The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall equal
	 * 1.
	 * The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal
	 * 1.
	 */
	public Boolean exponentModel;
	/**
	 * Portion of active power load modeled as constant current.
	 */
	public Float pConstantCurrent;
	/**
	 * Portion of active power load modeled as constant impedance.
	 */
	public Float pConstantImpedance;
	/**
	 * Portion of active power load modeled as constant power.
	 */
	public Float pConstantPower;
	/**
	 * Exponent of per unit frequency effecting active power.
	 */
	public Float pFrequencyExponent;
	/**
	 * Exponent of per unit voltage effecting real power.
	 */
	public Float pVoltageExponent;
	/**
	 * Portion of reactive power load modeled as constant current.
	 */
	public Float qConstantCurrent;
	/**
	 * Portion of reactive power load modeled as constant impedance.
	 */
	public Float qConstantImpedance;
	/**
	 * Portion of reactive power load modeled as constant power.
	 */
	public Float qConstantPower;
	/**
	 * Exponent of per unit frequency effecting reactive power.
	 */
	public Float qFrequencyExponent;
	/**
	 * Exponent of per unit voltage effecting reactive power.
	 */
	public Float qVoltageExponent;

	public LoadResponseCharacteristic(){

	}
}//end LoadResponseCharacteristic