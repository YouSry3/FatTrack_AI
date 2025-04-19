from flask import Flask, render_template, request
import joblib
import numpy as np
import os

from sklearn.decomposition import PCA

app = Flask(__name__)

# التأكد من وجود النماذج
if not all(os.path.exists(f) for f in ['model_no_pca.pkl', 'model_with_pca.pkl', 'pca.pkl']):
    raise FileNotFoundError("تأكد من أنك شغلت ملف model-Trining.py أولاً لإنشاء النماذج!")

# تحميل النماذج والـ PCA
model_no_pca = joblib.load("model_no_pca.pkl")
model_with_pca = joblib.load("model_with_pca.pkl")
pca = joblib.load("pca.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        weight = request.form.get('weight')
        height = request.form.get('height')
        age = request.form.get('age')

        # التحقق من أن كل القيم موجودة وصحيحة
        if not weight or not height or not age:
            return render_template("index.html", error="الرجاء ملء جميع الحقول.")

        weight = float(weight)
        height = float(height)
        age = int(age)

        if weight <= 0 or height <= 0 or age <= 0:
            return render_template("index.html", error="القيم يجب أن تكون موجبة!")

        # تحويل الوحدات من كجم/سم إلى باوند/إنش
        weight_lbs = weight * 2.20462
        height_inches = height * 0.393701

        input_data = np.array([[weight_lbs, height_inches, age]])

        # التنبؤ بدون PCA
        pred_no_pca = model_no_pca.predict(input_data)[0]

        # التنبؤ باستخدام PCA
        input_pca = pca.transform(input_data)
        pred_with_pca = model_with_pca.predict(input_pca)[0]

        return render_template(
            "index.html",
            pred_no_pca=round(pred_no_pca, 2),
            pred_with_pca=round(pred_with_pca, 2),
            before_pca_img="static/before_pca.png",
            after_pca_img="static/after_pca.png",
            fat=round(pred_no_pca, 2)
        )

    except ValueError:
        return render_template("index.html", error="القيم المدخلة غير صالحة، يرجى إدخال أرقام فقط.")
    except Exception as e:
        return render_template("index.html", error=f"حدث خطأ غير متوقع: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
