# NHS-Waiting-Time-Analysis
Data analysis project exploring NHS waiting time trends using Python. Includes data cleaning, transformation, and exploratory analysis to assess performance over time and identify key bottlenecks in patient care pathways.


```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("nhs_rtt_waiting_times_2021_2025.csv")

df.head()


```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>period</th>
      <th>year</th>
      <th>month</th>
      <th>provider_org_code</th>
      <th>provider_org_name</th>
      <th>commissioner_org_code</th>
      <th>commissioner_org_name</th>
      <th>sub_icb_org_code</th>
      <th>sub_icb_org_name</th>
      <th>rtt_part_type</th>
      <th>...</th>
      <th>week_096</th>
      <th>week_097</th>
      <th>week_098</th>
      <th>week_099</th>
      <th>week_100</th>
      <th>week_101</th>
      <th>week_102</th>
      <th>week_103</th>
      <th>week_104</th>
      <th>source_file</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>A0C5S</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>QR1</td>
      <td>GLOUCESTERSHIRE STP</td>
      <td>18C</td>
      <td>NHS HEREFORDSHIRE AND WORCESTERSHIRE CCG</td>
      <td>Part_1A</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20210228-RTT-FEBRUARY-2021-full-extract.csv</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>A0C5S</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>QR1</td>
      <td>GLOUCESTERSHIRE STP</td>
      <td>18C</td>
      <td>NHS HEREFORDSHIRE AND WORCESTERSHIRE CCG</td>
      <td>Part_1B</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20210228-RTT-FEBRUARY-2021-full-extract.csv</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>A0C5S</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>QR1</td>
      <td>GLOUCESTERSHIRE STP</td>
      <td>18C</td>
      <td>NHS HEREFORDSHIRE AND WORCESTERSHIRE CCG</td>
      <td>Part_2</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20210228-RTT-FEBRUARY-2021-full-extract.csv</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>A0C5S</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>QR1</td>
      <td>GLOUCESTERSHIRE STP</td>
      <td>18C</td>
      <td>NHS HEREFORDSHIRE AND WORCESTERSHIRE CCG</td>
      <td>Part_2A</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20210228-RTT-FEBRUARY-2021-full-extract.csv</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>A0C5S</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>QR1</td>
      <td>GLOUCESTERSHIRE STP</td>
      <td>18C</td>
      <td>NHS HEREFORDSHIRE AND WORCESTERSHIRE CCG</td>
      <td>Part_3</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20210228-RTT-FEBRUARY-2021-full-extract.csv</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 128 columns</p>
</div>




```python
# -----------------------------------------------
df.columns
```




    Index(['period', 'year', 'month', 'provider_org_code', 'provider_org_name',
           'commissioner_org_code', 'commissioner_org_name', 'sub_icb_org_code',
           'sub_icb_org_name', 'rtt_part_type',
           ...
           'week_096', 'week_097', 'week_098', 'week_099', 'week_100', 'week_101',
           'week_102', 'week_103', 'week_104', 'source_file'],
          dtype='object', length=128)




```python
# -----------------------------------------------
columns_needed = [
    "period",
    "year",
    "month",
    "provider_org_name",
    "rtt_part_type",
    "treatment_function_name",
    "total_waiting",
    "pct_within_18_weeks"
]

df = df[columns_needed]

df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>period</th>
      <th>year</th>
      <th>month</th>
      <th>provider_org_name</th>
      <th>rtt_part_type</th>
      <th>treatment_function_name</th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_1A</td>
      <td>Ophthalmology</td>
      <td>6.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_1B</td>
      <td>Ophthalmology</td>
      <td>6.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_2</td>
      <td>Ophthalmology</td>
      <td>49.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_2A</td>
      <td>Ophthalmology</td>
      <td>13.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_3</td>
      <td>Ophthalmology</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# -----------------------------------------------
# Check for missing values in each column

# df.isnull() -> returns True/False for missing values
# .sum() -> counts how many missing values per column
df.isnull().sum()
```




    period                          0
    year                            0
    month                           0
    provider_org_name               0
    rtt_part_type                   0
    treatment_function_name         0
    total_waiting              103642
    pct_within_18_weeks        109328
    dtype: int64




