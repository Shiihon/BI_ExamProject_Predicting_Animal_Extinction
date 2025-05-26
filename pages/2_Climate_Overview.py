import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Load merged dataset
@st.cache_data
def load_data():
    return pd.read_csv("Data/Cleaned_Data/cleaned_climate_data.csv")

df = load_data()
#st.write(df.columns.tolist())

# Page title and introduction
st.title("Data Overview: Climate Data")
st.markdown("""
This dataset captures average regional temperatures from 2014–2023 across five continents.
It highlights trends in warming and allows us to quantify the environmental pressure animals may be facing.
Each region’s yearly data is used to calculate a recent average temperature, which feeds into our extinction analysis.
""")

# Preview
st.subheader("Preview of Merged Dataset")
st.dataframe(df.head())
st.markdown("---")

st.subheader("Analyzing Climate Data")
# Extract year columns and global temperature averages
year_cols = [col for col in df.columns if col.endswith("-07")]
global_means = df[year_cols].mean()
years = [int(col.split("-")[0]) for col in year_cols]
temps = global_means.values

# Prepare xtick labels: every 5th year + last year
xtick_years = [year for i, year in enumerate(years) if i % 5 == 0]
if years[-1] not in xtick_years:
    xtick_years.append(years[-1])

# Plot
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(years, temps, label="Global Mean Temp", color="darkorange")

# Highlight 1956 if present
if 1956 in years:
    idx_1956 = years.index(1956)
    temp_1956 = temps[idx_1956]
    ax.scatter(1956, temp_1956, color="red", zorder=5)
    ax.annotate("Drop in 1956", (1956, temp_1956),
                textcoords="offset points", xytext=(0, 10),
                ha='center', color='red')

ax.set_title("Global Average Temperature Over Time", fontsize=17, loc="center")
ax.set_xlabel("Year", fontsize=16)
ax.set_ylabel("Temperature (°C)", fontsize=16)
ax.set_xticks(xtick_years)
ax.tick_params(axis='x', rotation=45)
ax.grid(True)
ax.legend()
plt.tight_layout()

st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This line chart shows how the global average temperature has changed from **1901 to 2023**.

- **Overall upward trend**: The temperature has steadily increased over the decades, especially since the 1980s.
- **Noticeable drop in 1956**: There’s a short-term dip around 1956, possibly due to natural variability or measurement changes.
- **Sharp rise post-2000**: The rise in temperature becomes much steeper in recent decades — a clear sign of accelerating climate change.
- **2023 is the warmest**: The final year on the chart marks the highest recorded average temperature, emphasizing the urgency of the climate crisis.

> This steady warming trend supports the need to consider climate data when analyzing extinction risk and habitat vulnerability.
""")

st.markdown("---")

# Filter only July columns from 2004 to 2023
july_cols = [col for col in df.columns if col.endswith("-07") and 2004 <= int(col.split("-")[0]) <= 2023]

# Add 'Region' column if it's not the index already
if 'Region' not in df.columns:
    df.reset_index(inplace=True)

# Group by Region and calculate mean per year
region_means = df.groupby("Region")[july_cols].mean()

# Transpose for plotting
df_plot = region_means.T
df_plot.index = df_plot.index.str.split("-").str[0]  # Convert '2004-07' to '2004'
df_plot.index.name = "Year"

# Convert index to int for sorting
df_plot.index = df_plot.index.astype(int)

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
for region in df_plot.columns:
    ax.plot(df_plot.index, df_plot[region], label=region)

ax.set_title("Average July Temperature per Region (2004–2023)", fontsize=17)
ax.set_xlabel("Year", fontsize=16)
ax.set_ylabel("Temperature (°C)", fontsize=16)
ax.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=16)  # Push legend outside
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**
            
This line chart shows the **average July temperature** across regions from **2004 to 2023**.

- **Africa, Oceania, and Asia** have the **highest July temperatures**, consistently above 20°C.
- **Europe and the Americas** show stable but slightly increasing trends, typically around 18–22°C.
- **The Arctic** stays cooler, but we still see **gradual warming** in recent years.
- **Antarctica** remains far below freezing — but even there, a **slight warming trend** is visible.

All regions are showing signs of rising temperatures, reinforcing the broader patterns of global climate change.
""")

st.markdown("---")

# Filter to only July columns from 2004 to 2023
july_cols = [col for col in df.columns if col.endswith("-07") and 2004 <= int(col.split("-")[0]) <= 2023]

