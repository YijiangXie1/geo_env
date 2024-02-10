import tools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr



df_isd = tools.read_isd_csv(r'D:\Geo-Environmental\Assignment3\41024099999.csv')




plot = df_isd.plot(title="ISD data for Jeddah")
plt.show()



df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values,df_isd['TMP'].values)

df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values,df_isd['RH'].values)

print (df_isd.max())

print (df_isd.idxmax())

print (df_isd.loc[["2023-08-21 10:00:00"]])

df_isd_daily = df_isd.resample('D').mean()

print (df_isd_daily)

plt.figure(figsize=(10, 6))  # Creates a new figure with a specified size
df_isd_daily['HI'].plot(title="Daily Heat Index (HI) Time Series for Jeddah, 2023", color='green')
plt.xlabel('Date')  # Label for the x-axis
plt.ylabel('Heat Index')  # Label for the y-axis

# Save the plot to a file
plt.savefig('HI_Time_Series_2023_Jeddah.png', dpi=300)  # Saves the figure to a file with 300 DPI
plt.close()  # Closes the figure window to free up memory




# Step 1: Apply the projected warming
df_isd['TMP_warmed'] = df_isd['TMP'] + 3

# Step 2: Recalculate the Heat Index with the warmed temperatures
df_isd['HI_warmed'] = tools.gen_heat_index(df_isd['TMP_warmed'].values, df_isd['RH'].values)

# Step 3: Find the increase in the highest HI value
original_highest_HI = df_isd['HI'].max()
warmed_highest_HI = df_isd['HI_warmed'].max()
increase_in_HI = warmed_highest_HI - original_highest_HI

print(f"Original highest HI value: {original_highest_HI}")
print(f"Highest HI value after warming: {warmed_highest_HI}")
print(f"Increase in highest HI value: {increase_in_HI}")

