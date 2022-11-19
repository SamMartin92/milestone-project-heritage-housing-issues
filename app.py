import streamlit as st
from app_pages.multipage import MultiPage

#import pages scripts
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_correlation_study import page_correlation_study
from app_pages.page_hypotheses_study import page_hyp_study_body
from app_pages.page_ml_model import page_ml_model_body
from app_pages.page_house_price_prediction import page_house_price_prediction_body

app = MultiPage(app_name = "Heritage Housing Project")

#add app pages
app.add_page("Project Summary", page_project_summary_body)
app.add_page("Sale Price Correlation Study", page_correlation_study)
app.add_page("Project Hypotheses", page_hyp_study_body)
app.add_page("ML Model", page_ml_model_body)
app.add_page("House Price Prediction", page_house_price_prediction_body)

app.run()

