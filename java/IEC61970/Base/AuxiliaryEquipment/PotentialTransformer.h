///////////////////////////////////////////////////////////
//  PotentialTransformer.h
//  Implementation of the Class PotentialTransformer
//  Created on:      25-Dec-2023 8:32:01 PM
///////////////////////////////////////////////////////////

#if !defined(EA_F57F47B5_3B3B_45b8_965B_AC2886A00E32__INCLUDED_)
#define EA_F57F47B5_3B3B_45b8_965B_AC2886A00E32__INCLUDED_

#include "String.h"
#include "Float.h"
#include "java\IEC61970\IEC61970\Base\AuxiliaryEquipment\PotentialTransformerKind.java"
#include "java\IEC61970\IEC61970\Base\AuxiliaryEquipment\Sensor.java"

/**
 * Instrument transformer (also known as Voltage Transformer) used to measure
 * electrical qualities of the circuit that is being protected and/or monitored.
 * Typically used as voltage transducer for the purpose of metering, protection,
 * or sometimes auxiliary substation supply. A typical secondary voltage rating
 * would be 120V.
 */
class PotentialTransformer : public Sensor
{

public:
	PotentialTransformer();
	/**
	 * PT accuracy classification.
	 */
	String accuracyClass;
	/**
	 * Nominal ratio between the primary and secondary voltage.
	 */
	Float nominalRatio;
	/**
	 * Potential transformer (PT) classification covering burden.
	 */
	String ptClass;
	/**
	 * Potential transformer construction type.
	 */
	PotentialTransformerKind type;

};
#endif // !defined(EA_F57F47B5_3B3B_45b8_965B_AC2886A00E32__INCLUDED_)
