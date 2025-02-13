#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import os


# In[5]:


print(os.getcwd())


# In[81]:

import pandas as pd


df = pd.read_csv("Bank Data.csv")
 


df.columns = df.columns.str.strip()



# In[6]:

# os.chdir('/Users/Vikaspoojari/Desktop/portfolio')  # Removed for Streamlit deployment



# In[7]:


df=pd.read_csv('Bank Data.csv')


# In[8]:


df


# In[9]:


df.info()


# In[10]:


df.head()


# In[11]:


##Since Currency is object we will now convert it into numeric


# In[18]:


# Converting 'loan_amount' and to float (removing '$' sign)
df['loan_amount'] = df['loan_amount'].replace(r'[\$,]', '', regex=True).astype(float)



# In[15]:


print(df.column)


# 
# We can see that the column names **`' loan_amount '`** and **`' total_payment '`** have **leading and trailing spaces**, which can cause errors when trying to access them.
# 
# ## ** Problem**
# When trying to access `df['loan_amount']`, a **KeyError** occurred because the actual column name in the dataset was **`' loan_amount '`** (with spaces).  
# 
# Since column names must be an exact match, the presence of these spaces made it difficult to reference them properly.
# 
# ## ** Solution: Removing Extra Spaces**
# To resolve this issue, we will use the **`.str.strip()`** method to clean the column names:
# 
# ```python
# # Remove extra spaces from column names
# df.columns = df.columns.str.strip()
# 

# In[17]:


df.columns = df.columns.str.strip()


# In[24]:


df['loan_amount'] = df['loan_amount'].replace(r'[\$,]', '', regex=True).astype(float)
df['total_payment'] = df['total_payment'].replace(r'[\$,]', '', regex=True).astype(float)


# In[26]:


print(df[['loan_amount']].head())


# In[31]:


print(df['loan_amount'].dtype)


# 
# 
# ## **Final Takeaways**
#  The `loan_amount` column is now **clean** and **numerically formatted**.  
#  This allows for **statistical analysis and calculations** in Pandas.  
#  The same transformation can be applied to **other financial columns** (e.g., `total_payment`).  
# 

# In[32]:


print(df[['issue_date', 'last_credit_pull_date' , 'last_payment_date', 'next_payment_date']].dtypes)


# In[33]:


# Converting date columns with explicit format


# In[38]:


date_cols = ['issue_date', 'last_credit_pull_date', 'last_payment_date', 'next_payment_date']


# In[40]:


for col in date_cols:
    df[col] = pd.to_datetime(df[col], format='%m/%d/%Y', errors='coerce')


# In[41]:


print(df[['issue_date', 'last_credit_pull_date', 'last_payment_date', 'next_payment_date']].dtypes)


# In[42]:


#This confirms that all date columns are now properly converted to datetime format.


# In[43]:


print(df[date_cols].isnull().sum())


# **No missing Values Found**

# In[44]:


missing_values = df.isnull().sum()


# In[45]:


missing_values[missing_values>0]


# In[46]:


print(df.isnull().sum().sum())


# In[48]:


df['emp_title'].fillna('Unknown', inplace = True)


# In[49]:


print(df['emp_title'].isnull().sum())


# In[50]:


missing_values = df.isnull().sum()


# In[51]:


missing_values[missing_values>0]


# # **Handling Missing Values in `emp_title` Column**
# 
# ## **Issue: Missing Values in `emp_title`**
# After checking for missing values in the dataset, we found **1,438 missing values** in the `emp_title` column.
# 
# ```python
# df['emp_title'].isnull().sum()
# 

# In[52]:


df.describe()


# In[53]:


#Unique loan statuses
df['loan_status']. value_counts()


# 🔹 Interpretation**
# -  **Majority of loans are Fully Paid** – This indicates that most borrowers successfully repay their loans.
# -  **5,333 loans are Charged Off** – These loans were **defaulted** (borrowers failed to repay).
# -  **1,098 loans are Current** – These loans are **still active**, meaning payments are ongoing.
# 

# In[55]:


#Visualising 


# In[56]:


import matplotlib.pyplot as plt


# In[62]:


