import streamlit as st
from app_pages.multipage import MultiPage

#import pages scripts
from app_pages.page_project_summary import page_project_summary_body

app = MultiPage(app_name = "Heritage Housing Project")

#add app pages
app.add_page("Project Summary", page_project_summary_body)

app.run()

