package IEC61968.Assets;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * The precise standard used in executing a lab test, including the standard, and
 * standard version, test method and variant, if needed.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TestStandard extends IdentifiedObject {

	/**
	 * Identification of test method used if multiple methods specified by test
	 * standard.
	 */
	public TestMethod testMethod;
	/**
	 * Which ASTM standard used to determine analog value result. Applies only if ASTM
	 * standard used.
	 */
	public ASTMStandard testStandardASTM;
	/**
	 * Which CIGRE standard used to determine analog value result. Applies only if
	 * CIGRE standard used.
	 */
	public CIGREStandard testStandardCIGRE;
	/**
	 * Which DIN standard used to determine analog value result. Applies only if DIN
	 * standard used.
	 */
	public DINStandard testStandardDIN;
	/**
	 * Which Doble standard used to determine analog value result. Applies only if
	 * Doble standard used.
	 */
	public DobleStandard testStandardDoble;
	/**
	 * Which EPA standard used to determine analog value result. Applies only if EPA
	 * standard used.
	 */
	public EPAStandard testStandardEPA;
	/**
	 * Which IEC standard used to determine analog value result. Applies only if IEC
	 * standard used.
	 */
	public IECStandard testStandardIEC;
	/**
	 * Which IEEE standard used to determine analog value result. Applies only if IEEE
	 * standard used.
	 */
	public IEEEStandard testStandardIEEE;
	/**
	 * Which ISO standard used to determine analog value result. Applies only if ISO
	 * standard used.
	 */
	public ISOStandard testStandardISO;
	/**
	 * Which Laborelec standard used to determine analog value result. Applies only if
	 * Laborelec standard used.
	 */
	public LaborelecStandard testStandardLaborelec;
	/**
	 * Which TAPPI standard used to determine analog value result. Applies only if
	 * TAPPI standard used.
	 */
	public TAPPIStandard testStandardTAPPI;
	/**
	 * Which UK Ministry of Defence standard used to determine analog value result.
	 * Applies only if UK Ministry of Defence standard used.
	 */
	public UKMinistryOfDefenceStandard testStandardUKMinistryOfDefence;
	/**
	 * Which WEP standard used to determine analog value result. Applies only if WEP
	 * standard used.
	 */
	public WEPStandard testStandardWEP;
	/**
	 * Identification of variant of test method or standard if one is specified by the
	 * standard.
	 */
	public TestVariantKind testVariant;

	public TestStandard(){

	}
}//end TestStandard