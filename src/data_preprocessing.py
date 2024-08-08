# data_preprocessing.py

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from config import DB_PATH, PUBLIC_DATA_PATH

#Script will be able to process two specific types of datasets
#Use a flag to distinguish between processing the private dataset and the public dataset.

def load_data(use_public_data=False, db_path=DB_PATH):
    if use_public_data:
        # Load the public dataset
        df = pd.read_csv(PUBLIC_DATA_PATH, header=None)
        # Assuming last column is the label for spambase dataset
        df.columns = [f'feature_{i}' for i in range(1, df.shape[1])] + ['label']
        return df
    else:
        # Load data from the SQLite database
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM calls"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

def preprocess_data(df, use_public_data=False):
    if use_public_data:
        # For the public dataset (spambase)
        X = df.drop('label', axis=1)
        y = df['label']
        # No need to perform further preprocessing for the spambase dataset
        return X, y, X.columns
    else:
        # Handle negative values in 'Call Duration' and 'Financial Loss' by taking the absolute value
        df['Call Duration'] = df['Call Duration'].abs()
        df['Financial Loss'] = df['Financial Loss'].abs()

        # Convert 'Timestamp' to datetime, and 'Scam Call' to a binary variable
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Scam Call'] = df['Scam Call'].map({'Scam': 1, 'Not Scam': 0})
        
        # Calculate the median of financial loss - outside of the fillna operation
        financial_loss_median = df['Financial Loss'].median()
        # Use .loc to ensure the operation affects the original DataFrame
        df.loc[:, 'Financial Loss'] = df['Financial Loss'].fillna(financial_loss_median)
        df['Hour of Day'] = df['Timestamp'].dt.hour

        # Define categorical and numeric features
        categorical_features = ['Flagged by Carrier', 'Is International', 'Country Prefix', 'Call Type', 'Device Battery']
        numeric_features = ['Call Duration', 'Call Frequency', 'Financial Loss', 'Previous Contact Count', 'Hour of Day']

        # Create transformers for numeric and categorical data
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        # Combine into a single preprocessor
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        # Fit the preprocessor and transform the data
        X_preprocessed = preprocessor.fit_transform(df.drop('Scam Call', axis=1))
        
        # Get the feature names from the preprocessor
        try:
            feature_names = preprocessor.get_feature_names_out()
        except AttributeError:  # For scikit-learn versions prior to 0.24
            feature_names = [f'x{i}' for i in range(X_preprocessed.shape[1])]
        
        # Return both the preprocessed data and the feature names
        return X_preprocessed, df['Scam Call'], feature_names
