# Titanic Survival Prediction

This project implements a machine learning model to predict the survival of passengers aboard the Titanic using the Titanic dataset. The model utilizes various preprocessing techniques and logistic regression to make predictions based on passenger characteristics.

## Project Overview

The Titanic dataset is a well-known dataset in data science and machine learning communities. It contains information about passengers, including their class, age, gender, fare, and other attributes. The goal of this project is to predict whether a passenger survived or not based on these features.

## Features

- **Data Preprocessing**: Handling missing values, outlier removal, and feature engineering (e.g., extracting titles from names and calculating family size).
- **Machine Learning Pipeline**: Utilizes `scikit-learn` for building a robust pipeline that includes data preprocessing and model training.
- **Logistic Regression**: Implements logistic regression for binary classification of survival.
- **Model Evaluation**: Uses accuracy score and cross-validation to assess model performance.
- **Model Serialization**: Saves the trained model using `pickle` for future predictions.
  ![image](https://github.com/user-attachments/assets/c53f8ecc-2071-4c3e-a955-ec0d7299c783)


## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Flask (for the web form, if applicable)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mohitkumhar/titanic_survival_prediction/
   ```
2. Navigate to the project directory:
   ```bash
   cd titanic_survival_prediction
   ```
3. Install the required packages:
   ```bash
   pip install -r ./requirements.txt
   ```

## Usage

1. Run the model training script to create and save the prediction model:
   ```bash
   jupyter notebook model_training_code/main.ipynb
   ```
2. To use the web input method, run the Flask app:
    ```bash
    python app.py
    ```
3. Open your web browser and navigate to `http://127.0.0.1:5000` to access the prediction form.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository, create a new branch, and submit a pull request. Any improvements, suggestions, or bug fixes are appreciated!

## Acknowledgments

- The Titanic dataset is provided by [Kaggle](https://www.kaggle.com/datasets/hesh97/titanicdataset-traincsv).
- Special thanks to the data science community for their contributions to tutorials and resources.
