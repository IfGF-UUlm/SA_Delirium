# Post-Operative Delirium Prediction Model
This GitHub repository contains the source code for the SA_Delirium library, a Python package predicting post-operative delirium (POD) in older patients undergoing surgery.

## Project Overview
The SURGE-Ahead (Supporting Surgery with Geriatric Co-Management and AI) project has developed a robust explainable machine learning algorithm to pre-operatively predict POD in geriatric patients. We provide an easy-to-use interface for loading data, preprocessing input features, imputing missing values, calibrating models, and generating predictions.

## Features
The SA_Delirium library offers the following key features:
- **Standard POD Prediction**: Our library provides a robust algorithm for probabilistic POD prediction in geriatric patients undergoing surgery.
- **Feature Importance Calculation**: Understand the impact of individual input features on POD predictions with our built-in feature importance analysis.
- **Calibration**: The model is pre-calibrated on a diverse patient dataset using Platt Scaling; however, we also provide options for re-calibrating the model using Platt scaling or Venn-ABERS. This allows for adaptation to changing patient populations and optimization of performance in the face of distribution shifts.
- **Handling of Missing Values**: SA_Delirium includes flexible imputation tools to address missing data points, ensuring more accurate predictions. Choose from simple imputation methods (mean, median, mode) based on the training dataset or utilize the KNNImputer for more sophisticated handling of missing values.

## Model Training
The POD prediction model was trained on the PAWEL dataset, consisting of 878 patients (209 with POD, 669 without POD), aged 70 years or older, who underwent elective surgery at one of five centers in the state of Baden-Württemberg, Germany between June 2017 and January 2019. It utilizes a linear support vector machine architecture. For a detailed overview of the model training procedure, please refer to the corresponding [GitHub repository](https://github.com/IfGF-UUlm/SURGE-Ahead_Delirium) and the associated publication ([Benovic et al., 2024](https://doi.org/10.1093/ageing/afae101)).

## Project Structure
The repository has the following structure:
- [`data`](./data/): Calibration dataset template ([`calibration_template.csv`](./data/calibration_template.csv)), data transfer template ([`X_test_template.json`](./data/X_test_template.json)) and sample files ([`calibration.csv`](./data/calibration.csv), [`X_test.json`](./data/X_test.json))
- [`examples`](./examples/): Jupyter notebooks demonstrating usage examples for (multiple) calibrated prediction ([`Calibrated_Prediction.ipynb`](./examples/Calibrated_Prediction.ipynb), [`Multiple_Calibrated_Predictions.ipynb`](./examples/Multiple_Calibrated_Predictions.ipynb)), imputation ([`Imputation.ipynb`](./examples/Imputation.ipynb)), and ROC-AUC analysis ([`ROC_AUC.ipynb`](./examples/ROC_AUC.ipynb))
- [`pod_predictor`](./pod_predictor/): Implementation of the PODPredictor class, including initialization ([`__init__.py`](./pod_predictor/__init__.py)), inference ([`inference.py`](./pod_predictor/inference.py)), and utility functions ([`utils.py`](./pod_predictor/utils.py))
- [`requirements.txt`](./requirements.txt): List of required Python packages for this project
- [`setup.py`](./setup.py): Installation script for setting up the virtual environment
- [`app.py`](./app.py): Simple example script to execute the library
- [`run.py`](./run.py): Wrapper script to run [`app.py`](./app.py) within the virtual enviroment
- [`LICENSE`](./LICENSE): MIT License for this project

## Getting Started
To get started with SA_Delirium, follow these steps:
1. Clone this repository to your local machine using `git clone https://github.com/IfGF-UUlm/SA_Delirium.git`.
2. Set up the virtual environment by running the provided script: `python3 setup.py`. The script will create the virtual environment, activate it, and install the required dependencies.
3. Run the main script with `python3 run.py` to test the library.
4. Use the provided examples in the examples folder to explore different usage scenarios.

## Data Input
The SA_Delirium library accepts the following data types as input:
- Numpy array 
- Python dictionary 
- Pandas DataFrame 
- Json ([template](./data/X_test_template.json) provided)

The following features are used for POD prediction:
- Estimated Cut-to-Suture Time (minutes): The estimated cut-to-suture time can be either the surgeon's estimation or the empirical mean time of the procedure.
- Age (months): Age in months.
- GFR (Cockcroft-Gault, ml/min): Estimated glomerular filtration rate using the Cockcroft-Gault Formula.
- ASA Class (score): American Society of Anesthesiologists physical status classification system.
- MoCA Orientation (subscore): Montreal Cognitive Assessment (MoCA) Orientation subscore.
- MoCA Memory (subscore): Montreal Cognitive Assessment (MoCA) Memory subscore.
- Number of Medications (n): Number of long-term medications, excluding on-demand medication.
- Multimorbidity (score): Modified Charlson Comorbidity Index (CCI). The considered co-morbidities were myocardial infarction, congestive heart failure, peripheral vascular disease, cerebrovascular disease, dementia, chronic pulmonary disease (1 point each), liver disease (1 if mild, else 3), diabetes mellitus (1 if without complications, else 2), and renal disease (2 points).
- Clinical Frailty Scale (score): Frailty assessment using the [Clinical Frailty Scale](https://www.bgs.org.uk/sites/default/files/content/attachment/2018-07-05/rockwood_cfs.pdf).
- MoCA Verbal Fluency (subscore): Montreal Cognitive Assessment (MoCA) Verbal Fluency subscore.
- Dementia (Yes/No): Presence of dementia.
- Recent Fall (Yes/No): Fall(s) within the last 3 months.
- Post-OP Isolation (Yes/No): Anticipated isolation after the operation, e.g., due to antibiotic-resistant bacteria.
- Pre-OP Benzodiazepines (Yes/No): Use of pre-operative benzodiazepines, either as (on-demand) premedication or long-term medication.
- Cardio-Pulmonary Bypass (Yes/No): Use of cardio-pulmonary bypass during surgery.
To save time, the 5-minute version of the MoCA ([Wong et al. 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4373962/)) can also be used, with the original scoring system from the full MoCA applied to each subscore.

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

[The associated paper has been submitted for publication. The citation details will be updated once the paper is accepted.]

## Contributing

The SA_Delirium library is open to contributions from the community. If you would like to collaborate on the development of this project, please reach out to us at thomas.kocar@uni-ulm.de. We also accept pull requests via GitHub, which should include a clear description of the proposed changes and adhere to standard coding practices. Thank you for considering contributing to SA_Delirium!

## Contact
For any questions, feedback, or concerns, please contact us at thomas.kocar@uni-ulm.de.
