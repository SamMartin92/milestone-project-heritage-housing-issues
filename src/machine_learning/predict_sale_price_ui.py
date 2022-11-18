import streamlit as st

def predict_sale_price(X_live,features, pipeline):

    X_live_features = X_live.filter(features)

    prediction = pipeline.predict(X_live_features)

    st.write(prediction)
