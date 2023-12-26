package IEC62325.Environmental.EnvDomain;


/**
 * Kinds of analogs (floats)  measuring an atmospheric condition.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public enum AtmosphericAnalogKind {
	albedo,
	/**
	 * The temperature measured b<font color="#0f0f0f">y a thermometer exposed to the
	 * air in a place sheltered from direct solar radiation. </font>Also known as "dry
	 * bulb" because<font color="#0f0f0f"> the air temperature is indicated by a
	 * thermometer not affecte</font>d by the moisture of the air.
	 */
	ambientTemperature,
	atmosphericPressure,
	ceiling,
	/**
	 * The temperature to which air must be cooled at constant pressure and constant
	 * water-vapor content in order for saturation to occur. In other words, it is the
	 * temperature at which water vapor starts to condense out of the air.
	 */
	dewPoint,
	/**
	 * The temperature of how hot it "feels like" for a given combination of warm air
	 * temperature and relative humidity. 
	 */
	heatIndex,
	horizontalVisibility,
	humidity,
	ice,
	illuminanceDiffuseHorizontal,
	illuminanceDirectNormal,
	illuminanceGlobalHorizontal,
	irradianceDiffuseHorizonal,
	irradianceDirectNormal,
	irradianceExtraTerrestrialHorizontal,
	irradianceExtraTerrestrialVertical,
	irradianceGlobalHorizontal,
	luminanceZenith,
	precipitation,
	rain,
	skyCoverageOpaque,
	skyCoverageTotal,
	/**
	 * Snow amount over a specified period of time.
	 */
	snow,
	/**
	 * The temperature of how cold it "feels like" based on the rate of heat loss from
	 * exposed skin caused by the effects of wind and cold temperatures. 
	 */
	windChill,
	/**
	 * Maximum instantaneous wind speed in the 10 minute period preceding a moment in
	 * time so long as more than 10 knots of difference has been exhibited between
	 * peaks and lulls during that 10 minute time period.
	 * 0 value means no gusts during preceding 10 minute period.
	 */
	windSpeedGust,
	/**
	 * Wind speed at a moment in time.
	 */
	windSpeedInstantaneous,
	/**
	 * Peak instantaneous wind speed in the 60 minutes preceding a moment in time as
	 * long as peak speed greater than 25 knots.
	 * 0 value means speed did not exceed 25 knots during preceding 60 minutes.
	 */
	windSpeedPeak,
	/**
	 * Average instantaneous wind speed over the 2-minute time period preceding a
	 * moment in time.
	 */
	windSpeedSustained,
	verticalVisibility
}