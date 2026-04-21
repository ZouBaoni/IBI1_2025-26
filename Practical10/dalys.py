# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Switch the working directory to where the csv file is located
os.chdir("c:/Users/闪光/Desktop/Y1-B/IBI/Practical/IBI1_2025-26/Practical10")
# Read the data from the csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show the 3, 4 columns of the first 10 rows
print(dalys_data.iloc[0:10, [2, 3]])

# Extract the DALYs across the first 10 years of Afghanistan
afg = dalys_data[dalys_data["Entity"] == "Afghanistan"].head(10)
afg_dalys = afg["DALYs"]
afg_max_year = afg.loc[afg_dalys.idxmax(), "Year"]
"""
The year with the highest DALYs in Afghanistan is 1998. 
"""

# Show all years of Zimbabwe
zimbabwe = dalys_data[dalys_data["Entity"] == "Zimbabwe"]
print(zimbabwe[["Year"]])
# Find the first and last year of Zimbabwe
zim_first_year = zimbabwe["Year"].min()
zim_last_year = zimbabwe["Year"].max()
""" 
The first year of Zimbabwe for which DALY is recorded is 1990 and the last year is 2019. 
"""

# Extract the data of 2019
data_2019 = dalys_data[dalys_data["Year"] == 2019]
# Compute the Entity with the highest and lowest DALYs in 2019
max_country_2019 = data_2019.loc[data_2019["DALYs"].idxmax(), "Entity"]
min_country_2019 = data_2019.loc[data_2019["DALYs"].idxmin(), "Entity"]
"""
The country with the highest DALYs in 2019 is Lesotho.
The country with the lowest DALYs in 2019 is Singapore.
"""

# Create a plot showing the DALYs over time in minimal country
country_data = dalys_data[dalys_data["Entity"] == min_country_2019]
plt.figure(figsize=(12, 8))
plt.plot(country_data.Year, country_data.DALYs, 'bo-')
plt.title(f"{min_country_2019} DALYs over time", font=dict(size=16))
plt.xlabel("Year", font=dict(size=14))
plt.ylabel("DALYs", font=dict(size=14))
plt.xticks(country_data.Year, rotation=-90, font=dict(size=12))
plt.yticks(font=dict(size=12))
plt.show()


""" Question: Did the DALYs in China and the UK become more similar or less similar over time? """
# Extract the data for China and the UK
cn = dalys_data[dalys_data["Entity"] == "China"]
uk = dalys_data[dalys_data["Entity"] == "United Kingdom"]

# Merge the data for China and the UK on the Year column, Calculate the absolute difference in DALYs
df = pd.merge(cn[["Year", "DALYs"]], uk[["Year", "DALYs"]], on="Year", suffixes=("_CN", "_UK"))
df["difference"] = df["DALYs_CN"] - df["DALYs_UK"] 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Draw a plot showing the DALYs over time for China and the UK
ax1.plot(cn.Year, cn.DALYs, label="China", marker='o')
ax1.plot(uk.Year, uk.DALYs, label="UK", marker='s')
ax1.set_title("(a) DALYs trend: China versus UK", font=dict(size=16))
ax1.set_xlabel("Year", font=dict(size=14))
ax1.set_ylabel("DALYs per capita", font=dict(size=14))
ax1.legend()
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3)

# Draw a plot showing the difference in DALYs over time
ax2.plot(df["Year"], df["difference"], marker='o', color="red", linewidth=2)
ax2.set_title("(b) China - UK DALYs Difference Trend (1990-2019)", font=dict(size=16))
ax2.set_xlabel("Year", font=dict(size=14))
ax2.set_ylabel("Difference (CN - UK)", font=dict(size=14))
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)

# Show the plots
plt.tight_layout()
plt.show()
