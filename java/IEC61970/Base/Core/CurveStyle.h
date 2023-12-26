///////////////////////////////////////////////////////////
//  CurveStyle.h
//  Implementation of the Class CurveStyle
//  Created on:      25-Dec-2023 8:31:55 PM
///////////////////////////////////////////////////////////

#if !defined(EA_DDC2241E_52BD_4f0c_8E1B_3C7AE1FC4323__INCLUDED_)
#define EA_DDC2241E_52BD_4f0c_8E1B_3C7AE1FC4323__INCLUDED_

/**
 * Style or shape of curve.
 */
enum CurveStyle
{
	/**
	 * The Y-axis values are assumed constant until the next curve point and prior to
	 * the first curve point.
	 */
	constantYValue,
	/**
	 * The Y-axis values are assumed to be a straight line between values.  Also known
	 * as linear interpolation.
	 */
	straightLineYValues
};
#endif // !defined(EA_DDC2241E_52BD_4f0c_8E1B_3C7AE1FC4323__INCLUDED_)
