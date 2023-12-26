///////////////////////////////////////////////////////////
//  CatalogAssetType.h
//  Implementation of the Class CatalogAssetType
//  Created on:      25-Dec-2023 8:45:20 PM
///////////////////////////////////////////////////////////

#if !defined(EA_35841C18_1480_44ee_8647_666CA1ADE89F__INCLUDED_)
#define EA_35841C18_1480_44ee_8647_666CA1ADE89F__INCLUDED_

#include "Money.py"
#include "IEC61968\Assets\AssetKind.java"
#include "StringQuantity.py"
#include "Boolean.h"
#include "String.h"
#include "TypeAssetCatalogue.py"
#include "IdentifiedObject.py"
#include "\ErpReqLineItem.java"
#include "ErpBomItemData.py"

/**
 * assets that may be used for planning, work or design purposes.
 */
class CatalogAssetType : public IdentifiedObject
{

public:
	CatalogAssetType();
	/**
	 * Estimated unit cost (or cost per unit length) of this type of asset. It does
	 * not include labor to install, construct or configure it.
	 */
	Money estimatedUnitCost;
	AssetKind kind;
	/**
	 * The value, unit of measure, and multiplier for the quantity.
	 */
	StringQuantity quantity;
	/**
	 * True if item is a stock item (default).
	 */
	Boolean stockItem;
	String type;
	TypeAssetCatalogue *TypeAssetCatalogue;
	ErpReqLineItem *ErpReqLineItems;
	ErpBomItemData *ErpBomItemDatas;

};
#endif // !defined(EA_35841C18_1480_44ee_8647_666CA1ADE89F__INCLUDED_)