```python
# -----------------------------------------------
# Observations on missing values

# I noticed that:
# - total_waiting has many missing values
# - pct_within_18_weeks also has many missing values

# This could mean:
# - Data was not recorded for some providers
# - Some categories (like RTT parts) may not require these values
# - Or data collection was incomplete for certain periods

# Important:
# We should NOT blindly delete or fill these yet
# First, we need to understand WHY they are missing

df.isnull().sum()
```




    period                          0
    year                            0
    month                           0
    provider_org_name               0
    rtt_part_type                   0
    treatment_function_name         0
    total_waiting              103642
    pct_within_18_weeks        109328
    dtype: int64




```python
# -----------------------------------------------


df[df['total_waiting'].isnull()].head()

```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>period</th>
      <th>year</th>
      <th>month</th>
      <th>provider_org_name</th>
      <th>rtt_part_type</th>
      <th>treatment_function_name</th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_3</td>
      <td>Ophthalmology</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_3</td>
      <td>Ophthalmology</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_3</td>
      <td>Ophthalmology</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_3</td>
      <td>Ophthalmology</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2021-02</td>
      <td>2021</td>
      <td>2</td>
      <td>SPAMEDICA GLOUCESTER</td>
      <td>Part_3</td>
      <td>Ophthalmology</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# -----------------------------------------------
# Insight from investigation of missing values

# I observed that missing values in 'total_waiting' and
# 'pct_within_18_weeks' occur mainly when rtt_part_type = 'Part_3'

# This suggests the missing data is NOT random
# It may be that these metrics are not applicable or not recorded for Part_3

# Therefore, missing values should be treated carefully
# rather than immediately removing or filling them

# -----------------------------------------------
```


```python
# Check missing values by RTT part type

df.groupby('rtt_part_type')[['total_waiting', 'pct_within_18_weeks']]\
  .apply(lambda x: x.isnull().sum())

```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>rtt_part_type</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Part_1A</th>
      <td>13</td>
      <td>654</td>
    </tr>
    <tr>
      <th>Part_1B</th>
      <td>13</td>
      <td>879</td>
    </tr>
    <tr>
      <th>Part_2</th>
      <td>0</td>
      <td>2321</td>
    </tr>
    <tr>
      <th>Part_2A</th>
      <td>0</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Part_3</th>
      <td>103613</td>
      <td>103613</td>
    </tr>
    <tr>
      <th>RTT Part Type</th>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python

# -----------------------------------------------
# Final insight on missing values

# Missing values are heavily concentrated in rtt_part_type = 'Part_3'
# This confirms that the missing data is NOT random

# It is likely that 'total_waiting' and 'pct_within_18_weeks'
# are not recorded or not applicable for Part_3 cases

# Therefore, Part_3 may need to be treated separately in analysis
```


```python
# -----------------------------------------------
# Convert 'period' column to datetime format
# This allows time-based analysis like trends over months/years

df['period'] = pd.to_datetime(df['period'], format='%Y-%m')
# Check data types to confirm conversion
df.dtypes
```




    period                     datetime64[ns]
    year                                int64
    month                               int64
    provider_org_name                  object
    rtt_part_type                      object
    treatment_function_name            object
    total_waiting                     float64
    pct_within_18_weeks               float64
    dtype: object




```python
# ===============================
# START OF ANALYSIS
# ===============================

# Objective:
# Analyse NHS waiting times to understand:
# - Trends over time (2021-2025)
# - Performance against targets
# - Areas under pressure

# From this point, the analysis phase begins after data cleaning


```


```python
# ===============================
# Question 1. How have NHS waiting times changed over time?
# ===============================

# Group data by time (period)
# Calculate average waiting metrics per month

df_trend = df.groupby('period')[['total_waiting', 'pct_within_18_weeks']].mean()

# View first few rows
df_trend.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>period</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-02-01</th>
      <td>103.603853</td>
      <td>64.506451</td>
    </tr>
    <tr>
      <th>2021-03-01</th>
      <td>106.205666</td>
      <td>63.275534</td>
    </tr>
    <tr>
      <th>2021-04-01</th>
      <td>115.407233</td>
      <td>64.968629</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plot total waiting trend
df_trend['total_waiting'].plot()

plt.title('NHS Total Waiting Trend Over Time')
plt.xlabel('Period')
plt.ylabel('Total Waiting')
plt.show()


```


    
![png](output_12_0.png)
    



