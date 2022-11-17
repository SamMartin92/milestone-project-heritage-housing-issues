import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_data():
    df = pd.read_csv("outputs/datasets/collection/HousePriceRecords.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_houses_data():
    df = pd.read_csv("outputs/datasets/collection/InheritedHouses.csv")
    return df

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
