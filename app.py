import streamlit as st
import pandas as pd
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Loan Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# Loading dataset
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_bank_data.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Data")
selected_term = st.sidebar.selectbox("Select Loan Term", df["term"].unique())
selected_purpose = st.sidebar.selectbox("Select Loan Purpose", df["Purpose"].unique())

# Filter dataset
filtered_df = df[(df["term"] == selected_term) & (df["Purpose"] == selected_purpose)]

# Key Metrics
total_loans = len(filtered_df)
average_loan_amount = filtered_df["loan_amount"].mean()
default_rate = (filtered_df["loan_status"] == "Charged Off").sum() / total_loans * 100

# Dashboard Header
st.title("Loan Data Analysis Dashboard")
st.write("This dashboard provides insights into loan trends, borrower demographics, and key financial metrics.")

# Key Metrics Display
col1, col2, col3 = st.columns(3)
col1.metric("Total Loans", f"{total_loans:,}")
col2.metric("Average Loan Amount", f"${average_loan_amount:,.2f}")
col3.metric("Default Rate", f"{default_rate:.2f}%")

# Loan Amount Distribution
st.subheader("Loan Amount Distribution")
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
    template="plotly_white",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)
st.plotly_chart(fig_loan_dist, use_container_width=True)

# Loan Status Breakdown
st.subheader("Loan Status Breakdown")
fig_loan_status = px.pie(
    filtered_df, 
    names="loan_status",  
    title="Loan Status Distribution",
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig_loan_status, use_container_width=True)

# Loan Amount vs. Interest Rate
st.subheader("Loan Amount vs. Interest Rate")
fig_scatter = px.scatter(
    filtered_df, 
    x="loan_amount", 
    y="int_rate",
    title="Loan Amount vs Interest Rate",
    opacity=0.6,
    color="loan_status",
    hover_data=["Grade", "int_rate", "annual_income"]
)
fig_scatter.update_layout(
    xaxis_title="Loan Amount ($)",
    yaxis_title="Interest Rate (%)",
    template="plotly_white",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)
st.plotly_chart(fig_scatter, use_container_width=True)

# Annual Income vs. Loan Amount
st.subheader("Annual Income vs. Loan Amount")
fig_income = px.scatter(
    filtered_df, 
    x="annual_income", 
    y="loan_amount",
    title="Annual Income vs. Loan Amount",
    opacity=0.7,
    color="home_ownership",
    size="loan_amount",
    hover_data=["loan_status", "verification_status"]
)
fig_income.update_layout(
    xaxis_title="Annual Income ($)",
    yaxis_title="Loan Amount ($)",
    template="plotly_white",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)
st.plotly_chart(fig_income, use_container_width=True)

# Top Borrower Locations
st.subheader("Top Borrower Locations")
top_states = filtered_df["address_state"].value_counts().nlargest(10)
fig_states = px.bar(
    top_states, 
    x=top_states.index, 
    y=top_states.values, 
    title="Top 10 Borrower States",
    color=top_states.values,
    color_continuous_scale="Blues"
)
fig_states.update_layout(
    xaxis_title="State",
    yaxis_title="Number of Borrowers",
    template="plotly_white",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)
st.plotly_chart(fig_states, use_container_width=True)

# Footer
st.markdown("<h4 style='text-align: center;'>Data Source: Processed Loan Dataset</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Developed by Vikas Poojari </h5>", unsafe_allow_html=True)
