
---

```markdown
<h1 align="center">🏅 Sports Performance Prediction</h1>

<p align="center">
  <img src="https://github.com/TahaMazhar01/sports-performance-prediction/raw/main/banner.png" alt="Sports ML Banner" width="100%">
</p>

<p align="center"><strong>
  Machine learning powered web dashboard for predicting football player market value and wage.
</strong><br>
Built with <code>scikit-learn</code>, <code>Streamlit</code>, <code>pandas</code>, and deployed using Streamlit Cloud.
</p>

<p align="center">
  <a href="https://github.com/TahaMazhar01/sports-performance-prediction">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/TahaMazhar01/sports-performance-prediction?style=social">
  </a>
  <a href="https://github.com/TahaMazhar01/sports-performance-prediction/fork">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/TahaMazhar01/sports-performance-prediction?style=social">
  </a>
  <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-blue?style=flat">
  <img alt="Streamlit" src="https://img.shields.io/badge/Deployed%20on-Streamlit-red?style=flat">
</p>

---

## 📌 Project Overview

This project uses real-world football player stats to predict:

- 💰 **Player Market Value**
- 💸 **Player Wage**

It uses a visually interactive **Streamlit dashboard** for live predictions.

---

## ⚙️ Machine Learning Models Used

| Model            | Purpose                                  |
|------------------|-------------------------------------------|
| 🔍 Decision Tree | Final deployed model (best accuracy)      |
| 🌲 Random Forest | Ensemble model for comparative testing    |
| 📈 Linear Reg.   | Baseline model for wage/value prediction  |

> Final model: **DecisionTreeRegressor** after evaluating all three models.

---

## 📁 Folder Structure

```

sports-performance-prediction/
│
├── dashboard.py               # Streamlit app
├── train\_model.py            # Model training logic
├── sports\_value\_prediction.py
├── decision\_tree\_model.joblib
├── scaler.joblib
├── fifa\_eda\_stats.csv        # Cleaned dataset
├── requirements.txt
└── README.md

````

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/TahaMazhar01/sports-performance-prediction.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run dashboard.py
````

---

## 🌐 Live Deployment

Hosted on **Streamlit Cloud**:
🔗 [https://sports-performance-prediction.streamlit.app](https://sports-performance-prediction.streamlit.app) *(replace with your link)*

---

## 🧠 Features

* Interactive sidebar inputs for predictions
* Data preprocessing + scaling
* EDA-ready dataset
* Easy to extend with new models
* Real-time prediction interface

---

## 🧑‍💻 Author

Made with ❤️ by [**TahaMazhar01**](https://github.com/TahaMazhar01)

---

```

✅ Now it will display perfectly on GitHub — banners, badges, emojis, and proper formatting.

Let me know if you want to add:
- 📊 Graphs/screenshots
- 📽️ Demo GIF/video
- 🧪 Unit test details
- 📂 Link to datasets or Kaggle

I'll be happy to enhance it further!
```