plt.figure(figsize=(10,6))
plt.hist(df['loan_amount'], bins=50, color='royalblue', edgecolor='black', alpha=0.75)
plt.title('Distribution of Loan Amounts', fontsize=14, fontweight='bold')
plt.xlabel('Loan Amount ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# # **📊 Loan Amount Distribution**
# 
# ## ** Why This Matters**
# Understanding how loan amounts are distributed helps us see **common borrowing patterns**. Are most people borrowing small amounts, or do we have a lot of high-value loans? This can give insights into borrower behavior and lending trends.
# 
# ---
# 
# ## **🔹 What We Found**
# -  **Most loans fall between $5,000 and $15,000**, showing that people typically borrow in this range.  
# -  There are *spikes around $10,000, $15,000, and $25,000*, suggesting these might help in commomn loan requesting amounts
# -  **Very few loans go beyond $30,000**, meaning high-value loans are not as frequent.  
# -  The distribution is **right-skewed**, meaning smaller loans are much more common than larger ones.
# 
# ## ** Making the Chart Look Better**
# To make the histogram clearer and easier to read, a few tweaks were made:
#  **Larger figure size** so details aren’t lost.  
#  **Better colors (royal blue) with black edges** to improve contrast.  
#  **Added grid lines** to help compare frequencies more easily.  
#  **Labeled everything properly** (because no one likes charts without labels).  
# 
#   
# 

# In[65]:


import matplotlib.pyplot as plt


plt.figure(figsize=(10,6))
plt.scatter(df['loan_amount'], df['int_rate'], alpha=0.5, color='green')
plt.title('Loan Amount vs. Interest Rate', fontsize=14, fontweight='bold')
plt.xlabel('Loan Amount ($)', fontsize=12)
plt.ylabel('Interest Rate (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)


plt.show()



# # **Loan Amount vs. Interest Rate Analysis**
# 
# ## **Why This Matters**
# Understanding the relationship between **loan amount** and **interest rate** helps determine:
# - Whether larger loans come with higher interest rates.
# - If smaller loans receive better interest rates.
# - Any unusual patterns in lending rates.
# 
# ---
# 
# ## **Key Observations**
# - Loans under $15,000 have a wide range of interest rates, with some very low and others significantly high.  
# - Higher loan amounts generally have lower interest rates, but there are exceptions.  
# - There are vertical clusters at $10,000, $15,000, $25,000, and $35,000, indicating standard loan amounts.  
# - There is no strict linear trend, but interest rates appear to flatten as loan amounts increase.  
# 
# ---
# 
# ## **Improving the Visualization**
# To enhance clarity and readability, the following improvements were applied:
# - Increased figure size for better visibility.  
# - Used semi-transparent markers to reduce excessive overlap.  
# - Added grid lines to help compare interest rates across loan amounts.  
# - Styled the title and labels with improved font sizes and bold formatting.  
# 

# In[67]:


plt.figure(figsize=(10,6))
plt.hexbin(df['loan_amount'], df['int_rate'], gridsize=50, cmap='viridis', bins='log')
plt.colorbar(label='Density of Loans')
plt.xlabel('Loan Amount ($)', fontsize=12)
plt.ylabel('Interest Rate (%)', fontsize=12)
plt.title('Loan Amount vs. Interest Rate Density Heatmap', fontsize=14, fontweight='bold')

plt.show()


# In[68]:


plt.figure(figsize=(10,6))


plt.scatter(df['annual_income'], df['loan_amount'], alpha=0.5, color='blue')
plt.xlabel('Annual Income ($)', fontsize=12)
plt.ylabel('Loan Amount ($)', fontsize=12)
plt.title('Annual Income vs. Loan Amount', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()


# # **Annual Income vs. Loan Amount Analysis**
# 
# ## *In this we-**
# Understanding the relationship between **borrower income** and **loan amount** helps answer key financial questions:
# - Do higher-income borrowers take larger loans, or do they borrow conservatively?
# - Is there a **cap on loan amounts** regardless of income?
# - Are there **low-income borrowers taking high-value loans**, indicating potential financial risk?
# 
# ---
# 
# ## **Key Observations**
# - **Most borrowers have an annual income below $200,000**.  
# - **Loan amounts remain within a fixed range ($5,000 - $35,000) across income levels**, suggesting lending caps.  
# - **A few extreme outliers exist with very high incomes (~$6 million) but moderate loan amounts**.  
# - **Some lower-income individuals have large loans**, which might indicate **higher risk** or **more lenient lending policies**.  
# 

# In[71]:





# In[94]:


#We will make a Dashboard


# In[73]:


import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Loan Data Dashboard", style={'textAlign': 'center'}),
    html.P("This dashboard will help analyze loan trends.")
])


if __name__ == '__main__':
    app.run_server(debug=True)


# In[89]:


import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("Bank Data.csv")  

df.columns = df.columns.str.strip()

df["loan_amount"] = df["loan_amount"].astype(str).str.replace(r"[\$,]", "", regex=True).astype(float)

df = df[df["loan_amount"] <= 40000]  

app = dash.Dash(__name__)

fig_loan_dist = px.histogram(
    df, 
    x="loan_amount",  
    nbins=40, 
    title="Loan Amount Distribution", 
    color_discrete_sequence=["royalblue"],  
    opacity=0.8
)

fig_loan_dist.update_layout(
    xaxis_title="Loan Amount ($)",
    yaxis_title="Count",
    xaxis=dict(
        tickangle=-45,  
        tickmode="array",  
        tickvals=[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    ),
    yaxis_type="linear",  
    bargap=0.1,      template="plotly_white"
)

app.layout = html.Div([
    html.H1("Loan Data Dashboard", style={'textAlign': 'center'}),
    html.P("This dashboard will help analyze loan trends."),
    
    dcc.Graph(figure=fig_loan_dist)  
])

if __name__ == '__main__':
    app.run_server(debug=True)


# In[90]:


import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("Bank Data.csv")  

df.columns = df.columns.str.strip()

df["loan_amount"] = df["loan_amount"].astype(str).str.replace(r"[\$,]", "", regex=True).astype(float)

df = df[df["loan_amount"] <= 40000]  

app = dash.Dash(__name__)

# Loan Amount Distribution Histogram
fig_loan_dist = px.histogram(
    df, 
    x="loan_amount",  
    nbins=40,  
    title="Loan Amount Distribution", 
    color_discrete_sequence=["royalblue"],  
    opacity=0.8
)

fig_loan_dist.update_layout(
    xaxis_title="Loan Amount ($)",
    yaxis_title="Count",
    xaxis=dict(
        tickangle=-45,  
        tickmode="array",  
        tickvals=[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    ),
    yaxis_type="linear",  
    bargap=0.1,  
    template="plotly_white"
)

# Loan Status Pie Chart
fig_loan_status = px.pie(
    df, 
    names="loan_status",  
    title="Loan Status Breakdown",
    color_discrete_sequence=px.colors.qualitative.Set2
)

# Dashboard Layout
app.layout = html.Div([
    html.H1("Loan Data Dashboard", style={'textAlign': 'center'}),
    html.P("This dashboard helps analyze loan trends and repayment status."),

    dcc.Graph(figure=fig_loan_dist),  # Histogram
    dcc.Graph(figure=fig_loan_status)  # Pie Chart
])

if __name__ == '__main__':
    app.run_server(debug=True)


# In[91]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("Bank Data.csv")  

df.columns = df.columns.str.strip()

df["loan_amount"] = df["loan_amount"].astype(str).str.replace(r"[\$,]", "", regex=True).astype(float)

df = df[df["loan_amount"] <= 40000]  

app = dash.Dash(__name__)

# Unique loan terms for dropdown
loan_terms = df["term"].unique()

app.layout = html.Div([
    html.H1("Loan Data Dashboard", style={'textAlign': 'center'}),
    html.P("This dashboard helps analyze loan trends and repayment status."),

    html.Label("Select Loan Term:"),
    dcc.Dropdown(
        id="term_filter",
        options=[{"label": term, "value": term} for term in loan_terms],
        value=loan_terms[0],  # Default selection
        clearable=False
    ),

    dcc.Graph(id="loan_dist_chart"),
    dcc.Graph(id="loan_status_chart")
])

@app.callback(
    [Output("loan_dist_chart", "figure"), Output("loan_status_chart", "figure")],
    [Input("term_filter", "value")]
)
def update_charts(selected_term):
    filtered_df = df[df["term"] == selected_term]

    fig_loan_dist = px.histogram(
        filtered_df, 
        x="loan_amount",  
        nbins=40,  
        title="Loan Amount Distribution", 
        color_discrete_sequence=["royalblue"],  
        opacity=0.8
    )

    fig_loan_dist.update_layout(
        xaxis_title="Loan Amount ($)",
        yaxis_title="Count",
        xaxis=dict(tickangle=-45, tickmode="array", tickvals=[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]),
        yaxis_type="linear",
        bargap=0.1,
        template="plotly_white"
    )

    fig_loan_status = px.pie(
        filtered_df, 
        names="loan_status",  
        title="Loan Status Breakdown",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    return fig_loan_dist, fig_loan_status

if __name__ == '__main__':
    app.run_server(debug=True)


# In[92]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("Bank Data.csv")  

df.columns = df.columns.str.strip()

df["loan_amount"] = df["loan_amount"].astype(str).str.replace(r"[\$,]", "", regex=True).astype(float)

df = df[df["loan_amount"] <= 40000]  

app = dash.Dash(__name__)

loan_terms = df["term"].unique()
loan_purposes = df["Purpose"].unique()

app.layout = html.Div([
    html.H1("Loan Data Dashboard", style={'textAlign': 'center'}),
    html.P("This dashboard helps analyze loan trends and repayment status."),

    html.Label("Select Loan Term:"),
    dcc.Dropdown(
        id="term_filter",
        options=[{"label": term, "value": term} for term in loan_terms],
        value=loan_terms[0],  
        clearable=False
    ),

    html.Label("Select Loan Purpose:"),
    dcc.Dropdown(
        id="purpose_filter",
        options=[{"label": purpose, "value": purpose} for purpose in loan_purposes],
        value=loan_purposes[0],  
        clearable=False
    ),

    dcc.Graph(id="loan_dist_chart"),
    dcc.Graph(id="loan_status_chart")
])

@app.callback(
    [Output("loan_dist_chart", "figure"), Output("loan_status_chart", "figure")],
    [Input("term_filter", "value"), Input("purpose_filter", "value")]
)
def update_charts(selected_term, selected_purpose):
    filtered_df = df[(df["term"] == selected_term) & (df["Purpose"] == selected_purpose)]

    fig_loan_dist = px.histogram(
        filtered_df, 
        x="loan_amount",  
        nbins=40,  
        title="Loan Amount Distribution", 
        color_discrete_sequence=["royalblue"],  
        opacity=0.8
    )

    fig_loan_dist.update_layout(
        xaxis_title="Loan Amount ($)",
        yaxis_title="Count",
        xaxis=dict(tickangle=-45, tickmode="array", tickvals=[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]),
        yaxis_type="linear",
        bargap=0.1,
        template="plotly_white"
    )

    fig_loan_status = px.pie(
        filtered_df, 
        names="loan_status",  
        title="Loan Status Breakdown",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    return fig_loan_dist, fig_loan_status

if __name__ == '__main__':
    app.run_server(debug=True)


# In[93]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("Bank Data.csv")  

df.columns = df.columns.str.strip()

df["loan_amount"] = df["loan_amount"].astype(str).str.replace(r"[\$,]", "", regex=True).astype(float)

df = df[df["loan_amount"] <= 40000]  

app = dash.Dash(__name__)

loan_terms = df["term"].unique()
loan_purposes = df["Purpose"].unique()

app.layout = html.Div([
    html.H1("Loan Data Dashboard", style={'textAlign': 'center'}),
    html.P("This dashboard helps analyze loan trends and repayment status."),

    # Summary Metrics
    html.Div([
        html.Div(id="total_loans", style={"fontSize": "20px", "fontWeight": "bold"}),
        html.Div(id="avg_loan_amount", style={"fontSize": "20px", "fontWeight": "bold"}),
        html.Div(id="default_rate", style={"fontSize": "20px", "fontWeight": "bold"})
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),

    html.Label("Select Loan Term:"),
    dcc.Dropdown(
        id="term_filter",
        options=[{"label": term, "value": term} for term in loan_terms],
        value=loan_terms[0],  
        clearable=False
    ),

    html.Label("Select Loan Purpose:"),
    dcc.Dropdown(
        id="purpose_filter",
        options=[{"label": purpose, "value": purpose} for purpose in loan_purposes],
        value=loan_purposes[0],  
        clearable=False
    ),

    dcc.Graph(id="loan_dist_chart"),
    dcc.Graph(id="loan_status_chart")
])

@app.callback(
    [Output("loan_dist_chart", "figure"), Output("loan_status_chart", "figure"),
     Output("total_loans", "children"), Output("avg_loan_amount", "children"), Output("default_rate", "children")],
    [Input("term_filter", "value"), Input("purpose_filter", "value")]
)
def update_charts(selected_term, selected_purpose):
    filtered_df = df[(df["term"] == selected_term) & (df["Purpose"] == selected_purpose)]

    fig_loan_dist = px.histogram(
        filtered_df, 
        x="loan_amount",  
        nbins=40,  
        title="Loan Amount Distribution", 
        color_discrete_sequence=["royalblue"],  
        opacity=0.8
    )

    fig_loan_dist.update_layout(
        xaxis_title="Loan Amount ($)",
        yaxis_title="Count",
        xaxis=dict(tickangle=-45, tickmode="array", tickvals=[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]),
        yaxis_type="linear",
        bargap=0.1,
        template="plotly_white"
    )

    fig_loan_status = px.pie(
        filtered_df, 
        names="loan_status",  
        title="Loan Status Breakdown",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    # Calculate Summary Metrics
    total_loans = f"Total Loans Issued: {len(filtered_df):,}"
    avg_loan_amount = f"Average Loan Amount: ${filtered_df['loan_amount'].mean():,.2f}"
    default_rate = f"Default Rate: {((filtered_df['loan_status'] == 'Charged Off').sum() / len(filtered_df)) * 100:.2f}%"

    return fig_loan_dist, fig_loan_status, total_loans, avg_loan_amount, default_rate

if __name__ == '__main__':
    app.run_server(debug=True)


# # **📊 Loan Data Dashboard**
# 
# ## **Overview**
# This interactive dashboard provides insights into loan distribution, repayment status, and borrower trends. Users can **filter data dynamically** using dropdown menus for **Loan Term** and **Loan Purpose**.
# 
# ---
# 
# ## **📌 Features**
# ✔ **Loan Amount Distribution Histogram** – Shows the frequency of different loan amounts.  
# ✔ **Loan Status Breakdown Pie Chart** – Displays the proportion of Fully Paid, Charged Off, and Current loans.  
# ✔ **Interactive Filters** – Users can filter data by **Loan Term** and **Loan Purpose**.  
# ✔ **Summary Metrics** – Key statistics on total loans, average loan amount, and default rate.  
# 
# ---
# 
# ## **📊 Visualizations**
# ### **1️⃣ Loan Amount Distribution**
# - Displays the number of loans issued for different loan amounts.
# - Helps identify common loan sizes and lending patterns.
# - Interactive filtering based on Loan Term and Loan Purpose.
# 
# ### **2️⃣ Loan Status Breakdown**
# - Pie chart showing repayment status:
#   - **Fully Paid**
#   - **Charged Off (Defaulted)**
#   - **Current (Ongoing Loans)**
# - Helps assess the proportion of defaulted vs. repaid loans.
# 
# ### **3️⃣ Summary Metrics**
# | Metric | Description |
# |--------|-------------|
# | **Total Loans Issued** | Number of loans in the selected category. |
# | **Average Loan Amount** | Mean loan amount based on selected filters. |
# | **Default Rate (%)** | Percentage of loans that were charged off. |
# 
# ---
# 
# ## **📌 How It Works**
# 1️⃣ **Select a Loan Term** (e.g., 36 months, 60 months).  
# 2️⃣ **Choose a Loan Purpose** (e.g., Debt Consolidation, Business, Home Improvement).  
# 3️⃣ **Dashboard updates automatically** to reflect the selected criteria.  
# 
# ---
# 
# ## **📌 Key Observations**
# - **Most loans fall between $5,000 and $15,000**.
# - **Majority of loans (~83%) are Fully Paid**, with a **small percentage (~13.8%) defaulting**.
# - **Loan Purpose influences repayment trends** – Some categories have higher default rates.
# - **Shorter loan terms generally have lower loan amounts**.
# 
# ---
# 
# ## ** Future Enhancements**
#  **Time Series Analysis** – Loan trends over different issue dates.  
#  **Credit Score Impact** – Exploring how credit scores affect default rates.  
# **Deployment** – Hosting the dashboard online (Streamlit, Heroku, or Flask).  
# 
# ---
# 
# ## ** Code Reference**
# The dashboard is built using:
# - **Dash & Plotly** for interactive visualizations.
# - **Pandas** for data processing.
# - **Dropdown Callbacks** for dynamic filtering.
# 
# 
# 

# In[1]:


get_ipython().system('jupyter nbconvert --to script bankdata.ipynb')


# In[ ]:




