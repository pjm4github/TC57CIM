#######################################################
# 
# Source.py
# Python implementation of the Class Source
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 7:19:42 PM
# 
#######################################################
from enum import Enum


class Source(Enum):
    """Source gives information related to the origin of a value.
    """
    PROCESS = 1
    DEFAULTED = 2
    SUBSTITUTED = 3

