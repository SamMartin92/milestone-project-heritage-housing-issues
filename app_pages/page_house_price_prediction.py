import streamlit as st
import pandas as pd
from src.data_management.data import load_housing_data, load_inherited_houses_data, load_pkl_file
from src.machine_learning.predict_sale_price_ui import predict_sale_price


def page_house_price_prediction_body():
    version = 'v1'
    df = load_housing_data()
    percentageMin, percentageMax = 0.4, 2.0

    fetaures = (pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
					.columns
					.to_list()
					)
    
    

    for i in range(len(fetaures)):
        



# 2ndFlrSF,GarageArea,OverallQual,TotalBsmtSF

def DrawInputWidgets():

    df = load_housing_data()
    percentageMin, percentageMax = 0.4, 2.0

    fetaures = (pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/X_train.csv")
					.columns
					.to_list()
					)
    
    

    for i in range(len(fetaures)):
        print(1)


    #     with col1:
    #         feature = '2ndFlrSF'
    #         st_widget = st.number_input(
    #             label = feature,
    #             options=df[feature].unique()
    #         )
    #     X_live[feature] = st_widget
