package IEC61968.AssetMeas;


/**
 * Analogs representing oil PCB analysis result.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public enum OilAnalysisPCBAnalogKind {
	/**
	 * Concentration of Aroclor 1221 (in ppm, specifically in mg/kg).
	 */
	aroclor1221,
	/**
	 * Concentration of Aroclor 1242 (in ppm, specifically in mg/kg).
	 */
	aroclor1242,
	/**
	 * Concentration of Aroclor 1254 (in ppm, specifically in mg/kg).
	 */
	aroclor1254,
	/**
	 * Concentration of Aroclor 1260 (in ppm, specifically in mg/kg).
	 */
	aroclor1260,
	/**
	 * Concentration of Aroclor 1016 (in ppm, specifically in mg/kg).
	 */
	aroclor1016,
	/**
	 * Total arochlor (PCB) content (in ppm, specifically in mg/kg). Is the sum of
	 * Aroclor 1221, Aroclor 1242, Aroclor 1254, Aroclor 1260, Aroclor 1016. 
	 */
	totalPCB
}