import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

# Convert values like €1.5M or €500K to float
def parse_euro(value):
    if isinstance(value, str):
        value = value.replace('€', '').replace(',', '').strip()
        if 'M' in value:
            return float(value.replace('M', '')) * 1_000_000
        elif 'K' in value:
            return float(value.replace('K', '')) * 1_000
        else:
            return float(value)
    return value

# Load dataset
df = pd.read_csv("fifa_eda_stats.csv")
df.columns = df.columns.str.strip()

# Clean currency columns
df['Value'] = df['Value'].apply(parse_euro)
df['Wage'] = df['Wage'].apply(parse_euro)

# Select features
features = ['Age', 'Overall', 'Potential', 'Value', 'Wage']
df = df.dropna(subset=features)

X = df[['Age', 'Overall', 'Potential']]
y = df['Value']

# Scale input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, "decision_tree_model.joblib")
joblib.dump(scaler, "scaler.joblib")

print("✅ Model trained and saved successfully.")
y