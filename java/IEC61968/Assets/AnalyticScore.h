///////////////////////////////////////////////////////////
//  AnalyticScore.h
//  Implementation of the Class AnalyticScore
//  Created on:      25-Dec-2023 8:45:18 PM
//  Original author: Gowri
///////////////////////////////////////////////////////////

#if !defined(EA_CD1F4D89_C863_43fd_8395_FFB25C5F652A__INCLUDED_)
#define EA_CD1F4D89_C863_43fd_8395_FFB25C5F652A__INCLUDED_

#include "DateTime.py"
#include "Float.h"
#include "IdentifiedObject.py"
#include "Asset.h"

/**
 * An indicative scoring by an analytic that can be used to characterize the
 * health of or the risk associated with one or more assets.  The analytic score
 * reflects the results of an execution of an analytic against an asset or group
 * of assets.
 */
class AnalyticScore : public IdentifiedObject
{

public:
	AnalyticScore();
	/**
	 * Timestamp of when the score was calculated.
	 */
	DateTime calculationDateTime;
	/**
	 * Date-time for when the score applies.
	 */
	DateTime effectiveDateTime;
	/**
	 * Asset health score value.
	 */
	Float value;
	Asset *Asset;

};
#endif // !defined(EA_CD1F4D89_C863_43fd_8395_FFB25C5F652A__INCLUDED_)
