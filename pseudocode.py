
import numpy as np
from matrix_from_xls import matrix_from_xls as mx2D
import constants as cst

# path for csv files
path = 'C:\\Users\\haggertr\\Desktop\\Roy\\Research\\WW2100\\Research\\results2\\files\\'

FileLoc1 = path + 'Irrigation_Amts_Pudding_(various)_Ref_Run0.csv'
Loc1PET2D = mx2D(FileLoc1, 2, cst.days_in_year, cst.day_of_year_oct1)

print Loc1PET2D[0,1:10]
