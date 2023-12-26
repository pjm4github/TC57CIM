package IEC61968.Assets;

import IEC61970.Base.Domain.Float;
import IEC61968.Common.Document;

/**
 * An algorithm or calculation for making an assessment about an asset or asset
 * grouping for lifecycle decision making.
 * @author Gowri
 * @version 1.0
 * @created 25-Dec-2023 8:45:18 PM
 */
public class Analytic extends Document {

	/**
	 * Value that indicates best possible numeric value.
	 */
	public Float bestValue;
	/**
	 * Kind of analytic this analytic is.
	 */
	public AnalyticKind kind;
	/**
	 * The scoring scale kind.
	 */
	public ScaleKind scaleKind;
	/**
	 * Value that indicates worst possible numeric value.
	 */
	public Float worstValue;
	public AssetGroup AssetGroup;
	public AnalyticScore AnalyticScore;
	public AssetHealthEvent AssetHealthEvent;
	public Asset Asset;

	public Analytic(){

	}
}//end Analytic