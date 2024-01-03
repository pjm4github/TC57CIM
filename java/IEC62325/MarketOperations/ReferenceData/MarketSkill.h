///////////////////////////////////////////////////////////
//  MarketSkill.h
//  Implementation of the Class MarketSkill
//  Created on:      03-Jan-2024 2:15:34 PM
///////////////////////////////////////////////////////////

#if !defined(EA_7B0A6E7A_3E7C_4905_9AD4_7493EB4E9029__INCLUDED_)
#define EA_7B0A6E7A_3E7C_4905_9AD4_7493EB4E9029__INCLUDED_

#include "java\IEC61970\Base\Domain\IEC61970\Base\Domain\DateTimeInterval.java"
#include "java\IEC61970\Base\Domain\IEC61970\Base\Domain\DateTime.java"
#include "java\IEC61970\Base\Domain\IEC61970\Base\Domain\String.java"
#include "java\IEC61968\Common\Document.java"
#include "MarketQualificationRequirement.java"

/**
 * Proficiency level of a craft, which is required to operate or maintain a
 * particular type of asset and/or perform certain types of work. 
 */
class MarketSkill : public Document
{

public:
	MarketSkill();
	/**
	 * Interval between the certification and its expiry.
	 */
	DateTimeInterval certificationPeriod;
	/**
	 * Date and time the skill became effective.
	 */
	DateTime effectiveDateTime;
	/**
	 * Level of skill for a Craft.
	 */
	String level;
	MarketQualificationRequirement *MarketQualificationRequirements;

};
#endif // !defined(EA_7B0A6E7A_3E7C_4905_9AD4_7493EB4E9029__INCLUDED_)
