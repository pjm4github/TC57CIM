///////////////////////////////////////////////////////////
//  OperatingParticipant.h
//  Implementation of the Class OperatingParticipant
//  Created on:      25-Dec-2023 8:32:01 PM
//  Original author: kdd
///////////////////////////////////////////////////////////

#if !defined(EA_CE78ED36_A6C5_47a5_89D2_2F85717C825E__INCLUDED_)
#define EA_CE78ED36_A6C5_47a5_89D2_2F85717C825E__INCLUDED_

#include "IdentifiedObject.py"

/**
 * An operator of multiple power system resource objects. Note multple operating
 * participants may operate the same power system resource object.   This can be
 * used for modeling jointly owned units where each owner operates as a
 * contractual share.
 */
class OperatingParticipant : public IdentifiedObject
{

public:
	OperatingParticipant();

};
#endif // !defined(EA_CE78ED36_A6C5_47a5_89D2_2F85717C825E__INCLUDED_)
