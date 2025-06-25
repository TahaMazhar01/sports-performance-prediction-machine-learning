

```markdown
<h1 align="center">
  🏆 Sports Performance Prediction
</h1>

<p align="center">
  <img src="https://github.com/TahaMazhar01/sports-performance-prediction/raw/main/banner.png" alt="Sports ML Banner" width="100%">
</p>

<p align="center">
  <strong>Machine learning powered web dashboard for predicting player market value and wage.</strong><br>
  Built with <code>scikit-learn</code>, <code>Streamlit</code>, <code>Pandas</code>, and deployed with Streamlit Cloud.
</p>

<p align="center">
  <a href="https://github.com/TahaMazhar01/sports-performance-prediction">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/TahaMazhar01/sports-performance-prediction?style=for-the-badge">
  </a>
  <a href="https://github.com/TahaMazhar01/sports-performance-prediction">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/TahaMazhar01/sports-performance-prediction?style=for-the-badge">
  </a>
  <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-blue.svg?style=for-the-badge">
</p>

---

## 🚀 Overview

This project predicts the **Value (in Euros)** and **Wage (in Euros)** of football players using a supervised machine learning model. A professional, interactive **Streamlit dashboard** is included for visualizing predictions and insights.

### 🎯 Objectives
- Predict player performance metrics like market value and wage.
- Explore and visualize sports dataset features.
- Offer a user-friendly web interface for demo or evaluation.

---

## 🧠 Machine Learning Approach

- **Model**: Decision Tree Regressor
- **Target Variables**: 
  - `Value (in Euro)`
  - `Wage (in Euro)`
- **Features Used**: Age, Overall rating, Potential, International reputation, etc.
- **Preprocessing**: Null value handling, Euro/K string cleaning, standardization with `StandardScaler`

---

## 📊 Dashboard Features

- 📈 Visual plots (bar, line, correlation heatmap)
- 📂 Input sliders for custom predictions
- 📉 Predicted value and wage display
- 🌗 Dark/light theme ready
- 📱 Fully mobile responsive UI

---

## 🗂️ Project Structure

```

sports-performance-prediction/
├── sports-performance-perdiction/
│   ├── dashboard.py             # Streamlit dashboard app
│   ├── train\_model.py           # Training and exporting ML model
│   ├── decision\_tree\_model.joblib
│   ├── scaler.joblib
│   ├── data.csv                 # Cleaned dataset
├── .streamlit/                  # Streamlit config
│   └── config.toml
├── requirements.txt
├── README.md
└── LICENSE

````

---

## 🛠️ Installation

```bash
# Clone repo
git clone https://github.com/TahaMazhar01/sports-performance-prediction.git
cd sports-performance-prediction/sports-performance-perdiction

# Setup virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r ../requirements.txt

# Run locally
streamlit run dashboard.py
````

---

## 🌐 Live Demo

🔗 [View on Streamlit Cloud](https://sports-performance-prediction.streamlit.app/)
*(If broken, check back after deployment refresh)*

---

## 📸 Screenshots

![Dashboard Preview](https://github.com/TahaMazhar01/sports-performance-prediction/raw/main/sports-performance-perdiction/preview.png)

---

## 🙋‍♂️ Author

Made with ❤️ by [TahaMazhar01](https://github.com/TahaMazhar01)

---

## 📄 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.

```

---

### ✅ Notes:

- Add a **banner image** `banner.png` and a **dashboard screenshot** `preview.png` into your repository.
- Make sure your `decision_tree_model.joblib` and `scaler.joblib` are inside the `sports-performance-perdiction/` folder.

Let me know if you want a dark-themed version of this README, a PDF export, or anything else added!
```