```python
# -----------------------------------------------
# Plot performance against 18-week target
df_trend['pct_within_18_weeks'].plot()

plt.title('Percentage Within 18 Weeks Over Time')
plt.xlabel('Period')
plt.ylabel('Percentage')
plt.show()
```


    
![png](output_13_0.png)
    



```python
# ===============================
# INSIGHT: NHS PERFORMANCE OVER TIME
# ===============================

# The total waiting list shows a clear upward trend from Feb to April 2021,
# indicating that the NHS backlog is increasing over time.

# This suggests growing pressure on the healthcare system and rising demand.

# The percentage of patients treated within 18 weeks remains low (~63-65%),
# which is significantly below the NHS target of 92%.

# Although there is a slight improvement in April, overall performance
# remains consistently below the expected standard.

# Conclusion:
# The NHS is not meeting its target and waiting times appear to be worsening,
# highlighting a potential capacity or demand issue.

# Note: Analysis excludes missing-value bias from RTT Part_3 where applicable

# Question 2 : Which Hospital are performing worst against targets?

df_hospital = df.groupby('provider_org_name')[['total_waiting', 'pct_within_18_weeks']].mean()

df_hospital.head()

```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>provider_org_name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AIREDALE NHS FOUNDATION TRUST</th>
      <td>50.394768</td>
      <td>76.424823</td>
    </tr>
    <tr>
      <th>ALDER HEY CHILDREN'S NHS FOUNDATION TRUST</th>
      <td>244.924242</td>
      <td>81.464974</td>
    </tr>
    <tr>
      <th>ANGLIA COMMUNITY EYE SERVICE LTD</th>
      <td>407.916667</td>
      <td>91.600833</td>
    </tr>
    <tr>
      <th>ASHFORD AND ST PETER'S HOSPITALS NHS FOUNDATION TRUST</th>
      <td>102.995025</td>
      <td>69.920838</td>
    </tr>
    <tr>
      <th>ASHTEAD HOSPITAL</th>
      <td>13.617329</td>
      <td>60.044801</td>
    </tr>
  </tbody>
</table>
</div>




```python
# -----------------------------------------------
worst_performing = df_hospital.sort_values('pct_within_18_weeks').head(10)

worst_performing
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>provider_org_name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>NUFFIELD HEALTH, CAMBRIDGE HOSPITAL</th>
      <td>4.216867</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>NEWMEDICA - WINTERTON</th>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>BMI - THE SANDRINGHAM HOSPITAL</th>
      <td>2.666667</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>NUFFIELD HEALTH, SHREWSBURY HOSPITAL</th>
      <td>80.847458</td>
      <td>0.287797</td>
    </tr>
    <tr>
      <th>NUFFIELD HEALTH, TAUNTON HOSPITAL</th>
      <td>23.736842</td>
      <td>6.062368</td>
    </tr>
    <tr>
      <th>BMI - THE HARBOUR HOSPITAL</th>
      <td>8.277778</td>
      <td>7.489444</td>
    </tr>
    <tr>
      <th>BMI - THE SHELBURNE HOSPITAL</th>
      <td>4.310345</td>
      <td>7.698448</td>
    </tr>
    <tr>
      <th>NUFFIELD HEALTH, BRIGHTON HOSPITAL</th>
      <td>58.139535</td>
      <td>18.491750</td>
    </tr>
    <tr>
      <th>NUFFIELD HEALTH, WESSEX HOSPITAL</th>
      <td>10.144928</td>
      <td>22.698116</td>
    </tr>
    <tr>
      <th>NUFFIELD HEALTH, PLYMOUTH HOSPITAL</th>
      <td>20.097222</td>
      <td>23.653496</td>
    </tr>
  </tbody>
</table>
</div>




```python
# -----------------------------------------------
highest_waiting = df_hospital.sort_values('total_waiting', ascending=False).head(10)

