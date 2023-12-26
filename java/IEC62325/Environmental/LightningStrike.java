package IEC62325.Environmental;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Length;
import IEC62325.Environmental.EnvDomain.Bearing;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.CurrentFlow;

/**
 * A cloud-to-ground lightning strike at a particular location.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class LightningStrike extends GeosphericPhenomenon {

	/**
	 * Likelihood that strike fell within errorEllipse.
	 */
	public PerCent errorEllipseConfidence;
	/**
	 * Length of major semi-axis (longest radius) of the error ellipse.
	 */
	public Length errorEllipseMajorSemiAxis;
	/**
	 * Length of minor semi-axis (shortest radius) of the error ellipse.
	 */
	public Length errorEllipseMinorSemiAxis;
	/**
	 * The orientation of the major semi- axis in degrees from True North.
	 */
	public Bearing errorEllipseOrientation;
	/**
	 * The polarity of the strike, with T meaning negative. About 90% of all lightning
	 * strokes are negative strokes, meaning that they were initiated by a large
	 * concentration of negative charge in the cloud-base; this tends to induce an
	 * area of positive charge on the ground.
	 */
	public Boolean negativePolarity;
	/**
	 * Peak current of strike.
	 */
	public CurrentFlow peakAmplitude;

	public LightningStrike(){

	}
}//end LightningStrike