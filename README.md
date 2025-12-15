# 🚗 Car Price Prediction Web App

A machine learning–based web application that predicts the selling price of a car based on user inputs such as year, kilometers driven, fuel type, seller type, and transmission.

The application is built using Streamlit and deployed on Render.

---

## 🌐 Live Demo
👉 Live App: https://car-price-prediction-3n4m.onrender.com

Note: The app may take a few seconds to load on first access because it is hosted on Render's free tier.

---

## 🧠 Problem Statement
Buying or selling a used car often involves uncertainty in pricing. This project aims to reduce that uncertainty by using a machine learning model to estimate a fair car price based on historical data.

---

## ⚙️ Tech Stack
- Programming Language: Python
- Web Framework: Streamlit
- Machine Learning: Scikit-learn
- Data Handling: Pandas, NumPy
- Deployment Platform: Render

---

## 📂 Project Structure

Car_prediction/
│
├── app.py               # Streamlit application
├── model.pkl            # Trained machine learning model
├── Cardetails.csv       # Dataset used for training
├── requirements.txt     # Project dependencies
├── runtime.txt          # Python version             
└── README.md            # Project documentation

---

## 🔍 Features
- Interactive user interface
- Real-time car price prediction
- Lightweight and efficient ML model
- Cloud deployed and accessible from anywhere

---

## ▶️ How to Run Locally

1. Clone the repository:
   git clone https://github.com/Lisha-Rani/Car-Price-Prediction.git
   cd Car_prediction

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

4. Open your browser and visit:
   http://localhost:8501

---

## 📊 Model Information
- Algorithm: Regression Model (Scikit-learn)
- Input Features:
  - Car Year
  - Kilometers Driven
  - Fuel Type
  - Seller Type
  - Transmission

- Output:
  - Predicted Selling Price

---

## 🚀 Deployment
The application is deployed on Render using:
- requirements.txt for dependencies
- runtime.txt for Python version
- Procfile for Streamlit startup command

---

## 📌 Future Improvements
- Add more input features (engine size, mileage, owner count)
- Improve UI design
- Display model accuracy and metrics
- Support multiple machine learning models

---

## 👩‍💻 Author
YASH VARDHAN RAJPOOT

---

## 📜 License
This project is created for educational purposes.
