package IEC61968.Operations;

import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.FloatQuantity;
import IEC61970.Base.Core.Equipment;
import IEC61968.Assets.ProductAssetModel;
import IEC61968.Common.Document;

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
 * @created 03-Jan-2024 1:16:03 PM
 */
public class OperationalRestriction extends Document {

	/**
	 * Interval during which this restriction is applied.
	 */
	public DateTimeInterval activePeriod;
	/**
	 * Restricted (new) value; includes unit of measure and potentially multiplier.
	 */
	public FloatQuantity restrictedValue;
	/**
	 * All equipments to which this restriction applies.
	 */
	public Equipment Equipments;
	/**
	 * Asset model to which this restriction applies.
	 */
	public ProductAssetModel ProductAssetModel;

	public OperationalRestriction(){

	}
}//end OperationalRestriction