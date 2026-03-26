import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("../data/sales_data.csv")

# Preprocessing
df['status'] = df['status'].map({'Laris': 1, 'Tidak': 0})

X = df[['jumlah_penjualan', 'harga', 'diskon']]
y = df['status']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Save model
joblib.dump(model, "model.joblib")

print("Model saved!")