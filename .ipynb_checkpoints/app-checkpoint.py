import json
import numpy as np
from pod_predictor.inference import PODPredictor

def load_X_test_from_json(file_path):
    with open(file_path, 'r') as file:
        X_test = json.load(file)
    
    for key in X_test:
        X_test[key] = [np.nan if x is None else x for x in X_test[key]]
        X_test[key] = [np.nan] if X_test[key]==[] else X_test[key]
    
    return X_test

def pod_prediction(X_test):
    model = PODPredictor()
    (mean, intervals), feature_importance = model.predict_proba(X_test)
    results = []
    for (mean, intervals) in zip(100*mean, 100*intervals):
        results.append(f'{mean[1]:.0f}% [95% CI: {intervals[0]:.0f}-{intervals[1]:.0f}%]')
    return results, feature_importance

def main():
    X_test = load_X_test_from_json('./data/X_test.json')
    results, feature_importance = pod_prediction(X_test)
    for i in range(len(results)):
        print('POD Probability: ', results[i])
        print('Feature Importance:')
        print(np.round(feature_importance.iloc[i].sort_values(ascending=False),2))
        print()
        

if __name__ == "__main__":
    main()
