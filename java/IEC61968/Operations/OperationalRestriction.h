///////////////////////////////////////////////////////////
//  OperationalRestriction.h
//  Implementation of the Class OperationalRestriction
//  Created on:      25-Dec-2023 8:45:23 PM
///////////////////////////////////////////////////////////

#if !defined(EA_CFEB39CE_9820_4896_AF56_9775CE98EE2A__INCLUDED_)
#define EA_CFEB39CE_9820_4896_AF56_9775CE98EE2A__INCLUDED_

#include "java\IEC61970\IEC61970\Base\Domain\DateTimeInterval.java"
#include "java\IEC61970\IEC61970\Base\Domain\FloatQuantity.java"
#include "Equipment.py"
#include "IEC61968\Assets\ProductAssetModel.java"
#include "Document.h"

/**
 * A document that can be associated with equipment to describe any sort of
 * restrictions compared with the original manufacturer's specification or with
 * the usual operational practice e.g. temporary maximum loadings, maximum
 * switching current, do not operate if bus couplers are open, etc.
 * In the UK, for example, if a breaker or switch ever mal-operates, this is
 * reported centrally and utilities use their asset systems to identify all the
 * installed devices of the same manufacturer's type. They then apply operational
 * restrictions in the operational systems to warn operators of potential problems.
 * After appropriate inspection and maintenance, the operational restrictions may
 * be removed.
 */
class OperationalRestriction : public Document
{

public:
	OperationalRestriction();
	/**
	 * Interval during which this restriction is applied.
	 */
	DateTimeInterval activePeriod;
	/**
	 * Restricted (new) value; includes unit of measure and potentially multiplier.
	 */
	FloatQuantity restrictedValue;
	/**
	 * All equipments to which this restriction applies.
	 */
	Equipment *Equipments;
	/**
	 * Asset model to which this restriction applies.
	 */
	ProductAssetModel *ProductAssetModel;

};
#endif // !defined(EA_CFEB39CE_9820_4896_AF56_9775CE98EE2A__INCLUDED_)
