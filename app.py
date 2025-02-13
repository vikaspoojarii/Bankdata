import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Loan Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# Loading the cleaned data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_bank_data.csv")
    return df

df = load_data()

# ---- HEADER ----
st.title("📊 Loan Data Analysis Dashboard")
st.write("Gain insights into loan trends, borrower demographics, and key financial metrics.")

# ---- SIDEBAR ----
st.sidebar.header("🔍 Filter Data")
selected_term = st.sidebar.selectbox("Select Loan Term", df["term"].unique())
selected_purpose = st.sidebar.selectbox("Select Loan Purpose", df["Purpose"].unique())

# Filter Data
filtered_df = df[(df["term"] == selected_term) & (df["Purpose"] == selected_purpose)]

# ---- METRICS ----
total_loans = len(filtered_df)
average_loan_amount = filtered_df["loan_amount"].mean()
default_rate = (filtered_df["loan_status"] == "Charged Off").sum() / total_loans * 100

# Display Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("📊 Total Loans", f"{total_loans:,}")
col2.metric("💰 Avg Loan Amount", f"${average_loan_amount:,.2f}")
col3.metric("⚠️ Default Rate", f"{default_rate:.2f}%")

# ---- VISUALIZATIONS ----
st.subheader("📌 Loan Amount Distribution")
fig_loan_dist = px.histogram(
    filtered_df, 
    x="loan_amount", 
    nbins=40, 
    title="Distribution of Loan Amounts", 
    color_discrete_sequence=["royalblue"],  
    opacity=0.8
)
fig_loan_dist.update_layout(
    xaxis_title="Loan Amount ($)",
    yaxis_title="Frequency",
    template="plotly_white"
)
st.plotly_chart(fig_loan_dist)

st.subheader("📌 Loan Status Breakdown")
fig_loan_status = px.pie(
    filtered_df, 
    names="loan_status",  
    title="Loan Status Distribution",
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig_loan_status)

st.subheader("📌 Loan Amount vs. Interest Rate")
fig_scatter = px.scatter(
    filtered_df, 
    x="loan_amount", 
    y="int_rate",
    title="Loan Amount vs Interest Rate",
    opacity=0.6,
    color_discrete_sequence=["green"]
)
st.plotly_chart(fig_scatter)

st.subheader("📌 Annual Income vs. Loan Amount")
fig_income = px.scatter(
    filtered_df, 
    x="annual_income", 
    y="loan_amount",
    title="Annual Income vs. Loan Amount",
    opacity=0.6,
    color_discrete_sequence=["blue"]
)
st.plotly_chart(fig_income)

# ---- FOOTER ----
st.write("📌 **Data Source:** Processed Loan Dataset")
st.write("🚀 **Built by:** Vikas Poojari | Data Analytics | Portfolio Project")

