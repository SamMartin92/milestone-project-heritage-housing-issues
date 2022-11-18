import streamlit as st

def predict_sale_price(X_live,features, pipeline):

    X_live_features = X_live.filter(features)

    prediction = float(pipeline.predict(X_live_features).round(2))

    return prediction

