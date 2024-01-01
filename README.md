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

## CI/CD Pipeline

This project includes a CI/CD pipeline using GitHub Actions. The pipeline automatically runs tests and checks code quality on every push and pull request, ensuring the application remains reliable and maintainable. The workflow is defined in `.github/workflows/python-app.yml` and includes steps to:
- Set up Python
- Install dependencies
- Run tests (if available)
- Check code formatting and linting

## Data Extraction

The dataset used for training the loan approval model was extracted using Python libraries `requests` and `BeautifulSoup`. These tools enabled automated web scraping and data collection from relevant sources, ensuring a robust and diverse dataset for model training. The extraction process involved:

- Sending HTTP requests to target websites using `requests`.
- Parsing HTML content with `BeautifulSoup` to extract structured data.
- Cleaning and preprocessing the extracted data to prepare it for model training.

## Model Training and Development

After data extraction, the following steps were performed to develop the loan approval prediction model:

- **Data Preprocessing:** Handling missing values, encoding categorical variables, and scaling numerical features.
- **Feature Engineering:** Creating new features to improve model performance.
- **Model Training:** Training an XGBoost model on the preprocessed dataset.
- **Model Evaluation:** Evaluating the model using metrics such as accuracy, precision, recall, and F1-score.
- **Model Deployment:** Deploying the trained model as a Flask web application for real-time predictions.

## Credits

This project was developed by Ankur as part of Machine Learning project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
