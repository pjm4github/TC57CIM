#######################################################
# 
# BlockDispatchInstruction.py
# Python implementation of the Class BlockDispatchInstruction
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:31:54 PM
# Original author: selaost1
# 
#######################################################
from IEC61970.InfIEC61970.EnergyArea.EnergyGroup import EnergyGroup
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.EnergyArea.BlockDispatchOrder import BlockDispatchOrder

class BlockDispatchInstruction(IdentifiedObject):
    m_EnergyGroup= EnergyGroup()

    m_BlockDispatchOrder= BlockDispatchOrder()