# Group by region and calculate the average per year
df_region_temp = df.groupby("Region")[july_cols].mean()

# Calculate year-over-year temperature change (by region)
df_diff = df_region_temp.diff(axis=1)

# Step 4: Plot
fig, ax = plt.subplots(figsize=(12, 6))
df_diff.T.plot(ax=ax)
ax.set_title("Year-over-Year Temperature Change per Region", fontsize=17)
ax.set_xlabel("Year", fontsize=16)
ax.set_ylabel("ΔTemp (°C)", fontsize=16)
ax.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This line chart shows how much the average July temperature **changed from year to year** in each region between **2004 and 2023**.

- **Fluctuations are common**: All regions show up-and-down swings, highlighting how variable climate patterns are from year to year.
- **Some years show sharp jumps** — like Europe in 2012 or Arctic in 2016 — indicating possible heatwaves or climate anomalies.
- **No region stays completely stable**: Even "mild" regions like Oceania and Africa experience changes of ±0.5°C or more some years.
- **Short-term change ≠ long-term trend**: While this chart shows variability, it doesn’t capture the long-term rise — that’s in the overall temperature trend chart.

This kind of chart is useful to detect **climate volatility**, which may affect ecosystems and species differently depending on their sensitivity.
""")

st.markdown("---")

# Filter only July columns (monthly climate data)
year_cols = [col for col in df.columns if col.endswith("-07")]

# Prepare X (years as ints) and y (global average temperature)
X_years = np.array([int(col.split("-")[0]) for col in year_cols]).reshape(-1, 1)
y_global = df[year_cols].mean().values

# Train linear regression model
model = LinearRegression()
model.fit(X_years, y_global)

# Predict future years: 2024–2030
future_years = np.array(range(2024, 2031)).reshape(-1, 1)
future_preds = model.predict(future_years)

# Predict entire regression line: 1901–2030
full_years = np.append(X_years.flatten(), future_years.flatten()).reshape(-1, 1)
full_preds = model.predict(full_years)

fig, ax = plt.subplots(figsize=(12, 5))

# Plot real data
ax.plot(X_years.flatten(), y_global, label="Global Actual (Mean)", color="orange")

# Plot future predictions
ax.plot(future_years.flatten(), future_preds, label="Forecast (2024–2030)",
        linestyle="--", color="red", linewidth=2)

# Plot full regression line
ax.plot(full_years.flatten(), full_preds, label="Linear Regression (Full)",
        linestyle="--", color="blue")

ax.set_title("Global Average Temperature Forecast (Linear Regression)", fontsize=17)
ax.set_xlabel("Year", fontsize=16)
ax.set_ylabel("Temperature (°C)", fontsize=16)
ax.grid(True)
ax.legend()
plt.tight_layout()

st.pyplot(fig)

st.markdown("""
### **What we can observe from the forecast chart:**

This forecast uses a simple linear regression model to estimate the **global average temperature** from historical data (1901–2023) and project it up to **2030**.

- **Consistent upward trend**: The orange line (actual mean temperature) shows a clear and steady increase over the past century.
- **Linear forecast (2024–2030)**: The red dashed line projects temperatures to continue rising if current trends persist.
- **Blue regression line**: Represents the full fitted trend line, confirming a long-term warming pattern.
- **Prediction beyond 2023**: If this simple model holds, we expect temperatures to keep climbing — adding urgency to climate awareness and mitigation.

While the model is basic, it reinforces what more advanced models also suggest: **our planet is steadily warming**, and we can visualize that clearly with even simple predictive tools.
""")

st.markdown("""
---  
### **Final Thoughts on Climate Data Trends**

This climate analysis highlights the ongoing rise in global temperatures and its regional impact.  
The patterns we observed offer several clear insights:

- **Global temperatures have risen steadily** since the early 1900s — with the steepest climb happening after the year 2000.
- **Year-over-year regional shifts** show short-term variability, but the overall direction is consistently upward.
- **Asia and Africa** not only house many vulnerable species, but also show **strong warming patterns**, indicating a dual pressure on biodiversity.
- Our **simple forecast model** projects continued warming through **2030**, aligning with international climate concerns.

These findings emphasize that climate change is **not a distant threat — it's happening now**.  
Understanding these temperature trends is crucial to predicting future challenges for ecosystems, species survival, and global stability.  
""")
