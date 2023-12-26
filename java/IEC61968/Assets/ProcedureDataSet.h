///////////////////////////////////////////////////////////
//  ProcedureDataSet.h
//  Implementation of the Class ProcedureDataSet
//  Created on:      25-Dec-2023 8:45:24 PM
///////////////////////////////////////////////////////////

#if !defined(EA_30A01BF2_270E_42d2_941D_D9C6D732C05E__INCLUDED_)
#define EA_30A01BF2_270E_42d2_941D_D9C6D732C05E__INCLUDED_

#include "DateTime.py"
#include "Asset.h"
#include "MeasurementValue.h"
#include "TransformerObservation.h"
#include "IEC61968\Work\WorkTask.java"
#include "Document.h"

/**
 * A data set recorded each time a procedure is executed. Observed results are
 * captured in associated measurement values and/or values for properties relevant
 * to the type of procedure performed.
 */
class ProcedureDataSet : public Document
{

public:
	ProcedureDataSet();
	/**
	 * Date and time procedure was completed.
	 */
	DateTime completedDateTime;
	/**
	 * Asset to which this procedure data set applies.
	 */
	Asset *Asset;
	MeasurementValue *MeasurementValue;
	TransformerObservation *TransformerObservations;
	/**
	 * Work task that created this procedure data set.
	 */
	WorkTask *WorkTask;

};
#endif // !defined(EA_30A01BF2_270E_42d2_941D_D9C6D732C05E__INCLUDED_)
