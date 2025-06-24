import os
print("Files here:", os.listdir('.'))

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load model, scaler, and features
model = joblib.load("decision_tree_model.joblib")
scaler = joblib.load("scaler.joblib")
with open("features.txt", "r") as f:
    feature_names = f.read().splitlines()

st.set_page_config(page_title="Sports Performance Prediction Dashboard", layout="wide")
st.title("⚽ Sports Performance Prediction Dashboard")

st.markdown("""
This dashboard predicts a football player's **value category** (Low, Medium, High) based on their attributes.
You can either upload a CSV file or enter values manually.
""")

# Sidebar: Choose input method
input_method = st.sidebar.radio("Choose input method:", ["Upload CSV", "Manual Input"])

def preprocess(df):
    df['Preferred Foot'] = df['Preferred Foot'].map({'Right': 1, 'Left': 0})
    df['Position'] = df['Position'].astype('category').cat.codes
    df = df[feature_names]
    df_scaled = scaler.transform(df)
    return df_scaled

if input_method == "Upload CSV":
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        try:
            X_processed = preprocess(data)
            preds = model.predict(X_processed)
            data['Predicted Value Category'] = preds
            st.success("✅ Predictions complete!")
            st.dataframe(data)

            st.markdown("### 📊 Predicted Value Distribution")
            fig, ax = plt.subplots()
            sns.countplot(data=data, x='Predicted Value Category', palette='viridis', ax=ax)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error in processing file: {e}")

else:
    st.subheader("📋 Manual Input")
    input_data = {}
    for feat in feature_names:
        input_data[feat] = st.number_input(f"{feat}", min_value=0.0, value=50.0)
    input_df = pd.DataFrame([input_data])
    try:
        X_processed = preprocess(input_df)
        pred = model.predict(X_processed)[0]
        st.success(f"🎯 Predicted Value Category: **{pred}**")
    except Exception as e:
        st.error(f"Prediction error: {e}")

st.markdown("---")
st.caption("Built by Taha Mazhar- BSCS (AI) || Machine Learning ")

try:
    model = joblib.load("decision_tree_model.joblib")
except FileNotFoundError:
    st.error("Model file not found. Please make sure it's uploaded to the repository.")

