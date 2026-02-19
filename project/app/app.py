from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("../notebook/model.save")
scaler = joblib.load("../notebook/transform.save")

# ---------------- HOME (Selection Page) ----------------
@app.route('/')
def home():
    return render_template("index.html")


# ---------------- MANUAL PAGE ----------------
@app.route('/manual')
def manual():
    return render_template("Manual_predict.html")


@app.route('/manual_predict', methods=['POST'])
def manual_predict():
    features = [
        float(request.form['ambient']),
        float(request.form['coolant']),
        float(request.form['u_d']),
        float(request.form['u_q']),
        float(request.form['motor_speed']),
        float(request.form['i_d']),
        float(request.form['i_q']),
        float(request.form['torque'])
    ]

    final_input = np.array([features])
    final_input_scaled = scaler.transform(final_input)
    prediction = model.predict(final_input_scaled)

    return render_template(
        "Manual_predict.html",
        prediction_text=f"Predicted PM Temperature: {prediction[0]:.2f}"
    )


# ---------------- SENSOR PAGE ----------------
@app.route('/sensor')
def sensor():
    return render_template("Sensor_predict.html")


@app.route('/sensor_predict', methods=['POST'])
def sensor_predict():
    features = [
        float(request.form['ambient']),
        float(request.form['coolant']),
        float(request.form['u_d']),
        float(request.form['u_q']),
        float(request.form['motor_speed']),
        float(request.form['i_d']),
        float(request.form['i_q']),
        float(request.form['torque'])
    ]

    final_input = np.array([features])
    final_input_scaled = scaler.transform(final_input)
    prediction = model.predict(final_input_scaled)

    return render_template(
        "Sensor_predict.html",
        prediction_text=f"Predicted PM Temperature: {prediction[0]:.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True)