highest_waiting

```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>provider_org_name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>SUSSEX COMMUNITY DERMATOLOGY SERVICE</th>
      <td>1565.047619</td>
      <td>98.855714</td>
    </tr>
    <tr>
      <th>KENT COMMUNITY HEALTH NHS FOUNDATION TRUST</th>
      <td>1481.454545</td>
      <td>99.567727</td>
    </tr>
    <tr>
      <th>NOTTINGHAM CITYCARE PARTNERSHIP</th>
      <td>1387.714286</td>
      <td>99.221429</td>
    </tr>
    <tr>
      <th>SIRONA CARE &amp; HEALTH</th>
      <td>1001.000000</td>
      <td>85.895000</td>
    </tr>
    <tr>
      <th>PRIMARY INTEGRATED COMMUNITY SERVICES LTD</th>
      <td>881.222222</td>
      <td>81.335556</td>
    </tr>
    <tr>
      <th>OLDHAM INTEGRATED CARE CENTRE</th>
      <td>711.000000</td>
      <td>97.916667</td>
    </tr>
    <tr>
      <th>FIRST COMMUNITY HEALTH AND CARE CIC</th>
      <td>471.000000</td>
      <td>98.621667</td>
    </tr>
    <tr>
      <th>BROMLEY HEALTHCARE</th>
      <td>436.777778</td>
      <td>73.021111</td>
    </tr>
    <tr>
      <th>CORNWALL PARTNERSHIP NHS FOUNDATION TRUST</th>
      <td>425.833333</td>
      <td>99.663333</td>
    </tr>
    <tr>
      <th>PROVIDE</th>
      <td>423.166667</td>
      <td>61.186667</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ==========================================
# Insight: Hospital Performance Analysis
# ==========================================

# Worst performing hospitals:
# Hospitals with the lowest 'pct_within_18_weeks' are performing poorly
# Some hospitals have values close to 0%, meaning almost no patients are treated within target time

# Highest waiting hospitals:
# Some providers have very high 'total_waiting' numbers (e.g. >1000)
# This indicates high demand or capacity pressure

# Key observation:
# High waiting numbers do NOT always mean poor performance
# Some hospitals with high demand still maintain high % within 18 weeks

# Conclusion:
# Performance must be evaluated using BOTH:
# - total_waiting (demand pressure)
# - pct_within_18_weeks (efficiency/performance)


```


```python
# ==========================================
# QUESTION 3: Which specialties are under pressure?
# ==========================================

# Objective:
# Identify which treatment areas (specialties) have the highest waiting times

# Key metrics:
# - total_waiting -> demand/pressure per specialty
# - pct_within_18_weeks -> performance level

# Approach:
# 1. Group data by treatment_function_name (specialty)
# 2. Calculate average waiting metrics per specialty
# 3. Identify:
#    - Specialties with highest waiting lists
#    - Specialties with lowest performance

# Expected insight:
# - Identify overloaded departments
# - Highlight pressure areas within NHS services

# -----------------------------------------------
# Group by specialty
df_specialty = df.groupby('treatment_function_name')[['total_waiting', 'pct_within_18_weeks']].mean()

df_specialty.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>treatment_function_name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cardiology</th>
      <td>55.186532</td>
      <td>73.079071</td>
    </tr>
    <tr>
      <th>Cardiology Service</th>
      <td>66.404613</td>
      <td>74.755229</td>
    </tr>
    <tr>
      <th>Cardiothoracic Surgery</th>
      <td>17.884907</td>
      <td>70.709399</td>
    </tr>
    <tr>
      <th>Cardiothoracic Surgery Service</th>
      <td>16.152459</td>
      <td>69.970812</td>
    </tr>
    <tr>
      <th>Dermatology</th>
      <td>75.310407</td>
      <td>70.296302</td>
    </tr>
  </tbody>
</table>
</div>




```python
# -----------------------------------------------
# Specialties with highest waiting lists (most pressure)
top_waiting_specialties = df_specialty.sort_values('total_waiting', ascending=False).head(10)

