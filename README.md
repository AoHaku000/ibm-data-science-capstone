# IBM Applied Data Science Capstone Project - SpaceX Falcon 9 Landing Prediction

## Project Overview
This repository contains the full source code and presentation for the IBM Data Science Professional Certificate Capstone Project. The goal is to predict whether the SpaceX Falcon 9 first-stage booster will land successfully (`Class = 1`) or fail (`Class = 0`), enabling competing launch providers to estimate launch costs accurately.

## Repository Structure
- `Data Science Capstone Project Report.pdf`: Final presentation slide deck.
- `07_plotly_dash_app.py`: Interactive Plotly Dash dashboard application.
- `datasets/`: CSV files produced across all project phases.
- `notebooks/`: Jupyter Notebooks covering Data Collection, Wrangling, EDA, Maps, and ML Models.

## Key Results
- **Predictive Accuracy**: Classification algorithms (Logistic Regression, SVM, Decision Tree, KNN) achieved ~83.3% test accuracy after hyperparameter tuning via `GridSearchCV`.
- **Geographical Insights**: All launch sites are located near ocean coastlines to allow safe initial flight trajectories over water.
