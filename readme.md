# Post-Operative Delirium Prediction Model
This GitHub repository contains the source code for the SA_Delirium library, a Python package predicting post-operative delirium (POD) in older patients undergoing surgery.

## Project Overview
The SURGE-Ahead (Supporting Surgery with Geriatric Co-Management and AI) aims to develop a robust algorithm that uses explainable machine learning techniques to predict POD in geriatric patients. We provide an easy-to-use interface for loading data, preprocessing input features, imputing missing values, calibrating models, and generating predictions.

## Features
The SA_Delirium library offers the following key features:
- **Standard POD Prediction**: Our library provides a robust algorithm for probabilistic POD prediction in geriatric patients undergoing surgery.
- **Feature Importance Calculation**: Understand the impact of individual input features on POD predictions with our built-in feature importance analysis.
- **Calibration**: The model is pre-calibrated on a diverse patient dataset using Platt Scaling; however, we also provide options for re-calibrating the model using Platt scaling or Venn-ABERS. This allows for adaptation to changing patient populations and optimization of performance in the face of distribution shifts.
- **Handling of Missing Values**: SA_Delirium includes flexible imputation tools to address missing data points, ensuring more accurate predictions. Choose from simple imputation methods (mean, median, mode) based on the training dataset or utilize the KNNImputer for more sophisticated handling of missing values.

## Project Structure
The repository has the following structure:
- [`data`](./data/): Calibration dataset template ([`calibration_template.csv`](./data/calibration_template.csv)), data transfer template ([`X_test_template.json`](./data/X_test.json)) and sample files ([`calibration.csv`](./data/calibration.csv), [`X_test.json`](./data/X_test_template.json))
- [`examples`](./examples/): Jupyter notebooks demonstrating usage examples for (multiple) calibrated prediction ([`Calibrated_Prediction.ipynb`](./examples/Calibrated_Prediction.ipynb), [`Multiple_Calibrated_Predictions.ipynb`](./examples/Multiple_Calibrated_Predictions.ipynb)), imputation ([`Imputation.ipynb`](./examples/Imputation.ipynb)), and ROC-AUC analysis ([`ROC_AUC.ipynb`](./examples/ROC_AUC.ipynb))
- [`pod_predictor`](./pod_predictor/): Implementation of the PODPredictor class, including initialization ([`__init__.py`](./pod_predictor/__init__.py)), inference ([`inference.py`](./pod_predictor/inference.py)), and utility functions ([`utils.py`](./pod_predictor/utils.py))
- [`requirements.txt`](./requirements.txt): List of required Python packages for this project
- [`setup.py`](./setup.py): Installation script for setting up the virtual environment
- [`app.py`](./app.py): Simple example script to execute the library
- [`run.py`](./run.py): Wrapper script to run [`app.py`](./app.py) within the virtual enviroment
- [`LICENSE`](./LICENSE): MIT License for this project

## Getting Started
To get started with SA_Delirium, follow these steps:
1. Clone this repository to your local machine using git clone https://github.com/IfGF-UUlm/SA_Delirium.git.
2. Set up the virtual environment by running the provided script: `python3 setup.py`. The script will create the virtual environment, activate it, and install the required dependencies.
3. Run the main script with `python3 run.py` to test the library.
4. Use the provided examples in the examples folder to explore different usage scenarios.

## Dependencies
This project requires Python 3.x and the following packages:
- numpy
- pandas
- scikit-learn
- venn-abers

You can install all dependencies by running `pip install -r requirements.txt`.

## License
This project is licensed under the MIT License.

## Citation
If you use this code in your research, please cite our paper:

[Insert citation information here]

## Contributing

The SA_Delirium library is open to contributions from the community. If you would like to collaborate on the development of this project, please reach out to us at thomas.kocar@uni-ulm.de. We also accept pull requests via GitHub, which should include a clear description of the proposed changes and adhere to standard coding practices. Thank you for considering contributing to SA_Delirium!

## Contact
For any questions, feedback, or concerns, please contact us at thomas.kocar@uni-ulm.de.
