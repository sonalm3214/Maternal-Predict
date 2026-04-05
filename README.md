# 🩺 MaternalPredict

**MaternalPredict** is a machine learning-powered web application that helps assess **pregnancy risk** and **fetal health conditions** using medical data.
Built with **Streamlit**, it provides an interactive interface for predictions and data visualization.

---

## 🚀 Features

* 📊 **Pregnancy Risk Prediction**

  * Predicts risk level (Low, Medium, High)
  * Based on vital health parameters

* ❤️ **Fetal Health Prediction**

  * Classifies fetal condition (Normal, Suspect, Pathological)
  * Uses CTG (Cardiotocography) data

* 📈 **Interactive Dashboard**

  * Visualizes maternal health data
  * Includes charts and insights

* 🎨 **Modern UI**

  * Clean and responsive interface
  * Styled homepage with metrics and visuals

---

## 🧠 Machine Learning Models

* Maternal Risk Model (trained on medical dataset)
* Fetal Health Classifier
* Feature scaling applied using Standard Scaler

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **ML Libraries:** scikit-learn, NumPy
* **Visualization:** Streamlit charts / custom dashboard
* **Data Source:** data.gov.in API (for dashboard)

---

## 📂 Project Structure

```
MaternalPredict/
│── model/
│   ├── finalized_maternal_model.sav
│   ├── fetal_health_classifier.sav
│   ├── scaler_maternal_model.sav
│
│── codebase/
│   └── dashboard_graphs.py
│
│── main.py
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the application

```bash
streamlit run main.py
```

---

## 📊 Usage

1. Open the app in browser (`localhost:8501`)
2. Navigate using sidebar:

   * About Us
   * Pregnancy Risk Prediction
   * Fetal Health Prediction
   * Dashboard
3. Enter medical values
4. Click **Predict** to view results

---

## ⚠️ Notes

* Dashboard API may sometimes be unavailable (fallback data recommended)
* Ensure model files (`.sav`) are present in `/model` folder

---

## 🔮 Future Improvements

* Deploy app online (Streamlit Cloud / Render)
* Add real-time data integration
* Improve model accuracy
* Add user authentication
* Advanced visualizations (Plotly)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is for educational purposes.

---

