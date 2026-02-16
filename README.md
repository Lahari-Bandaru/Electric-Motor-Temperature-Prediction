# Electric Motor Temperature Prediction using Machine Learning
#📌 Project Overview

This project focuses on predicting the Permanent Magnet (PM) temperature of an electric motor using machine learning techniques. The system takes real-time or manual sensor inputs such as voltage, current, ambient temperature, motor speed, and other electrical parameters to predict the PM temperature.

The goal of this project is to:
Improve thermal monitoring of electric motors
Prevent overheating and system failure
Demonstrate end-to-end ML deployment (Training → Model Saving → Web App Deployment)
This project was developed as part of my Final Internship Project.

#📊 Features Used

The model was trained using the following 8 input features:
Ambient Temperature
Coolant Temperature
Direct Axis Voltage (u_d)
Quadrature Axis Voltage (u_q)
Motor Speed
Direct Axis Current (i_d
Quadrature Axis Current (i_q)
Torque

🔹 Target Variable:
Permanent Magnet Temperature (PM Temperature)
Note: The input values are normalized according to the dataset. Units are not considered in prediction.

#⚙️ Technologies Used
🐍 Programming Language
Python 3.x

📚 Libraries
NumPy
Pandas
Scikit-learn
Matplotlib / Seaborn (for visualization)
Pickle (for model saving)

🌐 Deployment
Flask (Backend Web Framework)
HTML (Frontend Forms)
Jinja2 Templates

🛠 Tools
Jupyter Notebook
VS Code

#🌐 Web Application Features
The Flask web application includes:

📝 Manual Prediction Page
Allows users to enter motor parameters manually.

📡 Sensor Prediction Page
Designed for real-time sensor input simulation.

🔮 Predict Button
Displays the predicted PM Temperature instantly.

#🚀 Project Workflow
Data Collection
Data Preprocessing & Normalization
Model Training
Model Evaluation
Model Saving (pickle)
Flask App Development
Deployment Interface
