import streamlit as st
import pandas as pd
from src.data_management.data import load_housing_data, load_inherited_houses_data, load_pkl_file
from src.machine_learning.predict_sale_price_ui import predict_sale_price


def page_house_price_prediction_body():
    version = 'v1'
    df_inherited = load_inherited_houses_data()
    pipeline_regressor = load_pkl_file("outputs/ml_pipeline/predict_saleprice/v1/pipeline_regressor.pkl")
    features = (pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
					.columns
					.to_list()
					)
    




    X_live = DrawInputWidgets(version, features)
    sale_price_prediction = predict_sale_price(X_live, features, pipeline_regressor)



    
    st.write(sale_price_prediction)


    st.write(df_inherited.iloc[[0]])

    sale_price_prediction_1 =predict_sale_price(df_inherited.iloc[[0]], features, pipeline_regressor)

    st.write(sale_price_prediction_1)


    
        



def DrawInputWidgets(version, features):

    df = load_housing_data()
    percentageMin, percentageMax = 0.4, 2.0
    
    col1, col2, col3, col4 = st.beta_columns(4)

    X_live = pd.DataFrame([], index=[0])

    with col1:
        feature = features[0]
        st_widget = st.number_input(
            label = feature,
            min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = features[1]
        st_widget = st.number_input(
            label = feature,
            min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
        )
    X_live[feature] = st_widget

    with col3:
        feature = features[2]
        st_widget = st.number_input(
            label = feature,
            min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
        )
    X_live[feature] = st_widget

    with col4:
        feature = features[3]
        st_widget = st.number_input(
            label = feature,
            min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
        )
    X_live[feature] = st_widget

    return X_live

