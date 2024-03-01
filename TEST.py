import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

# Load the dataset
dset = xr.open_dataset(r'D:\Geo-Environmental\Assignment6\ERA5_Data\download.nc')

# Convert temperature from Kelvin to Celsius and precipitation to mm
dset['t2m'] = dset['t2m'] - 273.15  # Kelvin to Celsius
dset['tp'] = dset['tp'] * 1000  # Convert to mm

# Calculate annual mean precipitation
annual_precip = dset['tp'].resample(time='A').mean()

# Correct: Select the location from the annual_precip DataArray
selected_location = annual_precip.sel(latitude=22.175903554688663, longitude=39.55566155767245, method='nearest')

# Calculate the average annual precipitation for the selected location
average_annual_precip = selected_location.mean()

# Print the average annual precipitation
print(f"Average Annual Precipitation: {average_annual_precip.values} mm")

start_date = dset['time'].min().values
end_date = dset['time'].max().values

# Print the temporal range
print(f"Temporal range: {start_date} to {end_date}")



# Part 3

# Inputs for the fuction from the hourly ERA5 data:
tmin = selected_location['t2m'].resample(time='D').min().values
tmax = selected_location['t2m'].resample(time='D').max().values
tmean = selected_location['t2m'].resample(time='D').mean().values
lat = 22.175903554688663   #Latitude of reservoir
doy = (selected_location['t2m'].resample(time='D').mean().time).dt.dayofyear.values

# Compute the PE using:+
import tools
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)


#Plot the PE time series:
time_index = pd.to_datetime(time.values)
plt.figure(figsize=(10, 6), tight_layout=True)
plt.plot(time_index, pe, label='Potential Evaporation')
plt.xlabel('Date')
plt.ylabel('PE [mm day−1]')
plt.title('Potential Evaporation Time Series')
plt.grid(True)

# Add legend
lines, label = axl.get_legend_handles_labels()
lines2, labels2 = ax2.get_legned_handles_laels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

plt.title('Potential Evaporation Time Series')
plt.grid(True)
# plt.savefig('123', dpi=300)
# plt.show()

pe_eries = pd.Series(pe, index=time_index)
annual_mean_pe = pe_eriesseries.resample('A').mean()
mean_annual_pe = annual_mean_mean_pe.mean()

print("Mean Annual Potential Evaporation:",mean_annual_pe)
