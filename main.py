import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#page setup

about_page=st.Page(
page="app/routes/home.py",
title="About",
icon="🏦",
default=True


)

project=st.Page(
    page="app/routes/Real Time Insights.py",
    title="Real Time Insights",
    icon="🗞️"
)

pg=st.navigation(pages=[about_page,project])

pg.run()