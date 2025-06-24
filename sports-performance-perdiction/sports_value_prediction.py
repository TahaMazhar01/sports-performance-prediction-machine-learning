# Required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
df = pd.read_csv("fifa_eda_stats.csv")

# Convert 'Value' column to numeric (in Euros)
def value_to_float(value):
    if isinstance(value, str):
        value = value.strip("€")
        if "M" in value:
            return float(value.replace("M", "")) * 1e6
        elif "K" in value:
            return float(value.replace("K", "")) * 1e3
        else:
            try:
                return float(value)
            except:
                return np.nan
    return np.nan

df['Value(EUR)'] = df['Value'].apply(value_to_float)

# Categorize value into classes
def value_category(val):
    if val < 5e6:
        return 'Low'
    elif val < 30e6:
        return 'Medium'
    else:
        return 'High'

df['ValueCategory'] = df['Value(EUR)'].apply(value_category)

# Drop rows with missing value categories
df_cleaned = df.dropna(subset=['ValueCategory'])

# Drop irrelevant features
drop_columns = ['ID', 'Name', 'Nationality', 'Club', 'Value', 'Wage', 'Joined', 'Loaned From',
                'Contract Valid Until', 'Release Clause', 'Work Rate', 'Body Type', 'Height', 'Weight']
df_cleaned = df_cleaned.drop(columns=drop_columns)

# Drop rows with any remaining NaNs
df_cleaned = df_cleaned.dropna()

# Label encode categorical features
label_cols = ['Preferred Foot', 'Position']
le = LabelEncoder()
for col in label_cols:
    df_cleaned[col] = le.fit_transform(df_cleaned[col])

# Separate features and target
X = df_cleaned.drop(columns=['ValueCategory'])
y = df_cleaned['ValueCategory']

# Feature names for reference
feature_names = X.columns.tolist()

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, stratify=y, random_state=42)

# --- Train Models ---
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Support Vector Machine": SVC(),
    "Decision Tree": DecisionTreeClassifier()
}

for name, model in models.items():
    print(f"\n\n🔹 {name}")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# --- Plot Value Category Distribution ---
plt.figure(figsize=(8, 5))
sns.countplot(data=df_cleaned, x='ValueCategory', palette='viridis')
plt.title("Player Value Category Distribution")
plt.xlabel("Value Category")
plt.ylabel("Number of Players")
plt.tight_layout()
plt.show()

# --- Feature Importance (Decision Tree only) ---
dt_model = models["Decision Tree"]
importances = dt_model.feature_importances_
feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
feat_imp.head(15).plot(kind='barh', color='teal')
plt.title("Top 15 Feature Importances (Decision Tree)")
plt.xlabel("Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
