///////////////////////////////////////////////////////////
//  Structure.h
//  Implementation of the Class Structure
//  Created on:      25-Dec-2023 8:45:24 PM
///////////////////////////////////////////////////////////

#if !defined(EA_6F378E6E_133A_4de9_A20C_F83A385F5772__INCLUDED_)
#define EA_6F378E6E_133A_4de9_A20C_F83A385F5772__INCLUDED_

#include "Date.h"
#include "String.h"
#include "Length.py"
#include "IEC61968\InfIEC61968\InfAssets\StructureMaterialKind.java"
#include "Voltage.h"
#include "Boolean.h"
#include "AssetContainer.py"
#include "StructureSupport.h"

/**
 * Construction holding assets such as conductors, transformers, switchgear, etc.
 * Where applicable, number of conductors can be derived from the number of
 * associated wire spacing instances.
 */
class Structure : public AssetContainer
{

public:
	Structure();
	/**
	 * Date fumigant was last applied.
	 */
	Date fumigantAppliedDate;
	/**
	 * Name of fumigant.
	 */
	String fumigantName;
	/**
	 * Visible height of structure above ground level for overhead construction (e.g.,
	 * Pole or Tower) or below ground level for an underground vault, manhole, etc.
	 * Refer to associated DimensionPropertiesInfo for other types of dimensions.
	 */
	Length height;
	/**
	 * Material this structure is made of.
	 */
	StructureMaterialKind materialKind;
	/**
	 * Maximum rated voltage of the equipment that can be mounted on/contained within
	 * the structure.
	 */
	Voltage ratedVoltage;
	/**
	 * True if weeds are to be removed around asset.
	 */
	Boolean removeWeed;
	/**
	 * Date weed were last removed.
	 */
	Date weedRemovedDate;
	StructureSupport *StructureSupports;

};
#endif // !defined(EA_6F378E6E_133A_4de9_A20C_F83A385F5772__INCLUDED_)
