///////////////////////////////////////////////////////////
//  Tariff.h
//  Implementation of the Class Tariff
//  Created on:      25-Dec-2023 8:45:25 PM
///////////////////////////////////////////////////////////

#if !defined(EA_D190EDCE_51C4_4bf1_875A_5B3C6343EB96__INCLUDED_)
#define EA_D190EDCE_51C4_4bf1_875A_5B3C6343EB96__INCLUDED_

#include "Date.h"
#include "IEC61968\PaymentMetering\TariffProfile.java"
#include "Document.h"

/**
 * Document, approved by the responsible regulatory agency, listing the terms and
 * conditions, including a schedule of prices, under which utility services will
 * be provided. It has a unique number within the state or province. For rate
 * schedules it is frequently allocated by the affiliated Public utilities
 * commission (PUC).
 */
class Tariff : public Document
{

public:
	Tariff();
	/**
	 * (if tariff became inactive) Date tariff was terminated.
	 */
	Date endDate;
	/**
	 * Date tariff was activated.
	 */
	Date startDate;
	/**
	 * All tariff profiles using this tariff.
	 */
	TariffProfile *TariffProfiles;

};
#endif // !defined(EA_D190EDCE_51C4_4bf1_875A_5B3C6343EB96__INCLUDED_)
