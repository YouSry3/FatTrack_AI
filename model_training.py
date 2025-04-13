import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# تحميل البيانات
df = pd.read_csv('bodyfat.csv')


# processing the data
X = df[['Weight', 'Height', 'Age']]
y = df['BodyFat']

# Training the model
model = LinearRegression()
model.fit(X, y)

# Save the model in "model.pkl"
joblib.dump(model, 'model.pkl')
