# main.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
from data_preprocessing import load_data, preprocess_data
from feature_selection import select_features
from model_training import train_logistic_regression, train_random_forest, train_xgboost, evaluate_model
from sklearn.model_selection import train_test_split
import argparse

def main(use_public_data=False):
    # Load data
    df = load_data(use_public_data=use_public_data)

    # Preprocess data
    X, y, feature_names = preprocess_data(df, use_public_data=use_public_data)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Logistic Regression
    print("Logistic Regression Results:")
    lr_model = train_logistic_regression(X_train, y_train)
    evaluate_model(lr_model, X_test, y_test)

    # Random Forest
    print("\nRandom Forest Results:")
    rf_model = train_random_forest(X_train, y_train)
    evaluate_model(rf_model, X_test, y_test)

    # XGBoost
    print("\nXGBoost Results:")
    xgb_model = train_xgboost(X_train, y_train)
    evaluate_model(xgb_model, X_test, y_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the ML pipeline.')
    parser.add_argument('--use_public_data', action='store_true', help='Use the public dataset instead of the private dataset')
    args = parser.parse_args()

    main(use_public_data=args.use_public_data)
