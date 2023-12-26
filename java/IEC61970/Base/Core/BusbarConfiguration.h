///////////////////////////////////////////////////////////
//  BusbarConfiguration.h
//  Implementation of the Class BusbarConfiguration
//  Created on:      25-Dec-2023 8:31:54 PM
///////////////////////////////////////////////////////////

#if !defined(EA_B9AF7C39_8B42_49d9_9B31_D6F0A96EAD8C__INCLUDED_)
#define EA_B9AF7C39_8B42_49d9_9B31_D6F0A96EAD8C__INCLUDED_

/**
 * Busbar layout for bay.
 */
enum BusbarConfiguration
{
	/**
	 * Single bus.
	 */
	singleBus,
	/**
	 * Double bus.
	 */
	doubleBus,
	/**
	 * Main bus with transfer bus.
	 */
	mainWithTransfer,
	/**
	 * Ring bus.
	 */
	ringBus
};
#endif // !defined(EA_B9AF7C39_8B42_49d9_9B31_D6F0A96EAD8C__INCLUDED_)
