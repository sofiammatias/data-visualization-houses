import streamlit as st

st.set_page_config(page_title="Web Scraping Data", 
                   page_icon="📊")


url_pbi_page = "https://app.powerbi.com/view?r=eyJrIjoiMjQ4NzE2MjgtZDEwZi00ZWFkLWFmOGMtNzdkZDY4YzMzYWJhIiwidCI6ImJjMWIyYjg0LWVmMmItNDMyMy1iYzBlLWMwZTc0YjExZmU2ZSIsImMiOjl9&pageName=ReportSection"
url_pbi_wide = "https://app.powerbi.com/view?r=eyJrIjoiMjQ4NzE2MjgtZDEwZi00ZWFkLWFmOGMtNzdkZDY4YzMzYWJhIiwidCI6ImJjMWIyYjg0LWVmMmItNDMyMy1iYzBlLWMwZTc0YjExZmU2ZSIsImMiOjl9"

st.components.v1.iframe (url_pbi_page, width = 600, height = 900)