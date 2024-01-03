package IEC62325.InfIEC62325.InfExternalInputs;

import IEC61970.Base.Core.Curve;

/**
 * Optionally, this curve expresses elasticity of the associated requirement.  For
 * example, used to reduce requirements when clearing price exceeds reasonable
 * values when the supply quantity becomes scarce. For example, a single point
 * value of $1000/MW for a spinning reserve will cause a reduction in the required
 * spinning reserve.
 * X axis is constrained quantity (e.g., MW)
 * Y1 axis is money per constrained quantity
 * @created 03-Jan-2024 1:51:06 PM
 */
public class SensitivityPriceCurve extends Curve {

	public SensitivityPriceCurve(){

	}
}//end SensitivityPriceCurve