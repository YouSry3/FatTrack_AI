from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # give the user a message to enter the data)
        weight = float(request.form['weight'])  # kg
        height = float(request.form['height'])  # cm
        age = int(request.form['age'])  # Years

       # Check if the input values are valid
        if weight <= 0 or height <= 0 or age <= 0:
            return render_template("result.html", fat="Invalid input. Please enter positive values.")

        #  convert the input values to the required units
        weight_lbs = weight * 2.20462
        height_inches = height * 0.393701

        #  Make a prediction using the model
        prediction = model.predict(np.array([[weight_lbs, height_inches, age]]))
        fat_percent = round(prediction[0], 2)

        # Check if the prediction is within a valid range
        if fat_percent < 0:
            fat_percent = 0
        elif fat_percent > 100:
            fat_percent = 100

        # Show the result to the user
        return render_template("index.html", fat=fat_percent)

    except ValueError:
        return render_template("result.html", fat="Please enter valid numeric values.")

if __name__ == '__main__':
    app.run(debug=True)
