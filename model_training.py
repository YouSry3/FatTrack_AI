import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# تحميل الداتا
df = pd.read_csv("bodyfat.csv")

# تحديد المدخلات والمخرجات
X = df[["Weight", "Height"]]
y = df["BodyFat"]

# تدريب الموديل
model = LinearRegression()
model.fit(X, y)

# حفظ الموديل المدرب
joblib.dump(model, "model.pkl")
