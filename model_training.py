import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load Data Set that Download from Kalgge
df = pd.read_csv("bodyfat.csv")

# Select Features and Target Variable
X = df[["Weight", "Height"]]
y = df["BodyFat"]

# Tranning Model by Linear Regression
model = LinearRegression()
model.fit(X, y)

# حفظ الموديل المدرب
joblib.dump(model, "model.pkl")
