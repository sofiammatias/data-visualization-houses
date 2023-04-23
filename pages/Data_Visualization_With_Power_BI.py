import streamlit as st

st.set_page_config(page_title="Data Visualization with Power BI", 
                   page_icon="📊")

st.title ('Houses for Sale for loft.br')
st.subheader ('Jardim América, São Paulo, Brasil')


url_pbi_page = "https://app.powerbi.com/view?r=eyJrIjoiMjQ4NzE2MjgtZDEwZi00ZWFkLWFmOGMtNzdkZDY4YzMzYWJhIiwidCI6ImJjMWIyYjg0LWVmMmItNDMyMy1iYzBlLWMwZTc0YjExZmU2ZSIsImMiOjl9&pageName=ReportSection"
url_pbi_wide = "https://app.powerbi.com/view?r=eyJrIjoiMjQ4NzE2MjgtZDEwZi00ZWFkLWFmOGMtNzdkZDY4YzMzYWJhIiwidCI6ImJjMWIyYjg0LWVmMmItNDMyMy1iYzBlLWMwZTc0YjExZmU2ZSIsImMiOjl9"

st.components.v1.iframe (url_pbi_page, width = 600, height = 900)