import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
import os

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# --------------------------------------------------
# Load Model Safely
# --------------------------------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
try:
    with open(MODEL_PATH, "rb") as f:
        model = pk.load(f)
    model_loaded = True
except FileNotFoundError:
    st.error(
        "❌ Model file `model.pkl` not found. "
        "Please make sure it is in the same directory as this app."
    )
    model_loaded = False
except Exception as e:
    st.error(f"❌ Error loading the model: {e}")
    model_loaded = False

# --------------------------------------------------
# App Header
# --------------------------------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #1f77b4;'>🚗 Car Price Prediction System</h1>
    <p style='text-align: center; font-size: 18px;'>
    Predict the selling price of a used car using Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)
st.divider()

# --------------------------------------------------
# Load Dataset Safely
# --------------------------------------------------
DATA_PATH = os.path.join(os.path.dirname(__file__), "Cardetails.csv")
try:
    cars_data = pd.read_csv(DATA_PATH)
    def get_brand_name(car_name):
        return car_name.split(" ")[0].strip()
    cars_data["name"] = cars_data["name"].apply(get_brand_name)
    dataset_loaded = True
except FileNotFoundError:
    st.error("❌ Dataset `Cardetails.csv` not found. Predictions may not work properly.")
    dataset_loaded = False
except Exception as e:
    st.error(f"❌ Error loading dataset: {e}")
    dataset_loaded = False

# --------------------------------------------------
# User Input Section (only if dataset loaded)
# --------------------------------------------------
if dataset_loaded:
    st.subheader("🛠️ Enter Car Details")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.selectbox("🚘 Car Brand", cars_data["name"].unique())
        year = st.slider("📅 Manufacturing Year", 1994, 2024)
        km_driven = st.slider("🛣️ Kilometers Driven", 11, 200000)
    with col2:
        fuel = st.selectbox("⛽ Fuel Type", cars_data["fuel"].unique())
        seller_type = st.selectbox("🏪 Seller Type", cars_data["seller_type"].unique())
        transmission = st.selectbox("⚙️ Transmission", cars_data["transmission"].unique())
    
    st.divider()
    
    col3, col4 = st.columns(2)
    with col3:
        owner = st.selectbox("👤 Ownership Type", cars_data["owner"].unique())
        mileage = st.slider("📊 Mileage (km/l)", 10, 40)
    with col4:
        engine = st.slider("🔧 Engine Capacity (CC)", 700, 5000)
        max_power = st.slider("⚡ Max Power (bhp)", 0, 200)
        seats = st.slider("💺 Number of Seats", 4, 8)
    
    st.divider()

    # --------------------------------------------------
    # Prediction (only if model loaded)
    # --------------------------------------------------
    if model_loaded:
        if st.button("🔍 Predict Car Price"):
            input_data = pd.DataFrame(
                [[
                    name, year, km_driven, fuel, seller_type,
                    transmission, owner, mileage, engine,
                    max_power, seats
                ]],
                columns=[
                    "name", "year", "km_driven", "fuel",
                    "seller_type", "transmission", "owner",
                    "mileage", "engine", "max_power", "seats"
                ]
            )

            # Encoding categorical variables
            input_data["owner"].replace(
                ["First Owner", "Second Owner", "Third Owner",
                 "Fourth & Above Owner", "Test Drive Car"],
                [1, 2, 3, 4, 5],
                inplace=True
            )
            input_data["fuel"].replace(
                ["Diesel", "Petrol", "LPG", "CNG"],
                [1, 2, 3, 4],
                inplace=True
            )
            input_data["seller_type"].replace(
                ["Individual", "Dealer", "Trustmark Dealer"],
                [1, 2, 3],
                inplace=True
            )
            input_data["transmission"].replace(
                ["Manual", "Automatic"],
                [1, 2],
                inplace=True
            )
            input_data["name"].replace(
                [
                    "Maruti", "Skoda", "Honda", "Hyundai", "Toyota", "Ford",
                    "Renault", "Mahindra", "Tata", "Chevrolet", "Datsun",
                    "Jeep", "Mercedes-Benz", "Mitsubishi", "Audi",
                    "Volkswagen", "BMW", "Nissan", "Lexus", "Jaguar",
                    "Land", "MG", "Volvo", "Daewoo", "Kia", "Fiat",
                    "Force", "Ambassador", "Ashok", "Isuzu", "Opel"
                ],
                list(range(1, 32)),
                inplace=True
            )

            # Prediction
            try:
                car_price = model.predict(input_data)
                st.success(f"💰 Estimated Car Price: ₹ {car_price[0]:,.2f}")
            except Exception as e:
                st.error(f"❌ Prediction failed: {e}")
    else:
        st.warning("⚠️ Model not loaded. Cannot make predictions.")
else:
    st.warning("⚠️ Dataset not loaded. Cannot select car details.")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <p style='text-align:center;'>
    👨‍💻 Developed by <b>Yash Vardhan Rajpoot</b><br>
    Pre-Final Year CSE Undergraduate @ NIT Patna
    </p>
    """,
    unsafe_allow_html=True
)
