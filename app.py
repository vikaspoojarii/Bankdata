import streamlit as st
import pandas as pd
import plotly.express as px

# Load Cleaned Data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_bank_data.csv")
    return df

df = load_data()

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Loan Analysis Dashboard", page_icon="📊", layout="wide")

# ---- HEADER ----
st.title("📊 Loan Data Analysis Dashboard")
st.markdown("**A comprehensive dashboard analyzing loan amounts, repayment trends, and borrower demographics.**")

# ---- METRICS ----
st.subheader("📈 Key Loan Insights")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Loans Issued", f"{df.shape[0]:,}")
col2.metric("Avg. Loan Amount", f"${df['loan_amount'].mean():,.2f}")
col3.metric("Avg. Interest Rate", f"{df['int_rate'].mean():.2f}%")
col4.metric("Default Rate", f"{((df['loan_status'] == 'Charged Off').sum() / df.shape[0]) * 100:.2f}%")

st.divider()  # Visual break

# ---- LOAN DISTRIBUTION ----
st.subheader("💰 Loan Amount Distribution")

fig_loan_dist = px.histogram(df, x="loan_amount", nbins=40, 
                             title="Distribution of Loan Amounts", 
                             color_discrete_sequence=["royalblue"])
st.plotly_chart(fig_loan_dist, use_container_width=True)

# ---- LOAN STATUS BREAKDOWN ----
st.subheader("📌 Loan Status Breakdown")

fig_loan_status = px.pie(df, names="loan_status", title="Loan Status Breakdown", 
                         color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig_loan_status, use_container_width=True)

st.divider()

# ---- INCOME VS LOAN ----
st.subheader("💵 Income vs Loan Amount")

fig_income_loan = px.scatter(df, x="annual_income", y="loan_amount", 
                             title="Annual Income vs Loan Amount", 
                             color="loan_status", opacity=0.6)
st.plotly_chart(fig_income_loan, use_container_width=True)

# ---- LOAN TERM FILTER ----
st.subheader("🔍 Loan Term & Purpose Breakdown")

col_filter1, col_filter2 = st.columns(2)
with col_filter1:
    selected_term = st.selectbox("Select Loan Term:", df["term"].unique())

with col_filter2:
    selected_purpose = st.selectbox("Select Loan Purpose:", df["Purpose"].unique())

filtered_df = df[(df["term"] == selected_term) & (df["Purpose"] == selected_purpose)]

fig_filtered_loan = px.histogram(filtered_df, x="loan_amount", nbins=30, 
                                 title=f"Loan Amount Distribution ({selected_term}, {selected_purpose})", 
                                 color_discrete_sequence=["orange"])
st.plotly_chart(fig_filtered_loan, use_container_width=True)

# ---- FOOTER ----
st.markdown("🚀 **Built using Streamlit & Plotly** | Developed by [Vikas Poojari](https://www.linkedin.com/in/vikaspoojari)")

