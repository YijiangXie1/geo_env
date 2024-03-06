import xarray as xr

# Load the dataset
dset = xr.open_dataset(r'D:\Geo-Environmental\Assignment6\ERA5_Data\download.nc')

# Print the dimensions of the dataset
print(dset.dims)