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
    try:
        # الحصول على المدخلات من المستخدم (الوزن والطول والعمر)
        weight = float(request.form['weight'])  # kg
        height = float(request.form['height'])  # cm
        age = int(request.form['age'])  # Years

        # التحقق من أن المدخلات صحيحة (قيم موجبة)
        if weight <= 0 or height <= 0 or age <= 0:
            return render_template("result.html", fat="Invalid input. Please enter positive values.")

        # تحويل الوزن والطول إلى الوحدات المطلوبة
        weight_lbs = weight * 2.20462
        height_inches = height * 0.393701

        # إجراء التنبؤ
        prediction = model.predict(np.array([[weight_lbs, height_inches, age]]))
        fat_percent = round(prediction[0], 2)

        # التحقق من أن نسبة الدهون في الجسم معقولة (بين 0 و 100)
        if fat_percent < 0:
            fat_percent = 0
        elif fat_percent > 100:
            fat_percent = 100

        # عرض النتيجة
        return render_template("index.html", fat=fat_percent)

    except ValueError:
        return render_template("result.html", fat="Please enter valid numeric values.")

if __name__ == '__main__':
    app.run(debug=True)
