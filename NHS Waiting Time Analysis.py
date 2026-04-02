#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("nhs_rtt_waiting_times_2021_2025.csv")

df.head()



# In[2]:


# -----------------------------------------------
df.columns


# In[3]:


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


# In[4]:


# -----------------------------------------------
# Check for missing values in each column

# df.isnull() -> returns True/False for missing values
# .sum() -> counts how many missing values per column
df.isnull().sum()


# In[5]:


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


# In[6]:


# -----------------------------------------------


df[df['total_waiting'].isnull()].head()


# In[7]:


# -----------------------------------------------
# Insight from investigation of missing values

# I observed that missing values in 'total_waiting' and
# 'pct_within_18_weeks' occur mainly when rtt_part_type = 'Part_3'

# This suggests the missing data is NOT random
# It may be that these metrics are not applicable or not recorded for Part_3

# Therefore, missing values should be treated carefully
# rather than immediately removing or filling them

# -----------------------------------------------


# In[8]:


# Check missing values by RTT part type

df.groupby('rtt_part_type')[['total_waiting', 'pct_within_18_weeks']]\
  .apply(lambda x: x.isnull().sum())


# In[9]:


# -----------------------------------------------
# Final insight on missing values

# Missing values are heavily concentrated in rtt_part_type = 'Part_3'
# This confirms that the missing data is NOT random

# It is likely that 'total_waiting' and 'pct_within_18_weeks'
# are not recorded or not applicable for Part_3 cases

# Therefore, Part_3 may need to be treated separately in analysis


# In[10]:


# -----------------------------------------------
# Convert 'period' column to datetime format
# This allows time-based analysis like trends over months/years

df['period'] = pd.to_datetime(df['period'], format='%Y-%m')
# Check data types to confirm conversion
df.dtypes


# In[11]:


# ===============================
# START OF ANALYSIS
# ===============================

# Objective:
# Analyse NHS waiting times to understand:
# - Trends over time (2021-2025)
# - Performance against targets
# - Areas under pressure

# From this point, the analysis phase begins after data cleaning



# In[12]:


# ===============================
# Question 1. How have NHS waiting times changed over time?
# ===============================

# Group data by time (period)
# Calculate average waiting metrics per month

df_trend = df.groupby('period')[['total_waiting', 'pct_within_18_weeks']].mean()

# View first few rows
df_trend.head()


# In[13]:


# Plot total waiting trend
df_trend['total_waiting'].plot()

plt.title('NHS Total Waiting Trend Over Time')
plt.xlabel('Period')
plt.ylabel('Total Waiting')
plt.show()



# In[14]:


# -----------------------------------------------
# Plot performance against 18-week target
df_trend['pct_within_18_weeks'].plot()

plt.title('Percentage Within 18 Weeks Over Time')
plt.xlabel('Period')
plt.ylabel('Percentage')
plt.show()


# In[15]:


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


# In[16]:


# -----------------------------------------------
worst_performing = df_hospital.sort_values('pct_within_18_weeks').head(10)

worst_performing


# In[17]:


# -----------------------------------------------
highest_waiting = df_hospital.sort_values('total_waiting', ascending=False).head(10)

highest_waiting


# In[18]:


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



# In[19]:


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


# In[20]:


# -----------------------------------------------
# Specialties with highest waiting lists (most pressure)
top_waiting_specialties = df_specialty.sort_values('total_waiting', ascending=False).head(10)

top_waiting_specialties


# In[21]:


top_waiting_specialties['total_waiting'].plot(kind='barh', figsize=(10,6), color='orange')
plt.title('10 Specialties with Highest Waiting Lists')
plt.xlabel('Average Total Waiting')
plt.tight_layout()
plt.show()


# In[22]:


# -----------------------------------------------
# Specialties with lowest performance (worst at meeting target)
worst_specialties = df_specialty.sort_values('pct_within_18_weeks').head(10)

worst_specialties


# In[23]:


worst_specialties['pct_within_18_weeks'].plot(kind='barh', figsize=(10,6), color='red')
plt.title('10 Worst Performing Specialties by 18-Week Target')
plt.xlabel('% Within 18 Weeks')
plt.tight_layout()
plt.show()


# In[24]:


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


# In[25]:


# Group data by hospital
df_demand = df.groupby('provider_org_name')[['total_waiting', 'pct_within_18_weeks']].mean()


# Check relationship (correlation)
correlation = df_demand['total_waiting'].corr(df_demand['pct_within_18_weeks'])

correlation


# In[26]:


# -----------------------------------------------
# Scatter plot: Demand vs Performance
plt.scatter(df_demand['total_waiting'], df_demand['pct_within_18_weeks'])

plt.xlabel('Total Waiting (Demand)')
plt.ylabel('Percentage Within 18 Weeks (Performance)')
plt.title('Demand vs Performance Relationship')

plt.show()


# In[27]:


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



# In[28]:


# ============================================
# KPI Analysis:Is the NHS meeting its 18-Week Target (92%)
# ============================================

# Calculate average performance over time
df_kpi = df.groupby('period')['pct_within_18_weeks'].mean()

df_kpi


# In[29]:


# -----------------------------------------------
plt.plot(df_kpi.index, df_kpi.values)

# Add NHS target line
plt.axhline(y=92)

plt.xlabel('Time')
plt.ylabel('Percentage Within 18 Weeks')
plt.title('NHS Performance vs 92% Target')

plt.show()


# In[30]:


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


# In[31]:


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


# In[ ]:




