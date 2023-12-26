///////////////////////////////////////////////////////////
//  GeneratorControlSource.h
//  Implementation of the Class GeneratorControlSource
//  Created on:      25-Dec-2023 8:31:58 PM
///////////////////////////////////////////////////////////

#if !defined(EA_7C5A7CB2_3271_4e72_9DAF_F3EF37E19885__INCLUDED_)
#define EA_7C5A7CB2_3271_4e72_9DAF_F3EF37E19885__INCLUDED_

/**
 * The source of controls for a generating unit.
 */
enum GeneratorControlSource
{
	/**
	 * Not available.
	 */
	unavailable,
	/**
	 * Off of automatic generation control (AGC).
	 */
	offAGC,
	/**
	 * On automatic generation control (AGC).
	 */
	onAGC,
	/**
	 * Plant is controlling.
	 */
	plantControl
};
#endif // !defined(EA_7C5A7CB2_3271_4e72_9DAF_F3EF37E19885__INCLUDED_)
