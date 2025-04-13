from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# تحميل الموديل المدرب
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    # Get user input (in kg and cm)
    weight = float(request.form['weight'])  # kg
    height = float(request.form['height'])  # cm

    # Convert to lbs and inches
    weight_lbs = weight * 2.20462
    height_inches = height * 0.393701

    # Predict fat percentage
    prediction = model.predict(np.array([[weight_lbs, height_inches]]))
    fat_percent = round(prediction[0], 2)

    return render_template("result.html", fat=fat_percent)


if __name__ == '__main__':
    app.run(debug=True)
