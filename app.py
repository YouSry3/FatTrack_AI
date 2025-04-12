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
    # الحصول على المدخلات من المستخدم
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    # توقع نسبة الدهون
    prediction = model.predict(np.array([[weight, height]]))
    fat_percent = round(prediction[0], 2)

    return render_template("result.html", fat=fat_percent)

if __name__ == '__main__':
    app.run(debug=True)
