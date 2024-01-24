import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
dset = xr.open_dataset(r'C:\Users\MIRBA\Downloads\SRTMGL1_NC.003_Data\N21E039.SRTMGL1_NC.nc')
pdb.set_trace()
DEM = np.array(dset.variables['SRTMGL1_DEM'])
dset.close()
pdb.set_trace()
DEM.shape