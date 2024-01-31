

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
#opening of each of the CIMP6 netcdf files where dset represents 1850-1949, dset1 represents 1950-2014, dset2 represents 2015-2100 SSP119, dset3 represents 2015-2100 SSP245, dset4 represents SSP585
dset = xr.open_dataset(r'C:\Users\MIRBA\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc')
dset1 = xr.open_dataset(r'C:\Users\MIRBA\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')
dset2 = xr.open_dataset(r'C:\Users\MIRBA\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc')
dset3 = xr.open_dataset(r'C:\Users\MIRBA\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc')
dset4 = xr.open_dataset(r'C:\Users\MIRBA\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc')


#mean air temperature map for 1850–1900. This takes data from dset (1850-1949)
np.mean(dset['tas'].sel(time=slice('18500101', '19001231')), axis=0)
temp18501900=np.mean(dset['tas'].sel(time=slice('18500101', '19001231')), axis=0)

#mean air temperature map for 2071-2100. For the SSP119, SSP245, SSP585

np.mean(dset2['tas'].sel(time=slice('20710101', '21001231')), axis=0)
temp20712100ssp119=np.mean(dset2['tas'].sel(time=slice('20710101', '21001231')), axis=0)

np.mean(dset3['tas'].sel(time=slice('20710101', '21001231')), axis=0)
temp20712100ssp245=np.mean(dset3['tas'].sel(time=slice('20710101', '21001231')), axis=0)

np.mean(dset4['tas'].sel(time=slice('20710101', '21001231')), axis=0)
temp20712100ssp585=np.mean(dset4['tas'].sel(time=slice('20710101', '21001231')), axis=0)

#plots of mean air temperature map for 1850-1949 and 2071-2100 including ssp119, ssp245, ssp585

plt.imshow(temp18501900)
plt.title('Mean Air Temperature Map 1850-1900')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
cbar = plt.colorbar()
cbar.set_label("Mean Air Temperature")
plt.savefig('1850-1900.png',dpi=300)

plt.imshow(temp20712100ssp119)
plt.title('Mean Air Temperature Map 2071-2100 ssp119')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('2071-2100 SSP119.png',dpi=300)

plt.imshow(temp20712100ssp245)
plt.title('Mean Air Temperature Map 2071-2100 ssp245')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('2071-2100 SSP245.png',dpi=300)

plt.imshow(temp20712100ssp585)
plt.title('Mean Air Temperature Map 2071-2100 ssp585')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('2071-2100 SSP585.png',dpi=300)

pdb.set_trace()