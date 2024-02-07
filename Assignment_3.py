import tools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

# Read the data from the provided CSV file using a custom function from the 'tools' module
df_isd = tools.read_isd_csv(r'C:\Users\MIRBA\geo_env\41024099999.csv')

# Plot the data from the DataFrame with a title specifying it's ISD data for Jeddah
plot = df_isd.plot(title="ISD data for Jeddah")
# Optionally, if running this code in a Jupyter Notebook, the plot can be displayed using plt.show()

# Calculate relative humidity (RH) from dew point (DEW) and temperature (TMP) using a custom function from the 'tools' module
df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values,df_isd['TMP'].values)

# Calculate Heat Index (HI) from temperature (TMP) and relative humidity (RH) using a custom function from the 'tools' module
df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values, df_isd['RH'].values)

# Print the maximum values of each column in the DataFrame
print(df_isd.max())

# Print the index (date and time) where the maximum value occurs for each column in the DataFrame
print(df_isd.idxmax())

# Print the row corresponding to the specific date and time "2023-08-21 10:00:00" in the DataFrame
print(df_isd.loc[["2023-08-21 10:00:00"]])

# Resample the DataFrame to calculate daily mean values
df_isd_daily = df_isd.resample("D").mean()

# Print the resampled DataFrame showing daily mean values
print(df_isd_daily)

# Plot the daily Heat Index values from the resampled DataFrame
plt.figure(figsize=(10, 6))
plt.plot(df_isd_daily.index, df_isd_daily['HI'], marker='o', color='red')
plt.title('Daily Heat Index')
plt.xlabel('Date')
plt.ylabel('Heat Index')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
#plt.savefig('Figure.png',dpi=300)

original_hi_max = df_isd['HI'].max()

# Projected warming
projected_warming = 3  # in degrees Celsius
# Apply projected warming to air temperature data
df_isd['TMP_adjusted'] = df_isd['TMP'] + projected_warming

# Recalculate Heat Index with adjusted temperature
df_isd['HI_adjusted'] = tools.gen_heat_index(df_isd['TMP_adjusted'].values, df_isd['RH'].values)

# Find the highest Heat Index value after adjustment
adjusted_hi_max = df_isd['HI_adjusted'].max()

# Calculate the increase in the highest Heat Index value
increase_in_hi_max = adjusted_hi_max - original_hi_max

print("Original highest HI value:", original_hi_max)
print("Highest HI value after adjustment:", adjusted_hi_max)
print("Increase in highest HI value:", increase_in_hi_max)