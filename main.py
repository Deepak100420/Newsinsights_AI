import streamlit as st

#page setup

about_page=st.Page(
page="app/routes/home.py",
title="About",
icon="🏦",
default=True


)

project=st.Page(
    page="app/routes/page1.py",
    title="Real Time Insights",
    icon="🗞️"
)

pg=st.navigation(pages=[about_page,project])

pg.run()