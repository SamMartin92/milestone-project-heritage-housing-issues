import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management.data import load_pkl_file
from src.machine_learning.evaluate_regressor import regression_performance, regression_evaluation_plots


def page_ml_model_body():
    
    # load files
    version = 'v1'
    pipeline_regressor = load_pkl_file(f"outputs/ml_pipeline/predict_saleprice/{version}/pipeline_regressor.pkl")
    feat_importance_plot = plt.imread(f"outputs/ml_pipeline/predict_saleprice/{version}/features_importance.png")
    

    
