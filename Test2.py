import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
dset = xr.open_dataset(r'D:\Geo-Environmental\Assignment6\ERA5_Data\download.nc')

# 2. Extract relevant variables and convert them to numpy arrays
t2m = np.array(dset.variables['t2m'])
tp = np.array(dset.variables['tp'])
latitude = np.array(dset.variables['latitude'])
longitude = np.array(dset.variables['longitude'])
time_dt = np.array(dset.variables['time'])

# 3. Convert units for temperature and precipitation
t2m = t2m - 273.15  # Kelvin to Celsius
tp = tp * 1000  # m/h to mm/h

# 4. Simplify the dataset if it has four dimensions
if t2m.ndim == 4:
    t2m = np.nanmean(t2m, axis=1)
    tp = np.nanmean(tp, axis=1)

# 5. Create a pandas DataFrame for time series data
df_era5 = pd.DataFrame(index=time_dt)
df_era5['t2m'] = t2m[:,3,2]  # Assuming the third row and second column for the grid cell
df_era5['tp'] = tp[:,3,2]

# 6. Plot the time series
df_era5.plot()
plt.title('Temperature and Precipitation Time Series at Wadi Murwani Reservoir')

plt.savefig('P1', dpi=300)
#plt.show()

# 7. Calculate the average annual precipitation
df_era5.index = pd.to_datetime(df_era5.index)  # Convert index to datetime for resampling
annual_precip = df_era5['tp'].resample('Y').mean() * 24 * 365.25
mean_annual_precip = np.nanmean(annual_precip)

print(f"Mean Annual Precipitation: {mean_annual_precip} mm/year")


# Part 3

# Inputs for the fuction from the hourly ERA5 data:
tmin = df_era5['t2m'].resample('D').min().values
tmax = df_era5['t2m'].resample('D').max().values
tmean = df_era5['t2m'].resample('D').mean().values
lat = 22.175903554688663   #Latitude of reservoir
doy = df_era5['t2m'].resample('D').mean().index.dayofyear

# Compute the PE using:
import tools
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)

#Plot the PE time series:
ts_index = df_era5['t2m'].resample('D').mean().index
plt.figure()
plt.plot(ts_index, pe, label='Potential Evaporation')
plt.xlabel('Time')
plt.ylabel('Potential evaporation (mm d−1)')
plt.title('Potential Evaporation Time Series')
plt.savefig('P2', dpi=300)
plt.show()

# Step 1: Create a DataFrame for the PE data
df_pe = pd.DataFrame(pe, index=ts_index, columns=['PE'])

# Step 2: Convert index to datetime, if not already
df_pe.index = pd.to_datetime(df_pe.index)

# Step 3: Resample to annual time step, sum to get total annual PE, then calculate the mean
annual_pe = df_pe['PE'].resample('Y').sum()
mean_annual_pe = np.nanmean(annual_pe)

print(f"Mean Annual Potential Evaporation: {mean_annual_pe} mm/year")