"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import pollution_ranking
# Constants

air_quality_index = int(input("Air Quality Index: "))
pollution = pollution_ranking(air_quality_index)
print(pollution)
