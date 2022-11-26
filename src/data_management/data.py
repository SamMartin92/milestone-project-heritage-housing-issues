import streamlit as st
import pandas as pd
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_data():
    """
    Loads House Price dataset as DataFrame
    """
    df = pd.read_csv("outputs/datasets/collection/HousePriceRecords.csv")
    return df


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_houses_data():
    """
    Loads Inherited Houses dataset as DataFrame
    """
    df = pd.read_csv("outputs/datasets/collection/InheritedHouses.csv")
    return df


def load_pkl_file(file_path):
    """
    Loads saved ML pipeline for dashboard use
    """
    return joblib.load(filename=file_path)
