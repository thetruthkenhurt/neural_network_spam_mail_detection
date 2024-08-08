# Spam Mail Classification

This project aims to classify spam mails using machine learning techniques. This project came about from an assignment originally focused on classifying scam calls from a private dataset, but I have repurposed the scripts I have written to classify spam mails using the [UCI Spambase dataset](https://archive.ics.uci.edu/ml/datasets/spambase).

## Project Overview

The goal of this project is to build and evaluate machine learning models to classify emails as spam or not spam. The project utilizes Logistic Regression, Random Forest, and XGBoost classifiers to perform the classification task.

## Directory Structure
```
Spam-Mail-Classification/
│
├── spambase/ # Public dataset folder
│
├── src/ # Source code folder
│ ├── config.py
│ ├── data_preprocessing.py
│ ├── feature_selection.py
│ ├── model_training.py
│ ├── main.py
│
├── Spam mail classification.ipynb # Jupyter Notebook for Exploratory Data Analysis
├── requirements.txt # List of dependencies
└── README.md # Project documentation
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/Spam-Mail-Classification.git
    cd Spam-Mail-Classification
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Pipeline

1. Ensure you have the public dataset (`spambase.data`) in the `spambase` folder.
2. Run the `main.py` script to execute the machine learning pipeline:
    ```bash
    cd src
    python main.py --use_public_data
    ```

### Jupyter Notebook

For detailed exploratory data analysis and insights, you can refer to the Jupyter Notebook `Spam mail classification.ipynb`:
- Open the notebook:
    ```bash
    jupyter notebook Spam\ mail\ classification.ipynb
    ```

## Scripts

- `config.py`: Configuration file for database paths and other constants.
- `data_preprocessing.py`: Script for loading and preprocessing the dataset.
- `feature_selection.py`: Script for feature selection (not heavily used in the current implementation).
- `model_training.py`: Script for training and evaluating different machine learning models.
- `main.py`: Main script to run the entire pipeline including data loading, preprocessing, model training, and evaluation.

## Results

### Logistic Regression
|            | precision | recall | f1-score | support |
|------------|-----------|--------|----------|---------|
| 0          | 0.92      | 0.95   | 0.93     | 531     |
| 1          | 0.93      | 0.88   | 0.91     | 390     |
| **accuracy** |           |        | 0.92     | 921     |
| **macro avg**    | 0.92  | 0.92   | 0.92     | 921     |
| **weighted avg** | 0.92  | 0.92   | 0.92     | 921     |

**Confusion Matrix**:
|                  | Predicted: No | Predicted: Yes |
|------------------|---------------|----------------|
| **Actual: No**   |      505      |       26       |
| **Actual: Yes**  |      46       |      344       |

### Random Forest
|            | precision | recall | f1-score | support |
|------------|-----------|--------|----------|---------|
| 0          | 0.94      | 0.98   | 0.96     | 531     |
| 1          | 0.97      | 0.92   | 0.94     | 390     |
| **accuracy** |           |        | 0.95     | 921     |
| **macro avg**    | 0.96  | 0.95   | 0.95     | 921     |
| **weighted avg** | 0.96  | 0.95   | 0.95     | 921     |

**Confusion Matrix**:
|                  | Predicted: No | Predicted: Yes |
|------------------|---------------|----------------|
| **Actual: No**   |      521      |       10       |
| **Actual: Yes**  |      32       |      358       |

### XGBoost
|            | precision | recall | f1-score | support |
|------------|-----------|--------|----------|---------|
| 0          | 0.95      | 0.98   | 0.96     | 531     |
| 1          | 0.97      | 0.94   | 0.96     | 390     |
| **accuracy** |           |        | 0.96     | 921     |
| **macro avg**    | 0.96  | 0.96   | 0.96     | 921     |
| **weighted avg** | 0.96  | 0.96   | 0.96     | 921     |

**Confusion Matrix**:
|                  | Predicted: No | Predicted: Yes |
|------------------|---------------|----------------|
| **Actual: No**   |      518      |       13       |
| **Actual: Yes**  |      25       |      365       |


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/spambase) for providing the Spambase dataset.

