import streamlit as st
import pandas as pd
import datetime
from src.data_management.data import load_housing_data, load_inherited_houses_data, load_pkl_file
from src.machine_learning.predict_sale_price_ui import predict_sale_price


def page_house_price_prediction_body():
    version = 'v2'
    df_inherited = load_inherited_houses_data()
    pipeline_regressor = load_pkl_file(
        f"outputs/ml_pipeline/predict_saleprice/{version}/pipeline_regressor.pkl")
    features = (pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
                .columns
                .to_list()
                )

    sale_price_prediction_1 = predict_sale_price(
        df_inherited.iloc[[0]], features, pipeline_regressor)
    sale_price_prediction_2 = predict_sale_price(
        df_inherited.iloc[[1]], features, pipeline_regressor)
    sale_price_prediction_3 = predict_sale_price(
        df_inherited.iloc[[2]], features, pipeline_regressor)
    sale_price_prediction_4 = predict_sale_price(
        df_inherited.iloc[[3]], features, pipeline_regressor)

    st.write(" # Sale Price Prediction:")

    st.info(
        """
        * Our client is interested in predicting the potential sale price of her four inherited properties
        and would like to be able to predict the sale price of other homes in Ames, Iowa, should she wish 
         to buy there in the future.
        * Below are the features and predicted sales prices of her 4 inherited properties:
        """
    )

    st.write(df_inherited)

    st.write(
        f"* **House 1**: Precited Sale Price: ${sale_price_prediction_1}\n"
        f"* **House 2**: Precited Sale Price: ${sale_price_prediction_2}\n"
        f"* **House 3**: Precited Sale Price: ${sale_price_prediction_3}\n"
        f"* **House 4**: Precited Sale Price: ${sale_price_prediction_4}\n"
        f"\n\n"
        f"**Total Expected sale price**: "
        f"${sale_price_prediction_1 + sale_price_prediction_2 + sale_price_prediction_3 + sale_price_prediction_4}"
    )

    st.info(
        """
        * With the below interface, the client can predict the sale price of any home in Ames, Iowa by inputting the 
        the relevant values and running predictive analysis by clicking the 'Predict Sale Price' button.
        """
    )

    X_live = DrawInputWidgets(version, features)
    sale_price_prediction = predict_sale_price(
        X_live, features, pipeline_regressor)

    if st.button("Predict Sale Price"):
        st.success(
            f"* A house with these attributes has an estimated sale price of **${sale_price_prediction}**."
        )


def DrawInputWidgets(version, features):

    df = load_housing_data()

    percentageMin, percentageMax = 0.4, 2.0
    year = datetime.date.today().strftime("%Y")

    col1, col2, col3 = st.beta_columns(3)
    col4, col5, col6 = st.beta_columns(3)

    X_live = pd.DataFrame([], index=[0])


    with col1:
        feature = features[0]
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = features[1]
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col3:
        feature = features[2]
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col4:
        feature = features[3]
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col5:
        feature = features[4]
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(year),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col6:
        feature = features[5]
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(year),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget


    return X_live