top_waiting_specialties
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>treatment_function_name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Oral Surgery</th>
      <td>292.438380</td>
      <td>55.819918</td>
    </tr>
    <tr>
      <th>Total</th>
      <td>234.115700</td>
      <td>62.412647</td>
    </tr>
    <tr>
      <th>Oral Surgery Service</th>
      <td>216.338109</td>
      <td>55.482314</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>109.713880</td>
      <td>69.413178</td>
    </tr>
    <tr>
      <th>Ophthalmology Service</th>
      <td>98.747879</td>
      <td>69.547016</td>
    </tr>
    <tr>
      <th>Dermatology Service</th>
      <td>91.214141</td>
      <td>74.607849</td>
    </tr>
    <tr>
      <th>Ophthalmology</th>
      <td>84.647536</td>
      <td>66.932536</td>
    </tr>
    <tr>
      <th>Other - Medical Services</th>
      <td>82.886843</td>
      <td>77.575998</td>
    </tr>
    <tr>
      <th>Trauma and Orthopaedic Service</th>
      <td>82.843087</td>
      <td>53.309952</td>
    </tr>
    <tr>
      <th>Other - Surgical Services</th>
      <td>82.440172</td>
      <td>63.005300</td>
    </tr>
  </tbody>
</table>
</div>




```python
# -----------------------------------------------
# Specialties with lowest performance (worst at meeting target)
worst_specialties = df_specialty.sort_values('pct_within_18_weeks').head(10)

worst_specialties
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_waiting</th>
      <th>pct_within_18_weeks</th>
    </tr>
    <tr>
      <th>treatment_function_name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Trauma &amp; Orthopaedics</th>
      <td>71.770765</td>
      <td>52.012643</td>
    </tr>
    <tr>
      <th>Ear, Nose &amp; Throat (ENT)</th>
      <td>67.901661</td>
      <td>52.491391</td>
    </tr>
    <tr>
      <th>Trauma and Orthopaedic Service</th>
      <td>82.843087</td>
      <td>53.309952</td>
    </tr>
    <tr>
      <th>Ear Nose and Throat Service</th>
      <td>81.042238</td>
      <td>54.738940</td>
    </tr>
    <tr>
      <th>Oral Surgery Service</th>
      <td>216.338109</td>
      <td>55.482314</td>
    </tr>
    <tr>
      <th>Oral Surgery</th>
      <td>292.438380</td>
      <td>55.819918</td>
    </tr>
    <tr>
      <th>Plastic Surgery</th>
      <td>30.267419</td>
      <td>56.485919</td>
    </tr>
    <tr>
      <th>Plastic Surgery Service</th>
      <td>35.488979</td>
      <td>57.792694</td>
    </tr>
    <tr>
      <th>General Surgery</th>
      <td>67.819132</td>
      <td>57.936287</td>
    </tr>
    <tr>
      <th>General Surgery Service</th>
      <td>74.706076</td>
      <td>58.645145</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ============================================
# Insight: Specialty Pressure Analysis
# ============================================

# High-demand specialties:
# - Oral Surgery and related services show the highest waiting volumes
# - Ophthalmology and Dermatology also have significant patient backlogs

# Worst-performing specialties:
# - Trauma & Orthopaedics (~52%)
# - ENT (~52%)
# - Oral Surgery (~55%)
# - General Surgery (~57%)

# Critical insight:
# Some specialties appear in BOTH high waiting and low performance groups

# This indicates:
# - High demand + poor efficiency = system pressure
# - These areas may be experiencing capacity constraints

# Conclusion:
# Oral Surgery, Trauma & Orthopaedics, and ENT are key pressure points
# in the NHS and may require prioritised resource allocation

# ============================================
# Question 4. Does higher demand lead to worse performance?
# ============================================
```


```python
# Group data by hospital
df_demand = df.groupby('provider_org_name')[['total_waiting', 'pct_within_18_weeks']].mean()


# Check relationship (correlation)
correlation = df_demand['total_waiting'].corr(df_demand['pct_within_18_weeks'])

correlation
```




    np.float64(0.08396117829967882)




