///////////////////////////////////////////////////////////
//  LoadResponseCharacteristic.h
//  Implementation of the Class LoadResponseCharacteristic
//  Created on:      25-Dec-2023 8:32:00 PM
//  Original author: kdd
///////////////////////////////////////////////////////////

#if !defined(EA_F59D3419_CCE9_4b56_B5FE_43F57AC88C4E__INCLUDED_)
#define EA_F59D3419_CCE9_4b56_B5FE_43F57AC88C4E__INCLUDED_

#include "Boolean.h"
#include "Float.h"
#include "IdentifiedObject.py"

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
 */
class LoadResponseCharacteristic : public IdentifiedObject
{

public:
	LoadResponseCharacteristic();
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
	Boolean exponentModel;
	/**
	 * Portion of active power load modeled as constant current.
	 */
	Float pConstantCurrent;
	/**
	 * Portion of active power load modeled as constant impedance.
	 */
	Float pConstantImpedance;
	/**
	 * Portion of active power load modeled as constant power.
	 */
	Float pConstantPower;
	/**
	 * Exponent of per unit frequency effecting active power.
	 */
	Float pFrequencyExponent;
	/**
	 * Exponent of per unit voltage effecting real power.
	 */
	Float pVoltageExponent;
	/**
	 * Portion of reactive power load modeled as constant current.
	 */
	Float qConstantCurrent;
	/**
	 * Portion of reactive power load modeled as constant impedance.
	 */
	Float qConstantImpedance;
	/**
	 * Portion of reactive power load modeled as constant power.
	 */
	Float qConstantPower;
	/**
	 * Exponent of per unit frequency effecting reactive power.
	 */
	Float qFrequencyExponent;
	/**
	 * Exponent of per unit voltage effecting reactive power.
	 */
	Float qVoltageExponent;

};
#endif // !defined(EA_F59D3419_CCE9_4b56_B5FE_43F57AC88C4E__INCLUDED_)
