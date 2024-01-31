import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
#opening of each of the CIMP6 netcdf files where dset1 represents 1850-1949, dset2 represents 1950-2014, dset3 represents 2015-2100 ssp119, dset4 represents 2015-2100 ssp245, dset5 represents ssp585
dset1 = xr.open_dataset(r'D:\Geo-Environmental\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc')
dset2 = xr.open_dataset(r'D:\Geo-Environmental\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')
dset3 = xr.open_dataset(r'D:\Geo-Environmental\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc')
dset4 = xr.open_dataset(r'D:\Geo-Environmental\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc')
dset5 = xr.open_dataset(r'D:\Geo-Environmental\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc')


#mean air temperature map for 1850–1900. This takes data from dset1 (1850-1949)
np.mean(dset1['tas'].sel(time=slice('18500101', '19001231')), axis=0)
gr1=np.mean(dset1['tas'].sel(time=slice('18500101', '19001231')), axis=0)

#mean air temperature map for 2071-2100. For the ssp119, ssp245, ssp585

np.mean(dset3['tas'].sel(time=slice('20710101', '21001231')), axis=0)
ssp119=np.mean(dset3['tas'].sel(time=slice('20710101', '21001231')), axis=0)

np.mean(dset4['tas'].sel(time=slice('20710101', '21001231')), axis=0)
ssp245=np.mean(dset4['tas'].sel(time=slice('20710101', '21001231')), axis=0)

np.mean(dset5['tas'].sel(time=slice('20710101', '21001231')), axis=0)
ssp585=np.mean(dset5['tas'].sel(time=slice('20710101', '21001231')), axis=0)

#plots of mean air temperature map for 1850-1949 and 2071-2100 including ssp119, ssp245, ssp585

plt.imshow(gr1)
plt.title('Mean Air Temperature Map 1850-1900')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
cbar = plt.colorbar()
cbar.set_label("Mean Air Temperature")
plt.savefig('gr1.png',dpi=300)

plt.imshow(ssp119)
plt.title('Mean Air Temperature Map 2071-2100 ssp119')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('ssp119.png',dpi=300)

plt.imshow(ssp245)
plt.title('Mean Air Temperature Map 2071-2100 ssp245')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('ssp245.png',dpi=300)

plt.imshow(ssp585)
plt.title('Mean Air Temperature Map 2071-2100 ssp585')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('ssp585.png',dpi=300)

pdb.set_trace()




