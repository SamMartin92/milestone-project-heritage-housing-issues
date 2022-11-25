import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management.data import load_pkl_file
from src.machine_learning.evaluate_regressor import regression_performance, regression_evaluation_plots, curr_version_r2_score


def page_ml_model_body():
    
    # load files
    version = 'v2'
    pipeline_regressor = load_pkl_file(f"outputs/ml_pipeline/predict_saleprice/{version}/pipeline_regressor.pkl")
    feat_importance_plot = plt.imread(f"outputs/ml_pipeline/predict_saleprice/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_test.csv")
    r2_train_score = curr_version_r2_score(X_train, y_train, pipeline_regressor)
    r2_test_score = curr_version_r2_score(X_test, y_test, pipeline_regressor)


    st.write(" ## **ML Pipeline: Predict Sale Price**")

    st.info(
            f"* An ML pipeline was developed to answer our client's second business requirement "
            f"of *'predicting the sale price from any house in Ames, Iowa in case of future property ownership in that area.'*\n"
            f"* It was decided a regressor model would be the most suitable model to predict sale price to our project requirement: "
            f"**An R2 score > 0.75** on train and test sets.\n"
            f"* Version 1 of this pipeline delivered an R2 score of **0.885** & **0.782** on our train and test sets respectively. "
            f"This meets our business requirement.\n"
            f"* Further data cleaning and feature engineering steps have taken place attempting to tune the model to higher score"
            f" and the current version: **'{version}'** delivers an R2 score of:\n"
            f"  * {r2_train_score} on TrainSet\n"
            f"  * {r2_test_score} on TestSet\n"
        
    )

 
    st.write("## ML Pipeline to predict Sale Price of house:")
    st.write(pipeline_regressor)
    
    st.write(
        """
            ### Feature importance

            * Below are the features the current model was trained on and their importance:
        """)
    
    st.write(list(X_train.columns))
    st.image(feat_importance_plot)

    st.write(" ## Pipeline Performance:")

    regression_performance(X_train, y_train, X_test, y_test,pipeline_regressor)

    st.write(" ## Regression Plots:")

    st.write("* Our ML model predictions on the Train & Test Sets")

    regression_evaluation_plots(X_train, y_train, X_test, y_test, pipeline_regressor)


    
