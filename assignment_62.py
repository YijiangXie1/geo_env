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

# Select the location
selected_location = dset.sel(latitude=22.175903554688663, longitude=39.55566155767245, method='nearest')



# Plotting
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature [°C]', color=color)
ax1.plot(selected_location['time'], selected_location['t2m'], label='T [°C]', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for the precipitation variable
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Precipitation [mm]', color=color)
ax2.plot(selected_location['time'], selected_location['tp'], label='P [mm]', color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Temperature and Precipitation Time Series at Wadi Murwani Reservoir')
fig.tight_layout()
plt.savefig('P1', dpi=300)
#plt.show()

annual_precip = selected_location['tp'].resample(time='A').mean()
print("Average annual prep:", annual_precip)
overall_avg_annual_precip = annual_precip.mean().values
print("Overall average annual precipitation:", overall_avg_annual_precip)

# Part 3

# Inputs for the fuction from the hourly ERA5 data:
tmin = selected_location['t2m'].resample(time='D').min().values
tmax = selected_location['t2m'].resample(time='D').max().values
tmean = selected_location['t2m'].resample(time='D').mean().values
lat = 22.175903554688663   #Latitude of reservoir
doy = (selected_location['time'].resample(time='D').mean().time).dt.dayofyear.values

# Compute the PE using:
import tools
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)


#Plot the PE time series:
time_index = pd.to_datetime(selected_location['time'].resample(time='D').mean().values)
plt.figure(figsize=(10, 6), tight_layout=True)
plt.plot(time_index, pe, label='Potential Evaporation', color='r')
plt.xlabel('Date')
plt.ylabel('PE [mm day−1]')
plt.title('Potential Evaporation Time Series')
plt.grid(True)

# Add legend
lines, label = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, label + labels2, loc='upper left')

plt.title('Potential Evaporation Time Series')
plt.grid(True)
plt.savefig('P2', dpi=300)
# plt.show()



# Assuming the function tools.hargreaves_samani_1982 returns a 2D array

# Flatten the 'pe' array to make it one-dimensional
pe_flat = pe.flatten()

# Create a pandas Series with the 1D array
pe_series = pd.Series(pe_flat, index=time_index.repeat(2)) # time_index needs to be repeated to match the length of the flattened array

# Resample to get annual mean PE
annual_mean_pe = pe_series.resample('A').mean()

# Calculate the mean of the annual means to get mean annual PE
mean_annual_pe = annual_mean_pe.mean()

# Print the mean annual PE in mm per year
print(f"Mean Annual Potential Evaporation: {mean_annual_pe:.2f} mm/year")

