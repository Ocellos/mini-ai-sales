from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# ======================
# CONFIG JWT
# ======================
SECRET_KEY = "secret123"
ALGORITHM = "HS256"

# ======================
# CORS
# ======================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# LOAD MODEL & DATA
# ======================
MODEL_PATH = os.path.join("..", "ml", "model.joblib")
DATA_PATH = os.path.join("..", "data", "sales_data.csv")

model = joblib.load(MODEL_PATH)

def get_data():
    return pd.read_csv(DATA_PATH)

# ======================
# REQUEST SCHEMA
# ======================
class LoginRequest(BaseModel):
    username: str
    password: str

class PredictRequest(BaseModel):
    jumlah_penjualan: float
    harga: float
    diskon: float

# ======================
# ROUTES
# ======================
@app.get("/")
def root():
    return {"message": "API is running"}

# 🔐 LOGIN (JWT)
@app.post("/login")
def login(data: LoginRequest):
    if data.username != "admin" or data.password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "sub": data.username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token}

# 📊 GET SALES
@app.get("/sales")
def get_sales():
    try:
        df = get_data()
        return df.to_dict(orient="records")
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to load data")

# 🤖 PREDICT
@app.post("/predict")
def predict(data: PredictRequest):
    try:
        input_data = [[
            data.jumlah_penjualan,
            data.harga,
            data.diskon
        ]]

        pred = model.predict(input_data)[0]

        return {
            "prediction": "Laris" if pred == 1 else "Tidak"
        }

    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed")