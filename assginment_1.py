import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import pdb
import xarray as xr 

dset = xr.open_dataset(r'D:\Geo-Environmental Modeling & Analysis\SRTMGL1_NC.003_Data\N21E039.SRTMGL1_NC.nc')

DEM = np.array(dset.variables['SRTMGL1_DEM'])
# save the pic to the local env 
plt.imshow(DEM)
cbar = plt.colorbar()
cbar.set_label('ELevation (m asl)')
plt.savefig('assignment_1.png', dpi=300)

