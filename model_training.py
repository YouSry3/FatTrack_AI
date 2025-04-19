import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import joblib
import os

# إنشاء مجلد static إذا لم يكن موجوداً
if not os.path.exists('static'):
    os.makedirs('static')

try:
    # تحميل البيانات
    df = pd.read_csv('bodyfat.csv')
    X = df[['Weight', 'Height', 'Age']]
    y = df['BodyFat']

    # 1. تدريب النموذج بدون PCA
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'model_no_pca.pkl')
    print("تم حفظ model_no_pca.pkl بنجاح")

    # 2. رسم البيانات قبل PCA
    plt.figure(figsize=(10, 6))
    plt.scatter(X['Weight'], X['Height'], c=y, cmap='viridis')
    plt.title("Features Before PCA")
    plt.xlabel("Weight (lbs)")
    plt.ylabel("Height (inches)")
    plt.colorbar(label='Body Fat %')
    plt.savefig("static/before_pca.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("تم حفظ before_pca.png")

    # 3. تطبيق PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    joblib.dump(pca, 'pca.pkl')
    print("تم حفظ pca.pkl بنجاح")

    # 4. رسم البيانات بعد PCA
    plt.figure(figsize=(10, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
    plt.title("Features After PCA")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.colorbar(label='Body Fat %')
    plt.savefig("static/after_pca.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("تم حفظ after_pca.png")

    # 5. تدريب النموذج على بيانات PCA
    model_pca = LinearRegression()
    model_pca.fit(X_pca, y)
    joblib.dump(model_pca, 'model_with_pca.pkl')
    print("تم حفظ model_with_pca.pkl بنجاح")

except Exception as e:
    print(f"حدث خطأ: {str(e)}")