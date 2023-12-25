from enum import Enum


class CurveStyle(Enum):
	"""
	Style or shape of curve.
	"""
	# /**
	#  * The Y-axis values are assumed constant until the next curve point and prior to
	#  * the first curve point.
	#  */
	CONSTANT_Y_VALUE = 1
	# /**
	#  * The Y-axis values are assumed to be a straight line between values.  Also known
	#  * as linear interpolation.
	#  */
	STRAIGHT_LINE_Y_VALUES = 2
