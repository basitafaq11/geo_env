import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

# Load the dataset
dset = xr.open_dataset(r'C:\Users\MIRBA\Downloads\ERA5_Data\download.nc')

# Convert temperature from Kelvin to Celsius and precipitation to mm
dset['t2m'] = dset['t2m'] - 273.15  # Kelvin to Celsius
dset['tp'] = dset['tp'] * 1000  # Convert to mm

# Select the location
selected_location = dset.sel(latitude=22.175903554688663, longitude=39.55566155767245, method='nearest')

# Plotting
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature [°C]', color=color)
ax1.plot(selected_location['time'], selected_location['t2m'], label='T [°C]', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for the precipitation variable
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Precipitation [mm]', color=color)
ax2.plot(selected_location['time'], selected_location['tp'], label='P [mm]', color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Temperature and Precipitation Time Series at Wadi Murwani Reservoir')
fig.tight_layout()
#plt.savefig('Final one', dpi=300)
#plt.show()

annual_precip = selected_location['tp'].resample(time='A').mean()
print("Average annual prep:", annual_precip)
overall_avg_annual_precip = annual_precip.mean().values
print("Overall average annual precipitation:", overall_avg_annual_precip)





# Part 3: Calculation of Potential Evaporation (PE)



# Inputs for the function from the hourly ERA5 data:
tmin = selected_location['t2m'].resample(time='D').min().values
tmax = selected_location['t2m'].resample(time='D').max().values
tmean = selected_location['t2m'].resample(time='D').mean().values
lat = 22.176389  # Latitude of Wadi Murwani reservoir
doy = selected_location['time'].resample(time='D').mean().dt.dayofyear.values

# Compute PE
import tools
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)

# Plot the PE time series
time_index = pd.to_datetime(selected_location['time'].resample(time='D').mean().values)
plt.figure(figsize=(10, 6), tight_layout=True)
plt.plot(time_index, pe, label='Potential Evaporation')
plt.xlabel('Date')
plt.ylabel('PE [mm day−1]')

# Add legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')


plt.title('Potential Evaporation Time Series')
plt.grid(True)
# plt.savefig('123', dpi=300)
# plt.show()



# mean annual PE in mm year−1
pe_series = pd.Series(pe[:, 0], index=time_index)
annual_mean_pe = pe_series.resample('A').mean()
mean_annual_pe = annual_mean_pe.mean()

# Print the mean annual PE
print("Mean Annual PE:", mean_annual_pe)


# Convert PE data to a Pandas Series for resampling
pe_series = pd.Series(pe[:, 0], index=time_index[:len(pe)])

# Resample PE annually and calculate the mean
annual_mean_pe = pe_series.resample('A').mean()
mean_annual_pe = annual_mean_pe.mean()

print(annual_mean_pe)