```python
# -----------------------------------------------
# Scatter plot: Demand vs Performance
plt.scatter(df_demand['total_waiting'], df_demand['pct_within_18_weeks'])

plt.xlabel('Total Waiting (Demand)')
plt.ylabel('Percentage Within 18 Weeks (Performance)')
plt.title('Demand vs Performance Relationship')

plt.show()
```


    
![png](output_23_0.png)
    



```python
# ============================================
# Insight: Demand vs Performance (Visual Analysis)
# ============================================

# The scatter plot shows a wide spread of performance values across all levels of demand

# Key observations:
# - Most hospitals are clustered at lower waiting levels (0-300),
#   but performance varies significantly (from ~20% to ~100%)
# - There is no clear upward or downward trend in the data points
# - Some hospitals with very high waiting volumes still achieve high performance

# Interpretation:
# There is no strong visual relationship between demand and performance

# Conclusion:
# Demand alone does not determine NHS performance.
# Differences in performance are likely influenced by operational efficiency,
# resource allocation, or internal management practices


```


```python
# ============================================
# KPI Analysis:Is the NHS meeting its 18-Week Target (92%)
# ============================================

# Calculate average performance over time
df_kpi = df.groupby('period')['pct_within_18_weeks'].mean()

df_kpi
```




    period
    2021-02-01    64.506451
    2021-03-01    63.275534
    2021-04-01    64.968629
    Name: pct_within_18_weeks, dtype: float64




```python
# -----------------------------------------------
plt.plot(df_kpi.index, df_kpi.values)

# Add NHS target line
plt.axhline(y=92)

plt.xlabel('Time')
plt.ylabel('Percentage Within 18 Weeks')
plt.title('NHS Performance vs 92% Target')

plt.show()

```


    
![png](output_26_0.png)
    



```python

# ============================================
# Final Insight: NHS Performance vs 92% Target
# ============================================

# The chart compares NHS performance against the 92% 18-week target

# Key observations:
# - Actual performance remains between ~63% and 65% over time
# - The NHS target of 92% is significantly higher than observed values
# - There is a clear and persistent gap between performance and the target

# Interpretation:
# The NHS is consistently failing to meet its 18-week treatment target

# Trend insight:
# - Performance remains relatively stable but low
# - No strong upward trend indicating recovery or improvement

# Business impact:
# - Indicates a sustained backlog of patients
# - Suggests ongoing capacity and efficiency challenges
# - Highlights pressure on healthcare services and patient care delays

# Final conclusion:
# The NHS is not meeting its key performance target,
# confirming long-term systemic pressure within the healthcare system
```


```python
# ============================================
# Final Recommendations: Addressing NHS Waiting Times
# ============================================

# Based on the analysis, the NHS is experiencing sustained pressure due to
# high demand, capacity constraints, and performance gaps.

# Recommended actions:

# 1. Increase Workforce Capacity
# - Recruit more healthcare professionals, including nurses and specialists
# - Expand training programmes and fast-track experienced healthcare students
# - Improve staff retention through better working conditions

# 2. Expand Community-Based Care
# - Enable pharmacies to manage minor conditions and prescribe treatments where appropriate
# - Train pharmacists to support specific treatment areas (e.g. dermatology, minor injuries)
# - Reduce unnecessary hospital visits by shifting care into the community

# 3. Optimise Resource Allocation
# - Prioritise high-pressure specialties (e.g. Oral Surgery, Orthopaedics, ENT)
# - Allocate additional funding and staff to these areas

# 4. Strengthen Primary Care (GP Services)
# - Improve access to GP appointments to prevent escalation to hospital care
# - Introduce triage systems to direct patients to the appropriate level of care

# 5. Collaborate with Private Healthcare Providers
# - Partner with private hospitals to reduce backlog
# - Use external capacity for non-emergency procedures

# Expected impact:
# - Reduced waiting times
# - Improved performance against the 18-week target
# - Better patient outcomes and reduced system pressure

# ============================================
# NHS England (2021-2025). Consultant-Led Referral to Treatment Waiting Times.
# Published by NHS England. Compiled and cleaned by Tawakalt Lawal, April 2026.
# Available at: https://github.com/TawannahAnalytics
```


```python

```
