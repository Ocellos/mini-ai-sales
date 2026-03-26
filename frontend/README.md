# 🚀 Mini AI Sales Prediction System

## 📌 Deskripsi
Aplikasi fullstack sederhana untuk:
- Mengelola data penjualan
- Memprediksi status produk (**Laris / Tidak Laris**)
- Menampilkan hasil dalam dashboard interaktif

---

## ⚙️ Tech Stack
- **Frontend:** React JS
- **Backend:** FastAPI (Python)
- **Machine Learning:** Scikit-learn
- **Data Source:** CSV

---

## 🧠 Arsitektur Sistem
Frontend (React)  
↓  
Backend API (FastAPI)  
↓  
Machine Learning Model (Scikit-learn)  
↓  
Data (CSV)

---

## 🔐 Authentication
Endpoint:
POST /login

Dummy user:
username: admin  
password: admin  

Response:
```json
{
  "access_token": "JWT_TOKEN"
}

| Method | Endpoint | Description            |
| ------ | -------- | ---------------------- |
| POST   | /login   | Login & get JWT token  |
| GET    | /sales   | Get sales data         |
| POST   | /predict | Predict product status |

🚀 Cara Menjalankan
1. Backend
cd backend
pip install fastapi uvicorn pandas scikit-learn joblib python-jose
python -m uvicorn main:app --reload

Buka Swagger:
http://127.0.0.1:8000/docs

2. Frontend
cd frontend
npm install
npm start

Akses:
http://localhost:3000

## 📸 Screenshot

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Prediction Result
![Prediction](screenshots/predict.png)

### Swagger API
![Swagger](screenshots/swagger.png)