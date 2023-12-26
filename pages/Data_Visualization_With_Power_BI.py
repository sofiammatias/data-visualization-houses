import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Data Visualization with Power BI", page_icon="📊")

st.title("Houses for Sale for loft.br")
st.subheader("Jardim América, São Paulo, Brasil")
st.markdown ("""
This app shows a small demo of data taken by web scraping of a brazilian estate website (loft.br)
and some data visualization about the data retrieved. In this page, you can see data visualization 
graphics done with Power BI (no live data).""")

url_pbi_page = """https://app.powerbi.com/view?r=eyJrIjoiMjQ4NzE2
MjgtZDEwZi00ZWFkLWFmOGMtNzdkZDY4YzMzYWJhIiwid
CI6ImJjMWIyYjg0LWVmMmItNDMyMy1iYzBlLWMwZTc0Yj
ExZmU2ZSIsImMiOjl9&pageName=ReportSection"""

url_pbi_wide = """https://app.powerbi.com/view?r=eyJrIjoiMjQ4NzE2
MjgtZDEwZi00ZWFkLWFmOGMtNzdkZDY4YzMzYWJhIiwid
CI6ImJjMWIyYjg0LWVmMmItNDMyMy1iYzBlLWMwZTc0Yj
ExZmU2ZSIsImMiOjl9"""

components.iframe(url_pbi_page, width=600, height=900)
