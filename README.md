# Loan Approval Prediction

This project predicts loan approval using a machine learning model implemented with Flask.

## Overview

The loan approval prediction model is built using XGBoost and deployed as a web application using Flask. Users can input various parameters related to loan applications, and the model will predict whether the loan will be approved or not based on historical data.

## Features

- Accepts user input for loan application details.
- Utilizes an XGBoost model trained on historical loan data.
- Displays the predicted loan approval outcome.

## Project Structure

The project directory contains the following files and folders:

- `artifacts/`: Directory containing model artifacts and data files.
- `model/`: Directory for storing the trained machine learning model.
- `static/`: Static assets such as CSS, JavaScript, or images.
- `templates/`: HTML templates for the Flask application.
- `app.py`: Main Flask application script.
- `LoanPredict.ipynb`: Jupyter Notebook for model training and development.
- `Procfile`: Heroku Procfile for deployment.
- `README.md`: Project documentation.
- `requirements.txt`: File listing required Python packages for the project.
- `runtime.txt`: File specifying Python runtime version.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AnkurMangroliya/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction
```

### 2. Set Up a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat  # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

Open a web browser and go to `http://localhost:5000` to access the application.

## Input Parameters

Users can input the following parameters into the web form for loan approval prediction:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History (1 for paid, 0 for not paid)
- Property Area

## Additional Notes

- Ensure all input values are provided in the correct format for accurate predictions.
- The machine learning model used for prediction is based on XGBoost.
- Feel free to explore and modify the project structure and code to suit your needs.

## Credits

This project was developed by Ankur as part of Machine Learning project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
