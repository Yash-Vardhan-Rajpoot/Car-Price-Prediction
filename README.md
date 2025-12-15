🚗 Car Price Prediction Web App

A machine learning–based web application that predicts the selling price of a car based on user inputs such as manufacturing year, kilometers driven, fuel type, seller type, and transmission.

The application is built using **Streamlit** and deployed on **Render**.

🌐 Live Demo
👉 Live App: [https://car-price-prediction-udlw.onrender.com/](https://car-price-prediction-udlw.onrender.com/)

> Note: The app may take a few seconds to load on first access because it is hosted on Render's free tier.

🧠 Problem Statement
Buying or selling a used car often involves uncertainty in pricing. This project aims to reduce that uncertainty by leveraging a machine learning regression model trained on historical car data to estimate a fair selling price.

⚙️ Tech Stack

* Programming Language: Python
* Web Framework: Streamlit
* Machine Learning: Scikit-learn
* Data Handling: Pandas, NumPy
* Deployment Platform: Render

📂 Project Structure

```
car price prediction project/
│
├── Cardetails.csv      # Dataset used for training
├── app.py              # Streamlit web application
├── model.pkl           # Trained ML model
├── requirements.txt    # Project dependencies
```

🔍 Features

* Interactive and user-friendly UI
* Real-time car price prediction
* Lightweight and efficient regression model
* Cloud deployed and accessible from anywhere

▶️ How to Run Locally

1. Clone the repository:

   ```bash
   git clone <your-github-repo-link>
   cd "car price prediction project"
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open your browser and visit:

   ```
   http://localhost:8501
   ```

📊 Model Information

* Algorithm: Regression Model (Scikit-learn)

Input Features:

* Car Year
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission

Output:

* Predicted Selling Price

🚀 Deployment
The application is deployed on **Render** using:

* `requirements.txt` for dependency management
* Streamlit as the web service

📌 Future Improvements

* Add more input features (engine size, mileage, owner count)
* Enhance UI/UX design
* Display model performance metrics
* Support multiple ML models for comparison

👨‍💻 Author
**Yash Vardhan Rajpoot**
Pre-Final Year CSE Undergraduate @ NIT Patna

📜 License
This project is created for educational and learning purposes.
