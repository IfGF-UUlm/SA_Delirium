import json
import numpy as np
from pod_predictor.inference import PODPredictor


def load_X_test_from_json(file_path):
    """
    Load test data from a JSON file and preprocess it.

    Args:
    file_path (str): The file path of the JSON file containing the test data.

    Returns:
    dict: A dictionary containing the preprocessed test data.
    """
    with open(file_path, 'r') as file:
        X_test = json.load(file)

    for key in X_test:
        X_test[key] = [np.nan if x is None else x for x in X_test[key]]
        X_test[key] = [np.nan] if X_test[key] == [] else X_test[key]

    return X_test


def pod_prediction(X_test):
    """
    Predict the probability of postoperative delirium (POD) for the given test data.

    Args:
    X_test (np.ndarray, pd.DataFrame, or dict): The test data to predict the probability of POD for.

    Returns:
    pandas.DataFrame: A DataFrame containing the formatted probability estimates as strings in the 'Delirium Probability' column,
                      along with the feature importance.
    """

    model = PODPredictor(calibration='va')
    report = model.get_report(X_test)
    report = np.round(report, 2)
    report['Delirium Probability'] = report.apply(
        lambda row: f"{row.iloc[0]*100:.0f}% [{row.iloc[1]*100:.0f}-{row.iloc[2]*100:.0f}%]", axis=1)

    return report


def main():
    """
    Load test data, predict the probability of postoperative delirium (POD), and print the results, along with the feature importance.

    Returns:
    None
    """

    X_test = load_X_test_from_json('./data/X_test.json')
    report = pod_prediction(X_test)
    for _, row in report.iterrows():
        print(row[:1].to_frame(name='Prediction [CI]'))
        print(row[3:].sort_values(ascending=False).to_frame(name='Feature Importance'))

if __name__ == "__main__":
    main()
