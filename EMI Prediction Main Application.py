import streamlit as st
import pandas as pd
import pickle

with open("EMI Regression Model.pkl", "rb") as f:
    regression_model = pickle.load(f)

with open("EMI Classifier Model.pkl", "rb") as f:
    classification_model = pickle.load(f)

categorical_cols = {
    'Gender': ['Male', 'Female', 'Other'],
    'Marital Status': ['Yes', 'No'],
    'Education': ['High School', 'Graduate', 'Post Graduate'],
    'Employment Type': ['Self Employed', 'Private', 'Government', 'Business'],
    'Company Type': ['Private', 'Government', 'Business'],
    'House Type': ['Owned', 'Rented'],
    'Emi Scenario': ['Yes', 'No'],
    'Existing Loans': ['Yes', 'No']
}

numerical_cols = [
    'Age', 'Monthly Salary', 'Years Of Employment',
    'Monthly Rent', 'Family Size', 'Other Monthly Expenses',
    'Credit Score', 'Current Emi Amount', 'Requested Amount',
    'Emergency Fund', 'Bank Balance'
]

st.set_page_config(
    page_title="EMI Prediction Suite",
    page_icon="💰",
    layout="centered"
)

st.markdown("<h1 style='text-align: center; color: #4B0082;'> EMI Prediction & Eligibility App</h1>", unsafe_allow_html=True)
st.write("Choose between **EMI Amount Prediction** and **Eligibility Prediction** below:")

option = st.sidebar.radio(
    "Select Prediction Type:",
    ("EMI Amount Prediction", "EMI Eligibility Prediction")
)

user_input = {}

st.subheader("Enter Your Details")

for col, options in categorical_cols.items():
    user_input[col] = st.selectbox(f"{col}", options)

for col in numerical_cols:
    user_input[col] = st.number_input(f"{col}", min_value=0, value=0)

input_df = pd.DataFrame([user_input])

if option == "EMI Amount Prediction":
    st.markdown("Predict Your Monthly EMI Amount")

    if st.button("Predict EMI Amount"):
        try:
            prediction = regression_model.predict(input_df)[0]
            st.success(f"Predicted EMI Amount: **₹{prediction:.2f}**")
        except Exception as e:
            st.error(f"Prediction Error: {e}")
    else:
        st.info("Enter details and click Predict to see EMI Amount.")

elif option == "EMI Eligibility Prediction":
    st.markdown("Check Your EMI Eligibility")

    if st.button("Predict Eligibility"):
        try:
            prediction = classification_model.predict(input_df)[0]
            st.success(f"EMI Eligibility Result: **{prediction}**")
        except Exception as e:
            st.error(f"rediction Error: {e}")
    else:
        st.info("Enter details and click Predict to check eligibility.")

with st.expander("View Input Data"):
    st.dataframe(input_df)
